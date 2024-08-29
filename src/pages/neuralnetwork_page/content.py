from dash import dcc, register_page
from src.configs import APP_NAME, TRANSLATE, GRAPH_CONFIG
from src.pages.neuralnetwork_page import callbacks # This is needed to register the callbacks

register_page(
    __name__,
    path="/neural-network",
    name=f"{APP_NAME}",
)

def layout(**kwargs):
    pass