ENDPOINT_TO_MOCK = 'http://mock_canary.com/v3/property/details?address=123+Main+St&zipcode=55555'


def test_health_endpoint(client):
    response = client.get("/api/health")
    assert response.status_code == 200
    data = response.json
    assert data['status'] == 'UP'


def test_property_details(client, requests_mock, house_canary_response):
    requests_mock.get(ENDPOINT_TO_MOCK, json=house_canary_response)
    response = client.get("/api/property/details?address=123+Main+St&zipcode=55555")
    assert response.status_code == 200
    property_data = response.json['property/details']['result']['property']

    assert property_data['sewer'] == 'municipal'


def test_property_details_404(client, requests_mock):
    requests_mock.get(ENDPOINT_TO_MOCK, status_code=404)
    response = client.get("/api/property/details?address=123+Main+St&zipcode=55555")
    assert response.status_code == 404
    data = response.json
    assert data['message'] == 'The property at 123 Main St 55555 could not be found'


def test_property_details_missing_params(client):
    # Missing both address and zipcode
    response = client.get("/api/property/details")
    assert response.status_code == 400
    data = response.json
    assert data['message'] == 'The address and zipcode query paramters are required.'
    
    # Missing just zipcode
    response = client.get("/api/property/details?address=123+Main+St")
    assert response.status_code == 400
    data = response.json
    assert data['message'] == 'The address and zipcode query paramters are required.'

    # Missing just address
    response = client.get("/api/property/details?zipcode=55555")
    assert response.status_code == 400
    data = response.json
    assert data['message'] == 'The address and zipcode query paramters are required.'