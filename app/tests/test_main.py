def test_read_hello_world(client):
    response = client.get("/hello_world")
    assert response.status_code == 200
    data = response.json()
    assert data["text"] == "Hello Test World"
