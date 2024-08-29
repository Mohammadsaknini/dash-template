from dash._utils import AttributeDict
from src.components import Navbar, Footer
from dash.exceptions import PreventUpdate
from app import display_page
import pytest

def test_display_page_callback_no_footer():
    """
    Test if the display_page callback returns the children if the path is not "/"
    """
    path = "/svm"
    children = [AttributeDict()]
    result = display_page(path, children)
    assert len(result) == 2
    assert not any(isinstance(child, Footer) for child in result)
    
def test_display_page_callback_footer():
    """
    Test if the display_page doesn't update the layout if the path is "/"
    """
    path = "/"
    children = [AttributeDict()]
    with pytest.raises(PreventUpdate):
        result = display_page(path, children)
        assert result == PreventUpdate