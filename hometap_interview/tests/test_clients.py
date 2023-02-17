import pytest

from hometap_interview.clients.house_canary import HouseCanaryClient, NotFoundException

ENDPOINT_TO_MOCK = 'http://mock_canary.com/v3/property/details?address=123+Main+St&zipcode=55555'

def test_house_canary_get_property_details(app, requests_mock, house_canary_response):
    with app.app_context():
        api_client = HouseCanaryClient()
        requests_mock.get(ENDPOINT_TO_MOCK, json=house_canary_response)
        response = api_client.get_property_details('123 Main St', '55555')
        assert response['property']['sewer'] == 'municipal'


def test_house_canary_get_property_details_404(app, requests_mock, house_canary_response):
    with app.app_context():
        with pytest.raises(NotFoundException) as ex_info:
            api_client = HouseCanaryClient()
            requests_mock.get(ENDPOINT_TO_MOCK, json=house_canary_response, status_code=404)
            api_client.get_property_details('123 Main St', '55555')
            
        assert str(ex_info.value) == 'The property at 123 Main St 55555 could not be found'
            