from functions.volitility import *
from functions.sentiment import vad_sentiment, fin_bert_sentiment
from scipy.signal import savgol_filter
import talib as ta
import pandas as pd
import pywt
import matplotlib.pyplot as plt
import time
from statistics import mean

base_features = ["o", "c", "l", "h", "v", "tc", "vwap"]

def df_m(name, df, *args):
    df[name] = (df.l + df.h) / 2

def df_savgol(selector, feature, df, symbol):
    if feature not in base_features:
        techs_dict[feature]["function"](feature, df, symbol)

    df[f"{selector}.{feature}"] = savgol_filter(df[feature], 7, 3)

def df_no_cheat_savgol(selector, feature, df, symbol):
    ncs = []

    window = 7

    for i in range(1, len(df) + 1):
        if i < window:
            ncs.append(np.nan)
            continue

        ncs.append(savgol_filter(df.c[:i], 7, 3)[-1])

    df[f"{selector}.{feature}"] = ncs

def df_change_percent(selector, feature, df, symbol):
    if feature not in base_features:
        techs_dict[feature]["function"](feature, df, symbol)
    df[f"{selector}.{feature}"] = df[feature].pct_change()

def df_differencer(selector, feature, df, symbol):
    if feature not in base_features:
        techs_dict[feature]["function"](feature, df, symbol)
    df[f"{selector}.{feature}"] = df[feature].diff(1)

def df_power_transformation(selector, feature, df, symbol):
    if feature not in base_features:
        techs_dict[feature]["function"](feature, df, symbol)
    df[f"{selector}.{feature}"] = df[feature].pow(.5)

def df_moving_average(selector, feature, df, symbol):
    if feature not in base_features:
        techs_dict[feature]["function"](feature, df, symbol)
    df[f"{selector}.{feature}"] = ta.SMA(df[feature], timeperiod=7)

def df_exponential_smoothing(selector, feature, df, symbol):
    if feature not in base_features:
        techs_dict[feature]["function"](feature, df, symbol)
    df[f"{selector}.{feature}"] = ta.EMA(df[feature], timeperiod=7)

def df_wavelet_transform(selector, feature, df, symbol):
    if feature not in base_features:
        techs_dict[feature]["function"](feature, df, symbol)

    std = np.nanstd(df[feature])

    # thresh = .04 # smooths more than sav_gol
    thresh = std/np.nanmax(df[feature]) # smooths more than above
    thresh = thresh*np.nanmax(df[feature])
    coeff = pywt.wavedec(df[feature], "db4", mode="smooth" )
    coeff[1:] = (pywt.threshold(i, value=thresh, mode="soft") for i in coeff[1:])
    reconstructed_signal = pywt.waverec(coeff, 'db4', mode="smooth")

    df[f"{selector}.{feature}"] = reconstructed_signal[len(reconstructed_signal) - len(df.index):]

def df_BBANDS(name, df, *args):
    high, mid, dow = ta.BBANDS(df.c, timeperiod=10, nbdevup=2, nbdevdn=2, matype=0)
    if name == "high_band":
        df[name] = high
    else:
        df[name] = dow

def df_OBV(name, df, *args):
    df[name] = ta.OBV(df.c, df.v)

def df_RSI(name, df, *args):
    df[name] = ta.RSI(df.c)

def df_lin_reg(name, df, *args):
    df[name] = ta.LINEARREG(df.c, timeperiod=14)

def df_lin_reg_ang(name, df, *args):
    df[name] = ta.LINEARREG_ANGLE(df.c, timeperiod=14)
    
def df_lin_reg_int(name, df, *args):
    df[name] = ta.LINEARREG_INTERCEPT(df.c, timeperiod=14)

def df_lin_reg_slope(name, df, *args):
    df[name] = ta.LINEARREG_SLOPE(df.c, timeperiod=14)

def df_pears_cor(name, df, *args):
    df[name] = ta.CORREL(df.h, df.l, timeperiod=30)

def df_mon_flow_ind(name, df, *args):
    df[name] = ta.MFI(df.h, df.l, df.c, df.v, timeperiod=14)

def df_willR(name, df, *args):
    df[name] = ta.WILLR(df.h, df.l, df.c, timeperiod=14)

def df_std_dev(name, df, *args):
    df[name] = ta.STDDEV(df.c, timeperiod=5, nbdev=1)

def df_minmax(name, df, *args):
    min, max = ta.MINMAX(df.c, timeperiod=30)
    if name == "min":
        df[name] = min
    else:
        df[name] = max

def df_commod_chan_ind(name, df, *args):
    df[name] = ta.CCI(df.h, df.l, df.c, timeperiod=14)

def df_para_SAR(name, df, *args):
    df[name] = ta.SAR(df.h, df.l)

def df_para_SAR_ext(name, df, *args):
    df[name] = ta.SAREXT(df.h, df.l)

def df_rate_of_change(name, df, *args):
    df[name] = ta.ROC(df.c, timeperiod=10)

def df_ht_dcperiod(name, df, *args):
    df[name] = ta.HT_DCPERIOD(df.c)

def df_ht_trendmode(name, df, *args):
    df[name] = ta.HT_TRENDMODE(df.c)

def df_ht_dcphase(name, df, *args):
    df[name] = ta.HT_DCPHASE(df.c)

def df_ht_phasor(name, df, *args):
    inphase, quad = ta.HT_PHASOR(df.c)
    if name == "ht_inphase":
        df[name] = inphase
    else:
        df[name] = quad

def df_ht_sine(name, df, *args):
    ht_sine, ht_leadsine = ta.HT_SINE(df.c)
    if name == "ht_sine":
        df[name] = ht_sine
    else:
        df[name] = ht_leadsine

def df_ht_trendline(name, df, *args):
    df[name] = ta.HT_TRENDLINE(df.c)

def df_mom(name, df, *args):
    df[name] = ta.MOM(df.c, timeperiod=10)

def df_abs_price_osc(name, df, *args):
    df[name] = ta.APO(df.c, fastperiod=12, slowperiod=26, matype=0)

def df_KAMA(name, df, *args):
    df[name] = ta.KAMA(df.c, timeperiod=30)

def df_typ_price(name, df, *args):
    df[name] = ta.TYPPRICE(df.h, df.l, df.c)

def df_ult_osc(name, df, *args):
    df[name] = ta.ULTOSC(df.h, df.l, df.c, timeperiod1=7, timeperiod2=14, timeperiod3=28)

def df_chai_line(name, df, *args):
    df[name] = ta.AD(df.h, df.l, df.c, df.v)

def df_chai_osc(name, df, *args):
    df[name] = ta.ADOSC(df.h, df.l, df.c, df.v, fastperiod=3, slowperiod=10)

def df_norm_avg_true_range(name, df, *args):
    df[name] = ta.NATR(df.h, df.l, df.c, timeperiod=14)

def df_median_price(name, df, *args):
    df[name] = ta.MEDPRICE(df.h, df.l)

def df_var(name, df, *args):
    df[name] = ta.MEDPRICE(df.h, df.l)

def df_aroon(name, df, *args):
    aroon_down, aroon_up = ta.AROON(df.h, df.l, timeperiod=14)
    if name == "aroon_down":
        df[name] = aroon_down
    else:
        df[name] = aroon_up

def df_aroon_osc(name, df, *args):
    df[name] = ta.AROONOSC(df.h, df.l, timeperiod=14)

def df_bal_of_pow(name, df, *args):
    df[name] = ta.BOP(df.o, df.h, df.l, df.c)

def df_chande_mom_osc(name, df, *args):
    df[name] = ta.CMO(df.c, timeperiod=14)

def df_MACD(name, df, *args):
    macd, macdsignal, macdhist = ta.MACD(df.c, fastperiod=12, slowperiod=26, signalperiod=9)
    if name == "MACD":
        df[name] = macd
    elif name == "MACD_signal":
        df[name] = macdsignal
    else:
        df[name] = macdhist

def df_con_MACD(name, df, *args):
    con_MACD, con_MACD_signal, con_MACD_hist = ta.MACDEXT(df.c, fastperiod=12, slowperiod=26, signalperiod=9)
    if name == "con_MACD":
        df[name] = con_MACD
    elif name == "con_MACD_signal":
        df[name] = con_MACD_signal
    else:
        df[name] = con_MACD_hist

def df_fix_MACD(name, df, *args):
    fix_MACD, fix_MACD_signal, fix_MACD_hist = ta.MACDFIX(df.c, signalperiod=9)
    if name == "fix_MACD":
        df[name] = fix_MACD
    elif name == "fix_MACD_signal":
        df[name] = fix_MACD_signal
    else:
        df[name] = fix_MACD_hist

def df_min_dir_ind(name, df, *args):
    df[name] = ta.MINUS_DI(df.h, df.l, df.c, timeperiod=14)

def df_min_dir_mov(name, df, *args):
    df[name] = ta.MINUS_DM(df.h, df.l, timeperiod=14)

def df_plus_dir_ind(name, df, *args):
    df[name] = ta.PLUS_DI(df.h, df.l, df.c, timeperiod=14)

def df_plus_dir_mov(name, df, *args):
    df[name] = ta.PLUS_DM(df.h, df.l, timeperiod=14)

def df_per_price_osc(name, df, *args):
    df[name] = ta.PPO(df.c, fastperiod=12, slowperiod=26, matype=0)

def df_stoch_fast(name, df, *args):
    stoch_fast_k, stoch_fast_d = ta.STOCHF(df.h, df.l, df.c)
    if name == "stoch_fast_k":
        df[name] = stoch_fast_k
    else:
        df[name] = stoch_fast_d

def df_stoch_rel_stren(name, df, *args):
    stoch_rel_stren_k, stoch_rel_stren_d = ta.STOCHRSI(df.c)
    if name == "stoch_rel_stren_k":
        df[name] = stoch_rel_stren_k
    else:
        df[name] = stoch_rel_stren_d

def df_stoch_slow(name, df, *args):
    stoch_slowk, stoch_slowd = ta.STOCHF(df.h, df.l, df.c)
    if name == "stoch_slowk":
        df[name] = stoch_slowk
    else:
        df[name] = stoch_slowd

def df_TRIX(name, df, *args):
    df[name] = ta.TRIX(df.c, timeperiod=30)

def df_weigh_mov_avg(name, df, *args):
    df[name] = ta.WMA(df.c, timeperiod=30)

def df_DEMA(name, df, *args):
    df[name] = ta.DEMA(df.c, timeperiod=30)



def df_MESA(name, df, *args):
    MESA_mama, MESA_fama = ta.MAMA(df.c)
    if name == "MESA_mama":
        df[name] = MESA_mama
    else:
        df[name] = MESA_fama

def df_midpnt(name, df, *args):
    df[name] = ta.MIDPOINT(df.c, timeperiod=14)

def df_midprice(name, df, *args):
    df[name] = ta.MIDPRICE(df.h, df.l, timeperiod=14)

def df_triple_EMA(name, df, *args):
    df[name] = ta.TEMA(df.c, timeperiod=30)

def df_tri_MA(name, df, *args):
    df[name] = ta.TRIMA(df.c, timeperiod=30)

def df_avg_dir_mov_ind(name, df, *args):
    df[name] = ta.ADX(df.h, df.l, df.c, timeperiod=14)

def df_true_range(name, df, *args):
    df[name] = ta.TRANGE(df.h, df.l, df.c)

def df_avg_price(name, df, *args):
    df[name] = ta.AVGPRICE(df.o, df.h, df.l, df.c)

def df_weig_c_price(name, df, *args):
    df[name] = ta.WCLPRICE(df.h, df.l, df.c)

def df_beta(name, df, *args):
    df[name] = ta.BETA(df.h, df.l, timeperiod=5)

def df_TSF(name, df, *args):
    df[name] = ta.TSF(df.c, timeperiod=14)

def convert_date_values(name, df, *args):	    
    df[name] = df.index	
    df[name] = pd.to_datetime(df[name])
    df[name] = df[name].dt.weekday + 1
    

def df_pass(name, df, symbol):
    pass

def testing(name, df, *args):
    # df["old_s.c"] = savgol_filter(df["c"], 7, 3)
    print("HELLO? YOU PLAY TO WIN THE GAME?")
    s = time.perf_counter()
    print(mean(df["c"].pct_change()))
    print(f"time to calc sav_gol {time.perf_counter() - s}")


        
    

techs_dict = {
    "s": {"function":df_savgol},
    "ncs": {"function":df_no_cheat_savgol},
    "pc": {"function":df_change_percent},
    "d": {"function":df_differencer},
    "wt": {"function":df_wavelet_transform},
    "pt": {"function":df_power_transformation},
    "ma": {"function":df_moving_average},
    "es": {"function":df_exponential_smoothing},
    "m": {"function":df_m},
    "vad": {"function":vad_sentiment},
    "fin_vad": {"function":vad_sentiment},
    "fin_bert_pos": {"function":fin_bert_sentiment},
    "fin_bert_neg": {"function":df_pass},
    "fin_bert_neu": {"function":df_pass},
    "garman_klass":  {"function":garman_klass},
    "hodges_tompkins": {"function":hodges_tompkins},
    "kurtosis": {"function":get_kurtosis},
    "parkison": {"function":parkinson},
    "rogers_stachell": {"function":rogers_stachell},
    "skew": {"function":get_skew},
    "yang_zhang" : {"function":yang_zhang},
    "high_band": {"function":df_BBANDS},
    "low_band": {"function":df_BBANDS},
    "OBV": {"function":df_OBV},
    "RSI": {"function":df_RSI},
    "lin_reg": {"function":df_lin_reg},
    "lin_reg_ang": {"function":df_lin_reg_ang},
    "lin_reg_slope": {"function":df_lin_reg_slope},
    "lin_reg_int": {"function":df_lin_reg_int},
    "pears_cor": {"function":df_pears_cor},
    "mon_flow_ind": {"function":df_mon_flow_ind},
    "willR": {"function":df_willR},
    "std_dev": {"function":df_std_dev},
    "min": {"function":df_minmax},
    "max": {"function":df_minmax},
    "commod_chan_ind": {"function":df_commod_chan_ind},
    "para_SAR": {"function":df_para_SAR},
    "para_SAR_ext": {"function":df_para_SAR_ext},
    "rate_of_change": {"function":df_rate_of_change},
    "ht_dcperiod": {"function":df_ht_dcperiod},
    "ht_trendmode": {"function":df_ht_trendmode},
    "ht_dcphase": {"function":df_ht_dcphase},
    "ht_inphase": {"function":df_ht_phasor},
    "quadrature": {"function":df_ht_phasor},
    "ht_sine": {"function":df_ht_sine},
    "ht_leadsine": {"function":df_ht_sine},
    "ht_trendline": {"function":df_ht_trendline},
    "mom": {"function":df_mom},
    "abs_price_osc": {"function":df_abs_price_osc},
    "KAMA": {"function":df_KAMA},
    "typ_price": {"function":df_typ_price},
    "ult_osc": {"function":df_ult_osc},
    "chai_line": {"function":df_chai_line},
    "chai_osc": {"function":df_chai_osc},
    "norm_avg_true_range": {"function":df_norm_avg_true_range},
    "median_price": {"function":df_median_price},
    "var": {"function":df_var},
    "aroon_down": {"function":df_aroon},
    "aroon_up": {"function":df_aroon},
    "aroon_osc": {"function":df_aroon_osc},
    "bal_of_pow": {"function":df_bal_of_pow},
    "chande_mom_osc": {"function":df_chande_mom_osc},
    "MACD": {"function":df_MACD},
    "MACD_signal": {"function":df_MACD},
    "MACD_hist": {"function":df_MACD},
    "con_MACD": {"function":df_con_MACD},
    "con_MACD_signal": {"function":df_con_MACD},
    "con_MACD_hist": {"function":df_con_MACD},
    "fix_MACD": {"function":df_fix_MACD},
    "fix_MACD_signal": {"function":df_fix_MACD},
    "fix_MACD_hist": {"function":df_fix_MACD},
    "min_dir_ind": {"function":df_min_dir_ind},
    "min_dir_mov": {"function":df_min_dir_mov},
    "plus_dir_ind": {"function":df_plus_dir_ind},
    "plus_dir_mov": {"function":df_plus_dir_mov},
    "per_price_osc": {"function":df_per_price_osc},
    "stoch_fast_k": {"function":df_stoch_fast},
    "stoch_fast_d": {"function":df_stoch_fast},
    "stoch_rel_stren_k": {"function":df_stoch_rel_stren},
    "stoch_rel_stren_d": {"function":df_stoch_rel_stren},
    "stoch_slowk": {"function":df_stoch_slow},
    "stoch_slowd": {"function":df_stoch_slow},
    "TRIX": {"function":df_TRIX},
    "weigh_mov_avg": {"function":df_weigh_mov_avg},
    "DEMA": {"function":df_DEMA},
    "MESA_mama": {"function":df_MESA},
    "MESA_fama": {"function":df_MESA},
    "midpnt": {"function":df_midpnt},
    "midprice": {"function":df_midprice},
    "triple_EMA": {"function":df_triple_EMA},
    "tri_MA": {"function":df_tri_MA},
    "avg_dir_mov_ind": {"function":df_avg_dir_mov_ind},
    "true_range": {"function":df_true_range},
    "weig_c_price": {"function":df_weig_c_price},
    "avg_price": {"function":df_avg_price},
    "beta": {"function":df_beta},
    "TSF": {"function":df_TSF},
    "day_of_week": {"function":convert_date_values},
    "testing": {"function":testing}
}

