from alpaca_neural_net import make_neural_net
import os
import sys


def replace(file, param, new_val):
    f = open(file, 'r')
    lines = []
    for line in f:
        if line.strip().split(',')[0].strip() == param:
            line = param+','+str(new_val)+'\n'
        lines.append(line)
    f.close()
    f = open(file, 'w')
    for line in lines:
        f.write(line)
    f.close()


def find_best_stats(ticker):
    directory = 'config'
    if not os.path.isdir(directory):
        os.mkdir(directory)
    f_name = directory + '/' + ticker + '.csv'
    #unit = find_best_units(ticker)
    #f = open(f_name, 'w')
    #f.write('UNITS,'+str(unit))
    #f.close()
    dropout = find_best_dropout(ticker)
    f = open(f_name, 'a')
    f.write('DROPOUT,'+str(dropout)+'\n')
    f.close()
    n_step = find_best_n_steps(ticker)
    f = open(f_name, 'a')
    f.write('N_STEPS,'+str(n_step)+'\n')
    f.close()
    epoch = find_best_epochs(ticker)
    f = open(f_name, 'a')
    f.write('EPOCH,'+str(epoch)+'\n')
    f.close()


def get_file_name(ticker):
    directory = 'config'
    if not os.path.isdir(directory):
        os.mkdir(directory)
    f_name = directory + '/' + ticker + '.csv'
    return f_name


def find_best_units(ticker):
    UNIT_VALS = [256, 320, 384, 448]
    best_unit = UNIT_VALS[0]
    best_acc = 0
    for unit in UNIT_VALS:
        perc, acc = make_neural_net(ticker, UNITS=unit, EPOCHS=1000)
        if acc > best_acc:
            best_acc = acc
            best_unit = unit
    f_name = get_file_name(ticker)


def find_best_dropout(ticker):
    DROPOUTS = [.3, .325, .35, .375, .4, .425]
    best_drop = DROPOUTS[0]
    best_acc = 0
    for drop in DROPOUTS:
        perc, acc = make_neural_net(ticker, DROPOUT=drop, EPOCHS=1000)
        if acc > best_acc:
            best_acc = acc
            best_drop = drop
    f_name = get_file_name(ticker)
    

def find_best_n_steps(ticker):
    N_STEP_VALS = [50, 100, 150, 200, 250, 300]
    best_step = N_STEP_VALS[0]
    best_acc = 0
    for step in N_STEP_VALS:
        perc, acc = make_neural_net(ticker, N_STEPS=step, EPOCHS=1000)
        if acc > best_acc:
            best_acc = acc
            best_step = step
    f_name = get_file_name(ticker)


def find_best_epochs(ticker):
    EPOCH_VALS = [500, 1000, 1500, 2000]
    best_epoch = EPOCH_VALS[0]
    best_acc = 0
    for epoch in EPOCH_VALS:
        perc, acc = make_neural_net(ticker, EPOCHS=epoch)
        if acc > best_acc:
            best_acc = acc
            best_epoch = epoch
    f_name = get_file_name(ticker)


def possibleArgPrinting():
    print('The accepted arguments are EPOCHS | DROPOUT | UNITS | N_STEPS')


if __name__ == '__main__':
    args = sys.argv
    #args[0] is the name of the file
    #args[1] is the parameter to test
    #args[2] is the ticker to test on
    if len(args) < 3:
        print('You need to pass in a parameter to test and a ticker to test it on')
        possibleArgPrinting()
        sys.exit(-1)
    ticker = args[2]
    if args[1] == 'EPOCHS':
        find_best_epochs(ticker)
    elif args[1] == 'DROPOUT':
        find_best_dropout(ticker)
    elif args[1] == 'UNITS':
        find_best_units(ticker)
    elif args[1] == 'N_STEPS':
        find_best_n_steps(ticker)
    else:
        print('The paramter you listed is not one of the accepted parameters')
        possibleArgPrinting()
    sys.exit(-1)

