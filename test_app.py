# Test suite for the Dash app
from contextvars import copy_context
from dash._callback_context import context_value
from dash._utils import AttributeDict
from app import update_graph


def test_header_present():
    from app import app
    header = app.layout.children[0].children[0]
    assert "Pink Morsel" in header.children


def test_graph_present():
    from app import app
    from dash import dcc
    graph_div = app.layout.children[2]
    graph = graph_div.children[0]
    assert isinstance(graph, dcc.Graph)
    assert graph.id == 'morsel-sales-graph'

def test_region_picker_present():
    from app import app
    controls_div = app.layout.children[0]  
    from dash import dcc
    radio = None
    for child in app.layout.children:
        for item in (child.children if isinstance(child.children, list) else [child.children]):
            if isinstance(item, dcc.RadioItems):
                radio = item
    assert radio is not None
    assert radio.id == 'region-filter'
    assert len(radio.options) == 5


def test_all_regions_callback():
    fig = update_graph('all')
    assert fig is not None


def test_single_region_callback():
    fig = update_graph('north')
    assert fig is not None