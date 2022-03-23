import pytest
from flask import url_for


@pytest.mark.api
def test_status_code_endpoint_api_convert_return_200(client):
    response = client.get(
        url_for("restapi.convertcrypt", token1="BTC", token2="USDT", amount="1")
    )
    assert response.status_code == 200


@pytest.mark.api
def test_status_code_endpoint_api_validtoken_return_200(client):
    response = client.get(url_for("restapi.validtoken", token="BTC"))
    assert response.status_code == 200


@pytest.mark.api
def test_status_code_endpoint_api_gettokensbycategory_return_200(client):
    response = client.get(url_for("restapi.gettokensbycategory", category="Metaverse"))
    assert response.status_code == 200


@pytest.mark.api
def test_status_code_parameter_not_exist_of_api_gettokensbycategory_return_404(
    client,
):
    response = client.get(url_for("restapi.gettokensbycategory", category="willfail"))
    assert response.status_code == 200
