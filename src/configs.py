from collections import defaultdict
import json

APP_NAME = "MyNewApp"
PRIMARY_COLOR = "#068D9D"
SECONDARY_COLOR = "#53599A"
TERTIARY_COLOR = "#607BB0"
QUATERNARY_COLOR = "#77BECF"
QUINARY_COLOR = "#AEECEF"

COLORS = ["#068D9D", "#53599A", "#607BB0", "#6D9DC5", "#77BECF", "#80DED9", "#AEECEF"]
GRAPH_CONFIG = {
    "displayModeBar": False,
    "responsive": True,
    "displaylogo": False,
    "editable": True,
}
PLOTLY_TEMPLATE = "plotly_white"

class KeyDefaultDict(defaultdict): # pragma: no cover
    def __missing__(self, key):
        return key
    
de_dict = KeyDefaultDict(lambda key: key)
de_dict.update(
    json.load(open("src/assets/locales/de.json"))
)
en_dict = KeyDefaultDict(lambda key: key)
TRANSLATE = {
    "de": de_dict,
    "en": en_dict
}
class AgGridConfigs():
    """
    Common configurations for ag-Grid
    """
    COLUMN_TYPES = {
        "longTextColumn": {
            "filter": "agTextColumnFilter",
            "cellStyle": {'textOverflow': 'ellipsis', 'whiteSpace': 'nowrap', 'overflow': 'hidden', 'padding': 0}
            },
        "formattedNumberColumn": {
            "valueFormatter": {"function": "d3.format(',.1f')(params.value)"},
            "filter": "agNumberColumnFilter",
            
        }
    }


def setup():
    from logging.config import fileConfig
    import plotly.io as pio
    from pathlib import Path
    import dash
    pio.templates.default = PLOTLY_TEMPLATE
    dash._dash_renderer._set_react_version('18.2.0')  # for DMC
    Path("logs").mkdir(parents=True, exist_ok=True)
    fileConfig('logging.conf')