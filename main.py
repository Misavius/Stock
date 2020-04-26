from pandas import read_csv
import pandas as pd
from pandas.plotting import scatter_matrix
from matplotlib import pyplot as plt
from api_key import api_key
names = ['Date','Open','High','Low','Close','Volume','Dividend','Split','Adj_Open','Adj_High','Adj_Low','Adj_Close','Adj_Volume']
#dataset = read_csv('https://www.quandl.com/api/v3/datasets/EOD/WMT.csv?api_key=' + api_key)
#print(dataset)
dataset = read_csv('EOD-WMT.csv', names=names)
dataset['Date'] = pd.to_datetime(dataset.Date, format='%Y-%m-%d')
dataset.index = dataset['Date']
data = dataset.sort_index(ascending=True, axis=0)
new_data = pd.DataFrame(index=range(0, len(dataset)), columns=['Date', 'Close'])
for i in range(0, len(data)):
    new_data['Date'][i] = data['Date'][i]
    new_data['Close'][i] = data['Close'][i]



