from app import app

def test_add():
    client = app.test_client()
    response = client.get('/add?a=2&b=3')
    assert response.json['result'] == 5.0

def test_subtract():
    client = app.test_client()
    response = client.get('/subtract?a=5&b=3')
    assert response.json['result'] == 2.0

def test_multiply():
    client = app.test_client()
    response = client.get('/multiply?a=4&b=3')
    assert response.json['result'] == 12.0

def test_divide():
    client = app.test_client()
    response = client.get('/divide?a=10&b=2')
    assert response.json['result'] == 5.0

def test_divide_by_zero():
    client = app.test_client()
    response = client.get('/divide?a=10&b=0')
    assert response.status_code == 400
