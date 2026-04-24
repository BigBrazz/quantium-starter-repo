import pytest
from app import app

from dash.testing.application_runners import import_app


# Test 1: Header exists
def test_header(dash_duo):
    app = import_app("app")

    dash_duo.start_server(app)

    header = dash_duo.find_element("h1")
    assert "Pink Morsel Sales Dashboard" in header.text


# Test 2: Graph exists
def test_graph(dash_duo):
    app = import_app("app")

    dash_duo.start_server(app)

    graph = dash_duo.find_element("#sales-chart")
    assert graph is not None


# Test 3: Region picker exists
def test_region_picker(dash_duo):
    app = import_app("app")

    dash_duo.start_server(app)

    radio = dash_duo.find_element("#region-filter")
    assert radio is not None