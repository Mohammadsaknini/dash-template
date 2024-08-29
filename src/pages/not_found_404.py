from dash import html, register_page
from src.configs import TRANSLATE

register_page(__name__)

def layout(**kwargs):
    lang = kwargs.get("lang", "en")
    return html.Div([
        html.H1(TRANSLATE[lang]["A custom 404 page not found message"], className="text-danger"),
        html.Strong(TRANSLATE[lang]["The page you are looking for does not exist."]),
    ], className="text-center mt-5")