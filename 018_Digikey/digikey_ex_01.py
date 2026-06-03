import os
import digikey
from digikey.v3.productinformation import KeywordSearchRequest
from parse import *

import logging

logger = logging.getLogger(__name__)
logger.setLevel(logging.DEBUG)

digikey_logger = logging.getLogger('digikey')
digikey_logger.setLevel(logging.DEBUG)

handler = logging.StreamHandler()
handler.setLevel(logging.DEBUG)
logger.addHandler(handler)
digikey_logger.addHandler(handler)

os.environ['DIGIKEY_CLIENT_ID'] = '***'
os.environ['DIGIKEY_CLIENT_SECRET'] = '****'
os.environ['DIGIKEY_CLIENT_SANDBOX'] = 'False'
os.environ['DIGIKEY_STORAGE_PATH'] = 'D://Works//PycharmProjects//001_TRAINING//018_Digikey//'

# Product Information
# digikey.keword_search()
# digikey.product_details()
# digikey.digi_reel_pricing()
# digikey.suggested_parts()
# digikey.manufacturer_product_details()

# Batch Product Details
#  digikey.batch_product_details()

# Order Support
# digikey.salesorder_history()
# digikey.status_salesorder_id()

# 1일 1,000회 조회 가능, 추가 시 Digikey 승인 필요
# API Limits
# api_limit = {'api_requests_limit': 1000,
#              'api_requests_remaining': 139}
# search_request = KeywordSearchRequest(keywords='CRCW080510K0FKEA', record_count=10)
# result = digikey.keyword_search(body=search_request, api_limits=api_limit)


# Query product number
dkpn = '296-6501-1-ND'
part = digikey.product_details(dkpn)
# print(part)
# print(type(part))
print(part.digi_key_part_number)
print(part.manufacturer.value)

# Search for parts
#search_request = KeywordSearchRequest(keywords='CRCW080510K0FKEA', record_count=10)
#print(type(search_request))
#print(search_request)

#result = digikey.keyword_search(body=search_request)
#print(result)

