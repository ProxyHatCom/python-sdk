import pytest
import respx

from proxyhat import AsyncProxyHat, ProxyHat

BASE_URL = "https://api.proxyhat.com/v1"


@pytest.fixture
def client():
    c = ProxyHat(api_key="ph_test_key", base_url=BASE_URL)
    yield c
    c.close()


@pytest.fixture
def async_client():
    return AsyncProxyHat(api_key="ph_test_key", base_url=BASE_URL)


@pytest.fixture
def mock_api():
    with respx.mock(base_url=BASE_URL) as respx_mock:
        yield respx_mock
