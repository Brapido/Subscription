import requests
import json

from .models import Subscription

from django.conf import settings

def get_access_token():

    data = {'grant_type': 'client_credentials'}
    headers = {'Accept': 'application/json', 'Accept-Language': 'en_US'}
    client_id = settings.SS_CLIENT_ID
    secret_id = settings.SS_SECRET_ID
    # For live application delete 'sandbox' and replace client_id & secret_id for live variables
    url = 'https://api.sandbox.paypal.com/v1/oauth2/token'
    r = requests.post(url, auth=(client_id, secret_id), headers=headers, data=data).json()
    access_token = r['access_token']
    return access_token

def cancel_subscription_paypal(access_token, subID):

    bearer_token = 'Bearer ' + access_token
    headers = {
        'Content-Type': 'application/json',
        'Authorization': bearer_token,
    }

    # For live application delete 'sandbox' and replace client_id & secret_id for live variables
    url = 'https://api.sandbox.paypal.com/v1/billing/subscriptions/' + subID + '/cancel'
    r = requests.post(url, headers=headers)
    print(r.status_code)

def update_subscription_paypal(access_token, subID):

    bearer_token = 'Bearer ' + access_token
    headers = {
        'Content-Type': 'application/json',
        'Authorization': bearer_token,
    }

    # obtain current subscription plan for the user
    subDetails = Subscription.objects.get(paypal_subscription_id=subID)
    current_sub_plan = subDetails.subscription_plan
    if current_sub_plan == "Standard":
        new_sub_plan_id= 'P-4HF936665H352344KM35OBIY' # To Premium
    elif current_sub_plan == "Premium":
        new_sub_plan_id = 'P-6B3737358P965530NM4C46SA' # To Standard

    # For live application delete 'sandbox' and replace client_id & secret_id for live variables
    url = 'https://api.sandbox.paypal.com/v1/billing/subscriptions/' + subID + '/revise'

    revision_data = {
        "plan_id": new_sub_plan_id
    }

    # Make a POST request to PayPal's API for updating/revising a subscription
    r = requests.post(url, headers=headers, data=json.dumps(revision_data))

    # Output the response from PayPal to console.
    response_data = r.json()
    print(response_data)

    # loop through response data from Paypal to grab HATEOAS approval link
    for link in response_data.get('links', []):
        if link.get('rel') == 'approve':
            approve_link = link['href']

    # checking that original POST request was valid
    if r.status_code == 200:
        print("Request was a success")
        return approve_link
    else:
        print("Sorry, an error occured!")

def get_current_subscription(access_token, subID):

    bearer_token = 'Bearer ' + access_token
    headers = {
        'Content-Type': 'application/json',
        'Authorization': bearer_token,
    }

    # For live application delete 'sandbox' and replace client_id & secret_id for live variables
    url = f'https://api.sandbox.paypal.com/v1/billing/subscriptions/{subID}'
    r = requests.get(url, headers=headers)
    if r.status_code == 200:
        subscription_data = r.json()
        current_plan_id = subscription_data.get('plan_id')
        return current_plan_id
    else:
        print("Failed to retreive subsciption details")
        return None

    
    


    
    



