from src.components import NamedComponent
import dash_bootstrap_components as dbc
from dash import dcc, register_page
from src.configs import APP_NAME, TRANSLATE, GRAPH_CONFIG
from src.pages.svm_page import callbacks # This is needed to register the callbacks

register_page(
    __name__,
    path="/svm",
    name=f"{APP_NAME}",
)

# inspired by https://dash.gallery/dash-svm/
def layout(**kwargs):
    lang = kwargs.get("lang", "en")  # for translation
    return dbc.Container(
        [
            dbc.Row(
                [
                    dbc.Col(
                        [
                            NamedComponent(
                                dcc.Dropdown(
                                    id="svm-dataset",
                                    options=[
                                        {"label": TRANSLATE[lang]["moons"], "value": "moons"},
                                        {"label": TRANSLATE[lang]["circles"], "value": "circles"},
                                        {
                                            "label": TRANSLATE[lang]["linear_separable"],
                                            "value": "linear",
                                        },
                                    ],
                                    value="moons",
                                    clearable=False,
                                ),
                                name=TRANSLATE[lang]["Select Dataset"],
                            className="mt-3"),
                            NamedComponent(
                                dcc.Dropdown(
                                    id="svm-kernel",
                                    options=[
                                        {"label": "RBF", "value": "rbf"},
                                        {"label": "Linear", "value": "linear"},
                                        {"label": "Polynomial", "value": "poly"},
                                    ],
                                    value="rbf",
                                    clearable=False,
                                ),
                                name="Kernel",
                            className="mt-3"),
                            NamedComponent(
                                dcc.Slider(
                                    id="svm-n-samples",
                                    min=100,
                                    max=500,
                                    step=100,
                                    value=300,
                                    marks={i: str(i) for i in range(100, 501, 100)},
                                ),
                                name=TRANSLATE[lang]["Number of Samples"],
                            className="mt-3"),
                            NamedComponent(
                                dcc.Slider(
                                    id="svm-noise",
                                    min=0,
                                    max=1,
                                    step=0.1,
                                    value=0.8,
                                    marks={i: str(i) for i in [0, 0.2, 0.4, 0.6, 0.8, 1]},
                                ),
                                name=TRANSLATE[lang]["Noise Level"],
                            className="mt-3"),
                            NamedComponent(
                                dcc.Slider(
                                    id="svm-gamma",
                                    min=0.1,
                                    max=10,
                                    step=0.1,
                                    value=1,
                                    marks={i: str(i) for i in range(1, 11)},
                                ),
                                name="Gamma Coefficient",
                            className="mt-3"),
                            NamedComponent(
                                dcc.Slider(
                                    id="svm-c",
                                    min=0.1,
                                    max=10,
                                    step=0.1,
                                    value=1,
                                    marks={i: str(i) for i in range(1, 11)},
                                ),
                                name="C Coefficient",
                            className="mt-3"),
                            NamedComponent(
                                dcc.Slider(
                                    id="svm-degree",
                                    min=2,
                                    max=10,
                                    value=3,
                                    step=1,
                                    marks={
                                        str(i): str(i) for i in range(2, 11, 2)
                                    },
                                    disabled=True,
                                ),
                                name="Degree",
                            className="mt-3"),

                        ],
                        md=2,
                    ),
                    dbc.Col(
                        [
                            dcc.Graph(id="svm-plot", config=GRAPH_CONFIG),
                        ],
                        md=6,
                    ),
                    dbc.Col(
                        [
                            dcc.Graph(id="svm-roc", config=GRAPH_CONFIG),
                            dcc.Graph(id="svm-cm", config=GRAPH_CONFIG),
                        ],
                        md=4,
                    ),
                ]
            ),
        ], fluid=True, className="p-5"
    )