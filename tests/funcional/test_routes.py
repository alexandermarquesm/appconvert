from flask import url_for
import pytest

def test_status_code_page_convert_return_200(client):
     response = client.get(url_for('webui.convert'))
     assert response.status_code == 200

def test_status_code_page_cryptogames_return_200(client):
    response = client.get(url_for('webui.cryptogames'))
    assert response.status_code == 200

def test_status_code_endpoint_api_convert_return_200(client):
     response = client.get(url_for('restapi.convertcrypt', token1='BTC', token2='USDT', amount='1'))
     assert response.status_code == 200

def test_status_code_endpoint_api_validtoken_return_200(client):
     response = client.get(url_for('restapi.validtoken', token='BTC'))
     assert response.status_code == 200

def test_status_code_endpoint_api_gettokensbycategory_return_200(client):
     response = client.get(url_for('restapi.gettokensbycategory', category='Metaverse'))
     assert response.status_code == 200

@pytest.mark.test
def test_if_debug_is_false(client):
     import ipdb; ipdb.set_trace()
