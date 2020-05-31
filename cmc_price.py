from requests import Request, Session
from requests.exceptions import ConnectionError, Timeout, TooManyRedirects
import json
import sys

#fb393c3b-8ac9-49ce-8f8d-022203ac355b

url = 'https://pro-api.coinmarketcap.com/v1/cryptocurrency/quotes/latest'
parameters = {
  'symbol': sys.argv[1]
}
headers = {
  'Accepts': 'application/json',
  'X-CMC_PRO_API_KEY': sys.argv[2]
}

session = Session()
session.headers.update(headers)

try:
  response = session.get(url, params=parameters)
  data = json.loads(response.text)
  cpath = data['data'][sys.argv[1]]['quote']['USD']
  price = cpath['price']
  price = (format(float(price), '.2f'))
  print(f'The price of {sys.argv[1]} is ${price}!')

  change_1 = float(format(float(cpath['percent_change_1h']), '.2f'))
  if change_1 > 0:
      print(f'The change in {sys.argv[1]} is up ${change_1} over the last hour.')
  elif change_1 < 0:
      print(f'The change in {sys.argv[1]} is down ${abs(change_1)} over the last hour.')
  else:
      print(f'The price of {sys.argv[1]} has not changed in the last hour.')

  change_24 = float(format(float(cpath['percent_change_24h']), '.2f'))
  if change_24 > 0:
      print(f'The change in {sys.argv[1]} is up ${change_24} over the last 24 hours.')
  elif change_24 < 0:
      print(f'The change in {sys.argv[1]} is down ${abs(change_24)} over the last 24 hours.')
  else:
      print(f'The price of {sys.argv[1]} has not changed in the last hour.')

except (ConnectionError, Timeout, TooManyRedirects) as e:
  print(e)