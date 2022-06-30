from config.silen_ten import silence_tensorflow
silence_tensorflow()
from config.environ import test_money
from config.symbols import tune_sym_dict, tune_year, tune_month, tune_day, tune_days
from config.model_repository import models
from functions.trade_functs import get_api, get_stock_portion_adjuster
from functions.time_functs import get_calendar, increment_calendar, get_actual_price
from functions.error_functs import error_handler, keyboard_interrupt
from functions.tuner_functs import subset_and_predict, get_user_input
from functions.paca_model_functs import get_current_price
from functions.data_load_functs import get_proper_df, df_subset
from functions.time_functs import get_past_datetime
from functions.functions import check_directories, r2
from paca_model import configure_gpu
from statistics import mean
import datetime
import time


def simulate_trades(tune_year, tune_month, tune_day, tune_days, params):
    time_s = time.perf_counter()

    api = get_api()
    configure_gpu()
        
    tune_symbols, params = get_user_input(tune_sym_dict, params)

    days_done = 1

    master_df_dict = {}
    portfolio = {
        "cash": test_money,
        "equity": test_money,
        "owned": {},
        "buy_prices": {},
    }

    symbol = "SPY"
    try:
        tmp_cal = get_calendar(get_past_datetime(tune_year, tune_month, tune_day), api, symbol)
        spy_df = get_proper_df(symbol, params["LIMIT"], "V2")
        spy_start_price = get_actual_price((get_past_datetime(tune_year, tune_month, tune_day) 
            - datetime.timedelta(1)), spy_df, tmp_cal)

        current_date = get_past_datetime(tune_year, tune_month, tune_day)
        starting_prices = []
        for symbol in tune_symbols:
            master_df_dict[symbol] = get_proper_df(symbol, params["LIMIT"], "V2")
            starting_prices.append(get_actual_price((get_past_datetime(tune_year, tune_month, tune_day) 
            - datetime.timedelta(1)), master_df_dict[symbol], tmp_cal))
            
        print(starting_prices)

        # tmp_cal = get_calendar(get_past_datetime(tune_year, tune_month, tune_day), api, "AAPL")
        # starting_day_price = get_actual_price((get_past_datetime(tune_year, tune_month, tune_day) 
        #     - datetime.timedelta(1)), master_df_dict[symbol], tmp_cal)

        calendar = get_calendar(current_date, api, "AAPL")

        while days_done <= tune_days:
            time_d = time.perf_counter()
            print(f"\nCurrently on day {days_done} of {tune_days} \n")
            print(current_date)

            pred_curr_list = {}
            current_date = increment_calendar(current_date, calendar)

            for symbol in tune_symbols:
                predicted_price, current_price, epochs_run, sub_df, data_dict = subset_and_predict(symbol, 
                            params, current_date, master_df_dict[symbol], to_print=False)
                # actual_price = get_actual_price(current_date, master_df_dict[symbol], calendar)
                # p_diff = round((abs(actual_price - predicted_price) / actual_price) * 100, 2)
                pred_curr_list[symbol] = {"predicted": predicted_price, "current": current_price}


            # recalculate equity
            portfolio["equity"] = 0.0
            for symbol in portfolio["owned"]:
                portfolio["equity"] += portfolio["owned"][symbol]["qty"] * pred_curr_list[symbol]["current"]
            portfolio["equity"] += portfolio["cash"]
            
            # sell block
            buy_list = []
            for symbol in tune_symbols:
                if pred_curr_list[symbol]["predicted"] > pred_curr_list[symbol]["current"]:
                    if symbol not in portfolio["owned"]:
                        buy_list.append(symbol)
                else :
                    #sell
                    if symbol in portfolio["owned"]:
                        portfolio["cash"] += portfolio["owned"][symbol]["qty"] * pred_curr_list[symbol]["current"]
                        portfolio["owned"].pop(symbol)
            
            # calculate splits
            value_in_stocks_before = round((1 - (portfolio["cash"] / portfolio["equity"])) * 100, 2)
            stock_portion_adjuster = get_stock_portion_adjuster(value_in_stocks_before, buy_list)

            # buy block
            for symbol in buy_list:
                # buy
                if pred_curr_list[symbol]["predicted"] > pred_curr_list[symbol]["current"]:
                    buy_qty = (portfolio["cash"] / stock_portion_adjuster) // pred_curr_list[symbol]["current"]

                    if buy_qty == 0:
                        # print("PROBLEM HERE MAYBE?")
                        continue

                    portfolio["owned"][symbol] = {"buy_price": pred_curr_list[symbol]["current"], "qty": buy_qty}
                    portfolio["cash"] -= portfolio["owned"][symbol]["qty"] * pred_curr_list[symbol]["current"]
            

            print(f"""end of day ... equity:{r2(portfolio["equity"])} cash:{r2(portfolio["cash"])}\n""", flush=True)
            
            print(portfolio["owned"])
            days_done += 1
            print(f"Running this day took {r2((time.perf_counter() - time_d))} seconds")
    
    except KeyboardInterrupt:
        keyboard_interrupt()
    except Exception:
        error_handler(symbol, Exception)
    

    spy_sub_df = df_subset(current_date, spy_df)
    spy_end_price = get_current_price(spy_sub_df)

    current_prices = []
    for symbol in pred_curr_list:
        current_prices.append(pred_curr_list[symbol]["current"])

    
    time_so_far = time.perf_counter() - time_s
    print(f"\nThe total value of the portfolio was {r2(portfolio['equity'])} with {r2(portfolio['cash'])} being in cash at the end")
    print(f"It was holding these {portfolio['owned']} stocks")
    print(f"Over the same period holding this group would have made {r2(test_money * (mean(current_prices) / mean(starting_prices)))}\n"
        f" and holding the S&P would have made {r2(test_money * (spy_end_price / spy_start_price))}")
    print(f"Testing all of the days took {r2(time_so_far / 3600)} hours or {int(time_so_far // 3600)}:"
        f"{int((time_so_far / 3600 - (time_so_far // 3600)) * 60)} minutes.")


if __name__ == "__main__":
    check_directories()
    params = {
        "ENSEMBLE": ["nn11"],
        "TRADING": False,
        "SAVE_FOLDER": "",
        "LIMIT": 4000,
    }

    for model in params["ENSEMBLE"]:
        if model in models:
            params[model] = models[model]

    simulate_trades(tune_year, tune_month, tune_day, tune_days, params)
    
