from pandas import read_csv
from pandas.plotting import scatter_matrix
from matplotlib import pyplot as plt

dataset = read_csv('https://www.quandl.com/api/v3/datasets/EOD/WMT.csv?api_key=tHUig52wPMmBP8xuxces')
print(dataset)
