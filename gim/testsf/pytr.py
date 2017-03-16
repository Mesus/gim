# from pytrends.request import TrendReq
#
google_username = "chopwind@gmail.com"
google_password = "Google1984"
# path = ""
# # connect to Google
# pytrend = TrendReq(google_username, google_password, custom_useragent='My Pytrends Script')
#
# trend_payload = {'q': 'Unmanned_ground_vehicle'}
# # toprelated
# toprelated = pytrend.related(trend_payload, related_type='top')
# print(toprelated)
# risingrelated = pytrend.related(trend_payload, related_type='rising')
# print(risingrelated)

# from urllib.parse import unquote
import requests

# company_code = '%2Fm%2F07gyp7'
# company_code_unquoted = unquote(company_code)
# search_params = {'gprop' : 'all' , 'q' : 'Unmanned_ground_vehicle'}
#
# root_url = 'https://www.google.co.jp/trends/explore'
# request_link = requests.get(root_url , params = search_params)
# company_spec_url = request_link.url

import pyGTrends as pyg
gt = pyg.pyGTrends(google_username,google_password)
gt._connect()
gt.download_report('Unmanned_ground_vehicle')