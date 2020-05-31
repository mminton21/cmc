from requests import Request, Session
from requests.exceptions import ConnectionError, Timeout, TooManyRedirects
import json
import sys

#fb393c3b-8ac9-49ce-8f8d-022203ac355b

url = ' https://pro-api.coinmarketcap.com/v1/cryptocurrency/map'
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
  print(data)
except (ConnectionError, Timeout, TooManyRedirects) as e:
  print(e)