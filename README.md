# cryCompare
Python wrapper for CryptoCompare public API (https://www.cryptocompare.com/api)
Project information https://pypi.org/project/crycompare/

Following API requests are supported:
- CoinList
- Price
- PriceMulti
- PriceMultiFull
- PriceHistorical
- generateAvg
- dayAvg
- CoinSnapshot
- CoinSnapshotFullById
- HistoMinute
- HistoHour
- HistoDay
- topPairs
- socialStats
- miningEquipment

Installation

```
pip install crycompare
```

Usage

```
from crycompare import price as p
print(p.coin_snapshot('btc', 'usd'))
```

price submodule: price, price_multi, price_multi_full, generate_avg, day_avg, price_historical, coin_snapshot, coin_snahpshot_id, top_pairs.
history submodule: histo_minute, histo_hour, histo_day.
social submodule: social_stats, mining_equipment

For detailed documentation visit CryptoCompare API website.
CryptoCompare API Documentation can be found at https://www.cryptocompare.com/api/#introduction
