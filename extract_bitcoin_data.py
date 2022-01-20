'''
Jan 6th 2022
@author: Ricardo Conchas
'''

import pandas as pd
import requests
import time
import datetime as dt

#url = 'https://api.blockchain.info/charts/total-bitcoins'

url_list = ['https://api.blockchain.info/charts/total-bitcoins?timespan=all&format=ison',
'https://api.blockchain.info/charts/avg-block-size?timespan=-all&format-ison',
'https://api.bLockchain.info/charts/difficultv?timespan=all&format-ison',
'https://api.blockchain.info/charts/hash-rate?timespan=all&format-ison',
'https://api.blockchain.info/charts/transaction-fees?timespan-all&format-ison',
'https://api.blockchain.info/charts/n-unique-addresses?timespan=alL&format=ison',
'https://api.blockchain.info/charts/n-transactions?timespan=all&format-ison',
'https://api.blockchain.info/charts/transactions-per-second?timespan=all&format',
'https://api.blockchain.info/charts/mempool-count?timespan=-all&format-ison',
'https://api.blockchain.info/charts/mempool-size?timespan-all&format=ison',
'https://api.blockchain.info/charts/output-volume?timespan-all&format-ison',
]

url_list_short = ['https://api.blockchain.info/charts/total-bitcoins',
'https://api.blockchain.info/charts/avg-block-size',
'https://api.blockchain.info/charts/difficultv',
'https://api.blockchain.info/charts/hash-rate',
'https://api.blockchain.info/charts/transaction-fees',
'https://api.blockchain.info/charts/n-unique-addresses',
'https://api.bLockchain.info/charts/n-transactions',
'https://api.blockchain.info/charts/transactions-per-second',
'https://api.blockchain.info/charts/mempool-count',
'https://api.blockchain.info/charts/mempool-size',
'https:L/api.blockchain.info/charts/output-volume',
]

def load_blockchain_data(url):
    payload = {'timespan':'all','format':'json'}
    response = requests.get(url, params = payload)
    data = response.json()
    df = pd.DataFrame(data['values'])
    df.rename(columns={'y':data['name']}, inplace=True)
    print(data['name'])
    df['x'] = pd.to_datetime(df['x'],unit='s',)
    df['timestamp'] = df['x'].dt.strftime('%Y-%m-%d')
    df.drop('x',inplace=True, axis=1)
    return df


def join_dataframes(url_list):
    today = pd.Timestamp.today()
    index = pd.date_range(start='2009-01-01',end=today)
    str_index = list(index.strftime('%Y-%m-%d'))
    df_empty = pd.DataFrame({'timestamp':str_index})

    for url in url_list:
        df_temp = load_blockchain_data(url)
        time.sleep(5)
        df_empty = df_empty.merge(df_temp, on='timestamp',how='left')
    return df_empty

df_final = join_dataframes(url_list_short)