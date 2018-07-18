import pandas as pd
import matplotlib.pyplot as plt

from crycompare import *

coins = ['BTC','VTC','XMR','ZEC','NEO']

p = Price()
h = History()

df = pd.DataFrame({})
coinlist = p.coinList()
#coins = sorted(list( coinlist['Data'].keys() ))
for coin in coins:
    print('Coin: ', coin)
    tmp = h.histoDay(coin, 'USD', allData=True)

    if not tmp['Data']:
        print('Coin: ' + coin + ', No Data')
        continue

    tmp = pd.DataFrame(tmp['Data'])
    tmp['Coin'] = coin
    tmp['time'] = pd.to_datetime(tmp['time'], unit='s')
    tmp['Alogirthm'] = coinlist['Data'][coin]['Algorithm']
    tmp['FullyPremined'] = coinlist['Data'][coin]['FullyPremined']
    tmp['PreMinedValue'] = coinlist['Data'][coin]['PreMinedValue']
    tmp['ProofType'] = coinlist['Data'][coin]['ProofType']
    tmp['Sponsored'] = coinlist['Data'][coin]['Sponsored']
    tmp['TotalCoinSupply'] = coinlist['Data'][coin]['TotalCoinSupply']
    tmp['TotalCoinsFreeFloat'] = coinlist['Data'][coin]['TotalCoinsFreeFloat']

    df = df.append(tmp)

df.set_index(['Coin','time'], inplace=True)
df.to_csv('out.csv')


