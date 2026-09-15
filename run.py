import pandas as pd
from dataset_maker import make_dataset as md
from calculate import main as m
try:
    df = pd.read_csv('Sales_Data.csv', index_col=0)
except FileNotFoundError:
    md()
    df = pd.read_csv('Sales_Data.csv', index_col=0)
m(df)
