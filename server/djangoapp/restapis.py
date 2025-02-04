import requests
import json

# import related models here
from .models import CarDealer
from requests.auth import HTTPBasicAuth
import logging
logger = logging.getLogger(__name__)

# Create a `get_request` to make HTTP GET requests
# e.g., response = requests.get(url, params=params, headers={'Content-Type': 'application/json'},
#                                     auth=HTTPBasicAuth('apikey', api_key))

def get_request(url, **kwargs):
    print(kwargs)
    print("GET from {} ".format(url))
    try:
        if 'api_key' in kwargs:
            # Basic authentication GET
            api_key= kwargs['api_key']
            kwargs.pop('api_key')
            response = requests.get(url, headers={'Content-Type': 'application/json'},
                                    params=kwargs,auth=HTTPBasicAuth('apikey', api_key))
        else:
            # no authentication GET
            response = requests.get(url, headers={'Content-Type': 'application/json'},
                                    params=kwargs)
            
            
    except:
        # If any error occurs
        print("Network exception occurred")

    status_code = response.status_code
    print("With status {} ".format(status_code))
    json_data = json.loads(response.text)
    print("With data {} ".format(json_data))

    return response.text
# Create a `post_request` to make HTTP POST requests
# e.g., response = requests.post(url, params=kwargs, json=payload)
def post_request(url, **kwargs):
    print(kwargs)
    print("POST from {} ".format(url))
    try:
        if ('api_key' in kwargs) and ('params' in kwargs):
            # Basic authentication POST
            api_key= kwargs['api_key']
            myobj=kwargs['params']
            kwargs.pop('api_key')
            response = requests.post(url, headers={'Content-Type': 'application/json'},
                                    json = myobj,auth=HTTPBasicAuth('apikey', api_key))
        else:
            # no authentication POST
            response = requests.post(url, headers={'Content-Type': 'application/json'},
                                    json=kwargs)
            
        
    except:
        # If any error occurs
        print("Not a valid request")

    status_code = response.status_code
    print("With status {} ".format(status_code))
    json_data = json.loads(response.text)
    print("With data {} ".format(json_data))
    return json_data

# Create a get_dealers_from_cf method to get dealers from a cloud function
# def get_dealers_from_cf(url, **kwargs):
# - Call get_request() with specified arguments
# - Parse JSON results into a CarDealer object list
def get_query_from_cf(url, **kwargs):
    results = []

    # Call get_request with a URL parameter
    json_result = format(get_request(url,**kwargs))
    if json_result:
        # Get the row list in JSON as dealers
        myresults = json_result
        # For each dealer object
        #for dealer in dealers:
            #print(dealer)
            # Get its content in `doc` object
            #dealer_doc = dealer['doc']
            # Create a CarDealer object with values in `doc` object
            #dealer_obj = CarDealer(address=dealer_doc["address"], city=dealer_doc["city"], full_name=dealer_doc["full_name"],
            #                       id=dealer_doc["id"], lat=dealer_doc["lat"], long=dealer_doc["long"],
            #                       short_name=dealer_doc["short_name"],
            #                       st=dealer_doc["st"], zip=dealer_doc["zip"])
            #results.append(dealer_obj)
            
            

    return myresults

# Create a get_dealer_reviews_from_cf method to get reviews by dealer id from a cloud function
# def get_dealer_by_id_from_cf(url, dealerId):
# - Call get_request() with specified arguments
# - Parse JSON results into a DealerView object list


# Create an `analyze_review_sentiments` method to call Watson NLU and analyze text
# def analyze_review_sentiments(text):
# - Call get_request() with specified arguments
# - Get the returned sentiment label such as Positive or Negative






