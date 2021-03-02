import json,requests,time
session = requests.session()
class monitor():
    def __init__(self):
        self.pricecheck1()
    def pricecheck1(self):
        priceHeaders = {
            'accept':'application/json'
        }
        priceUrl = 'https://api.coingecko.com/api/v3/coins/bitcoin?localization=true&tickers=false&market_data=true&community_data=false&developer_data=false&sparkline=false'
        priceGet = session.get(priceUrl,headers=priceHeaders)
        priceData = json.loads(priceGet.text)
        self.priceint1 = priceData['market_data']['current_price']['usd']
        stprice = str(self.priceint1)
        self.price1 = f'${stprice}'
        time.sleep(3)
        self.pricecheck2()
    def pricecheck2(self):
        priceHeaders = {
            'accept':'application/json'
        }
        priceUrl = 'https://api.coingecko.com/api/v3/coins/bitcoin?localization=true&tickers=false&market_data=true&community_data=false&developer_data=false&sparkline=false'
        priceGet = session.get(priceUrl,headers=priceHeaders)
        priceData = json.loads(priceGet.text)
        self.priceint2 = priceData['market_data']['current_price']['usd']
        stprice = str(self.priceint2)
        self.price2 = f'${stprice}'
        self.check()
    def check(self):
        difference = self.priceint2 - self.priceint1
        diff = str(difference)
        if self.priceint2 > self.priceint1:
            print(f'There was an increase of ${diff} in Bitcoin')
            self.pricecheck1()
        elif self.priceint2 == self.priceint1:
            print(f'There was no increase in Bitcoin')
            self.pricecheck1()
        elif self.priceint2 < self.priceint1:
            print(f'There was decrease of ${diff} in Bitcoin')
            self.pricecheck1()


monitor()