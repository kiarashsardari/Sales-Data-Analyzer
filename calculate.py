import matplotlib.pyplot as plt 
import pandas as pd
def summary(df):

    df['Month'] = df['Date'].dt.month
    result = df.groupby('Month')['Total Price'].sum()
    for n, s in result.items():
        print(f'month: {n} | sale prices: {s}')
def best_product(df):
    s_p = df.groupby('Product')['Total Price'].sum()
    dic = {}
    for n,s in s_p.items():
        dic[n] = s
    target = max(dic.values())
    lst = [k for k,v in dic.items() if v == target]
    for k in lst :
        print(f'best product: {k} | total sell: {dic[k]}')
def vector(df):
    sdf = df.sort_values(by='Date')
    g = sdf.groupby('Date')['Total Price'].sum()
    date = [dte for dte, tp in g.items()]
    tprice = [tp for dte, tp in g.items()]
    plt.plot(date, tprice)
    plt.show()
def main(df):
    df['Date'] = pd.to_datetime(df['Date'])
    summary(df)
    input('press enter to show best product...')
    best_product(df)
    input('press enter to show sale vector...')
    vector(df)

    






'''    date = data_frame['Date'].tolist()
    price = data_frame['Total Price'].tolist()
    sell = data_frame['Total Sell'].tolist()
    lst = ['01','02','03','04','05','06','07','08','09','10','11','12']
    indx = 0
    months_range = [0]
    next_m_indx = 0
    while indx!=12 :
        for dt in date[next_m_indx:]:
            if dt[5:7] != lst[indx]:
                next_m_indx = date.index(dt)
                months_range.append(next_m_indx)
                break
        indx+=1
        print(indx)
    print(months_range)
    mbym = []
    for i in range(len(months_range)):
        try:
            mbym.append(data_frame.iloc[months_range[i]:(months_range[i+1])])
        except IndexError:
            mbym.append(data_frame.iloc[months_range[i]:])
    print(mbym)'''