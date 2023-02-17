import requests

from flask import current_app

from hometap_interview.exceptions import NotFoundException
from hometap_interview.models.house_canary import PropertyDetail


class HouseCanaryClient:
    def __init__(self) -> None:
        """
        API client for interfacing with the HouseCanary API.  The HouseCanary API uses
        basic auth for authentication, all requests will use the API Key and Secret.
        """
        # Pull the various bits of information from the loaded app config
        self.api_key = current_app.config.get('HOUSE_CANARY_API_KEY')
        self.api_secret = current_app.config.get('HOUSE_CANARY_API_SECRET')
        self.base_url = current_app.config.get('HOUSE_CANARY_URL')
        self.mock_endpoint = current_app.config.get('MOCK_CANARY_ENDPOINT', None)

    def _get(self, endpoint: str, **params: str) -> requests.Response:
        """
        Handle Get requests to the given endpoint.

        :param endpoint: The endpoint to call
        :type endpoint: str
        :return: Returns the Response object from the reqests get call
        :rtype: requests.Response
        """
        # For the purposes of this inteview, I have a mock endpoint setup at mocky.io, if it's configured in the app
        # config just use that raw endpoint, otherwise the code is written to interface directly with the
        # House Canary API
        if self.mock_endpoint:
            current_app.logger.info('Using the mock endpoint to return property details')
            return requests.get(self.mock_endpoint)
        else:
            return requests.get(f"{self.base_url}/{endpoint}", params=params, auth=(self.api_key, self.api_secret))

    def get_property_details(self, address: str, zipcode: str) -> dict:
        """
        Fetch the property details from the HouseCanary API

        :param address: The address of the property to retreive the details for
        :type address: str
        :param zipcode: The zipcode for the property to retreive the details for
        :type zipcode: str
        :return: The raw dict response from the HouseCanary property/details endpoint
        :rtype: dict
        """
        # Only handling 200 and 404 for this exercise, this would also handle
        # other types of status codes like 401, 429, 500, etc that were applicable
        response = self._get('property/details', address=address, zipcode=zipcode)
        if response.status_code == 200:
            result = response.json()['property/details']['result']
            
            # TODO, not handling any validation errors for this case, but that would
            # need to be added and handled properly
            return PropertyDetail.parse_obj(result).dict()
        elif response.status_code == 404:
            raise NotFoundException(f"The property at {address} {zipcode} could not be found")