import pytest


@pytest.mark.pages
def test_status_code_page_convert_return_200(client):
    response = client.get("/convert")
    assert response.status_code == 200


@pytest.mark.pages
def test_status_code_page_cryptogames_return_200(client):
    response = client.get("/cryptogames")
    assert response.status_code == 200


@pytest.mark.pages
def test_status_code_page_something_return_404(client):
    response = client.get("/something")
    assert response.status_code == 404
