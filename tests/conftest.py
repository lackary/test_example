import pytest
import os
from dotenv import load_dotenv

load_dotenv()

@pytest.fixture(scope="session")
def api_url():
    """
    Fixture to provide the base URL for the API.
    """
    api_url = os.getenv("API_URL")
    assert api_url is not None, "API_URL environment variable not set"
    return api_url

@pytest.fixture
def api_headers():
    """
    Fixture to provide the headers for the API requests.
    """
    access_key = os.getenv("UNSPLASH_ACCESS_KEY")
    assert access_key is not None, "UNSPLASH_ACCESS_KEY environment variable not set"
    return {
        "Authorization": f"Client-ID {access_key}"
    }

@pytest.fixture(scope="session")
def api_photos():
    """
    Fixture to provide the API endpoint for photos.
    """
    api_photos = os.getenv("API_PHOTOS")
    assert api_photos is not None, "API_PHOTOS environment variable not set"
    return api_photos

@pytest.fixture(scope="session")
def api_collections():
    """
    Fixture to provide the API endpoint for collections.
    """
    api_collections = os.getenv("API_COLLECTIONS")
    assert api_collections is not None, "API_COLLECTIONS environment variable not set"
    return api_collections
