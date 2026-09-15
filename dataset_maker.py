import pandas as pd
import numpy as np
def make_data():
        products_prices = {'Phone':30, 'TV':70, 'Printer':40, 'Laptop':80, 'Computer':120, 'Charger':1.5, 'Memorys':10, 'PlayStation':150, 'Xbox':100}
        date = np.arange('2025-01-01', '2026-01-01', dtype='datetime64[D]')
        sells = np.arange(1, 5)
        choosed_products = np.random.choice(np.array(list(products_prices.keys())), size=100, p=[0.20, 0.05, 0.10, 0.15, 0.05, 0.25, 0.10, 0.05, 0.05])
        choosed_sells = np.random.choice(sells, size=100, p=[0.40, 0.30, 0.20, 0.10])
        choosed_dates = np.random.choice(date, size=100)
        choosed_bprices = np.array([(products_prices[x]) for x in (choosed_products)])
        choosed_tprices = np.array(choosed_bprices * choosed_sells)

        return {'Product' : choosed_products,
                'Total Sell' : choosed_sells,
                'Base Price' : choosed_bprices,
                'Total Price' : choosed_tprices,
                'Date' : choosed_dates}

def make_dataset():
        (pd.DataFrame(make_data())).to_csv('Sales_Data.csv', encoding='utf-8-sig')
