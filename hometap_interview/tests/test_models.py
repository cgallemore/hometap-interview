from hometap_interview.models.house_canary import PropertyDetail

def test_property_model(house_canary_response):
    data = house_canary_response['property/details']['result']
    property = PropertyDetail.parse_obj(data)
    assert property.dict()['property']['sewer'] == 'municipal'
