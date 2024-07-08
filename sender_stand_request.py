import requests
import configuration
def post_new_client_kit (kit_body, auth_token):
    return requests.post(configuration.URL_SERVICE + configuration.CREATE_PRODUCTS_KITS,
                         headers=auth_token,
                         json=kit_body)
