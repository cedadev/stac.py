import pytest
from stac.stac import STAC
import warnings
import requests

url = "https://stac-elasticsearch-master.130.246.131.9.nip.io"
service = STAC(url=url,
               verify=False)
warnings.simplefilter('ignore')


def test_get_collections():
    collections = service.collections
    collections = list(collections.values())

    response = requests.get(url=f"{url}/collections", verify=False)
    response = response.json()
    response_collections = response.get('collections')

    assert collections == response_collections


def test_get_collection():
    collection = service.collection(collection_id="Fj3reHsBhuk7QqVbt7P-")

    response = requests.get(url=f"{url}/collections/Fj3reHsBhuk7QqVbt7P-", verify=False)
    response = response.json()

    assert collection == response


def test_get_itemcollection():
    collection = service.collection(collection_id="Fj3reHsBhuk7QqVbt7P-")
    items = collection.get_items()

    response = requests.get(url=f"{url}/collections/Fj3reHsBhuk7QqVbt7P-/items", verify=False)
    response = response.json()

    assert items == response


def test_get_item():
    collection = service.collection(collection_id="Fj3reHsBhuk7QqVbt7P-")
    item = collection.get_items(item_id="4f2e47fb4e0eb437bb5336bba1fc1c23")

    response = requests.get(f"{url}/collections/Fj3reHsBhuk7QqVbt7P-/items/4f2e47fb4e0eb437bb5336bba1fc1c23",
                            verify=False)
    response = response.json()

    assert item == response


def test_conformance_classes():
    conformance = service.conformance

    response = requests.get(f"{url}/conformance", verify=False)
    response = response.json()

    assert conformance == response
