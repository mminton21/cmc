from requests import Request, Session
from requests.exceptions import ConnectionError, Timeout, TooManyRedirects
import json
import sys

url = ' https://pro-api.coinmarketcap.com/v1/cryptocurrency/map'
parameters = {
  'symbol': sys.argv[1]
}
headers = {
  'Accepts': 'application/json',
  'X-CMC_PRO_API_KEY': 'fb393c3b-8ac9-49ce-8f8d-022203ac355b',
}

session = Session()
session.headers.update(headers)

try:
  response = session.get(url, params=parameters)
  data = json.loads(response.text)
  print(data)
except (ConnectionError, Timeout, TooManyRedirects) as e:
  print(e)