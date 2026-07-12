from app.fireworks.client import FireworksClient


def test_client():

    client = FireworksClient()

    assert client.base_url.startswith("https://")