def test_request_example(client):
    response = client.get("/api/health/")
    assert response.status_code == 200
    data = response.json
    assert data['status'] == 'UP'
