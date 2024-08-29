from dash import html, register_page
import dash_bootstrap_components as dbc
from src.configs import APP_NAME, TRANSLATE
from lorem import text, paragraph, sentence

register_page(
    __name__,
    path="/",
    name=f"{APP_NAME}",
)


def layout(**kwargs): # pragma: no cover
    lang = kwargs.get("lang", "en")
    kwargs.pop("lang", None)
    home_section = html.Section(
        [
            html.Div(className="image-container",
                     style={"background-image": "url(https://picsum.photos/2000/2000)"}),
            html.Div(
                [
                    html.H1(APP_NAME),
                    html.Span(
                        [html.P(sentence() + " " + sentence() , className="mb-0"),
                         html.P(sentence())],
                        className="mt-4",
                    ),
                    html.Div(
                        [
                            dbc.Button(
                                TRANSLATE[lang]["Get Started"], color="primary", href="/register"
                            ),
                            dbc.Button(TRANSLATE[lang]["Learn More"], color="primary",
                                       href="/services"),
                        ],
                        className="d-flex gap-2",
                    ),
                ],
                className="home-content section-bg",
            ),
        ],
        className="home-section position-relative", id="home",
    )
    
    services_section = html.Section(
        className="section-content bg-light light",
        children=[
            html.Div(
                [
                    html.Div(
                        "Services",
                        className="section-title",
                    ),
                    html.Article(
                        [
                            html.A(
                                html.Img(
                                    src="https://picsum.photos/1000/1000",
                                    alt="Image Title",
                                    className="postcard-img",
                                ),
                                className="postcard-img-link",
                                href="#",
                            ),
                            html.Div(
                                [
                                    html.H1(
                                        html.A(TRANSLATE[lang]["Service"] + " 1", href="#"),
                                        className="postcard-title blue",
                                    ),
                                    html.Div("", className="postcard-bar"),
                                    html.Div(
                                        paragraph(),
                                        className="postcard-preview-txt",
                                    ),

                                    html.Ul(
                                        [
                                            html.Li(
                                                [
                                                    html.I(
                                                        className="fas fa-screwdriver-wrench mr-2"
                                                    ),
                                                    TRANSLATE[lang]["Feature"] + " 1",
                                                ],
                                                className="tag-item",
                                            ),
                                            html.Li(
                                                [
                                                    html.I(
                                                        className="fas fa-truck-moving mr-2"
                                                    ),
                                                    TRANSLATE[lang]["Feature"] + " 2",
                                                ],
                                                className="tag-item",
                                            ),
                                            html.Li(
                                                [
                                                    html.I(
                                                        className="fas fa-tachometer-alt mr-2"
                                                    ),
                                                    TRANSLATE[lang]["Feature"] + " 3",
                                                ],
                                                className="tag-item",
                                            ),
                                        ],
                                        className="postcard-tagbox",
                                    ),

                                ],
                                className="postcard-text t-dark",
                            ),
                        ],
                        className="postcard light blue",
                    ),
                    html.Article(
                        [
                            html.A(
                                html.Img(
                                    src="https://picsum.photos/1000/1000",
                                    alt="Image Title",
                                    className="postcard-img",
                                ),
                                className="postcard-img-link",
                                href="#",
                            ),
                            html.Div(
                                [
                                    html.H1(
                                        html.A(TRANSLATE[lang]["Service"] + " 2", href="#"),
                                        className="postcard-title green",
                                    ),
                                    html.Div("", className="postcard-bar"),
                                    html.Div(
                                        paragraph(),
                                        className="postcard-preview-txt",
                                    ),
                                    html.Ul(
                                        [
                                            html.Li(
                                                [
                                                    html.I(
                                                        className="fas fa-clock mr-2"
                                                    ),
                                                    TRANSLATE[lang]["Feature"] + " 1",
                                                ],
                                                className="tag-item",
                                            ),
                                            html.Li(
                                                [
                                                    html.I(
                                                        className="fas fa-calendar-alt mr-2"
                                                    ),
                                                    TRANSLATE[lang]["Feature"] + " 2",
                                                ],
                                                className="tag-item",
                                            ),
                                            html.Li(
                                                [
                                                    html.I(
                                                        className="fas fa-user-clock mr-2"
                                                    ),
                                                    TRANSLATE[lang]["Feature"] + " 3",
                                                ],
                                                className="tag-item",
                                            ),
                                        ],
                                        className="postcard-tagbox",
                                    ),
                                ],
                                className="postcard-text t-dark",
                            ),
                        ],
                        className="postcard light green",
                    ),
                    html.Article(
                        [
                            html.A(
                                html.Img(
                                    src="https://picsum.photos/1000/1000",
                                    alt="Image Title",
                                    className="postcard-img",
                                ),
                                className="postcard-img-link",
                                href="#",
                            ),
                            html.Div(
                                [
                                    html.H1(
                                        html.A(TRANSLATE[lang]["Service"] + " 3", href="#"),
                                        className="postcard-title orange",
                                    ),
                                    html.Div("", className="postcard-bar"),
                                    html.Div(
                                        paragraph(),
                                        className="postcard-preview-txt",
                                    ),
                                    html.Ul(
                                        [
                                            html.Li(
                                                [
                                                    html.I(
                                                        className="fas fa-file-invoice-dollar mr-2"
                                                    ),
                                                    TRANSLATE[lang]["Feature"] + " 1",
                                                ],
                                                className="tag-item",
                                            ),
                                            html.Li(
                                                [
                                                    html.I(
                                                        className="fas fa-chart-line mr-2"
                                                    ),
                                                    TRANSLATE[lang]["Feature"] + " 2",
                                                ],
                                                className="tag-item",
                                            ),
                                            html.Li(
                                                [
                                                    html.I(
                                                        className="fas fa-money-check-alt mr-2"
                                                    ),
                                                    TRANSLATE[lang]["Feature"] + " 3",
                                                ],
                                                className="tag-item",
                                            ),
                                        ],
                                        className="postcard-tagbox",
                                    ),
                                ],
                                className="postcard-text t-dark",
                            ),
                        ],
                        className="postcard light orange",
                    ),
                ],
                className="services-content section-bg p-5",
                id="services",
            )
        ],
    )
    pricing_section = html.Section(
        className="pricing-section section-padding",
        children=[
            html.Div(
                [
                    html.H1("Pricing Plan",
                            className="section-title text-center mb-5"),
                    html.Div(
                        [
                            html.Div(
                                [
                                    html.Div(
                                        [
                                            html.Div(
                                                [
                                                    html.H2(
                                                        "Start up",
                                                        className="price-head text-center",
                                                    ),
                                                    *[
                                                        html.Span(
                                                            "", className="price")
                                                        for _ in range(6)
                                                    ],
                                                ],
                                                className="price-head",
                                            ),
                                            html.H1(
                                                "$29", className="price text-center"
                                            ),
                                            html.H5(
                                                "Monthly", className="text-center"),
                                            html.Div([

                                                html.Ul(
                                                    [
                                                        html.Li(
                                                            "Item 1"),
                                                        html.Li(
                                                            "Item 2"),
                                                        html.Li(
                                                            "Item 3"),
                                                        html.Li(
                                                            "Item 4"),
                                                        html.Li(
                                                            "Item 5"),
                                                    ],
                                                    className="text-start"),
                                            ], className="d-flex justify-content-center"),
                                            dbc.Button(
                                                "Get start",
                                                href="/register",
                                                className="text-center",
                                            ),
                                        ],
                                        className="single-pricing",
                                    ),
                                ],
                                className="col-lg-4 col-sm-4 col-xs-12  fadeInUp",
                            ),
                            html.Div(
                                [
                                    html.Div(
                                        [
                                            html.Div(
                                                [
                                                    html.H2(
                                                        "Medium",
                                                        className="price-head text-center",
                                                    ),
                                                    *[
                                                        html.Span(
                                                            "", className="price")
                                                        for _ in range(6)
                                                    ],
                                                ],
                                                className="price-head",
                                            ),
                                            html.H1(
                                                "$49", className="price text-center"
                                            ),
                                            html.H5(
                                                "Monthly", className="text-center"),
                                            html.Div([

                                                html.Ul(
                                                    [
                                                        html.Li(
                                                            "Item 1"),
                                                        html.Li(
                                                            "Item 2"),
                                                        html.Li(
                                                            "Item 3"),
                                                        html.Li(
                                                            "Item 4"),
                                                        html.Li(
                                                            "Item 5"),
                                                    ],
                                                    className="text-start"),
                                            ], className="d-flex justify-content-center"),
                                            dbc.Button(
                                                "Get start",
                                                href="/register",
                                                className="text-center",
                                            ),
                                        ],
                                        className="single-pricing",
                                    ),
                                ],
                                className="col-lg-4 col-sm-4 col-xs-12 fadeInUp",
                            ),
                            html.Div(
                                [
                                    html.Div(
                                        [
                                            html.Div(
                                                [
                                                    html.H2(
                                                        "Large",
                                                        className="price-head text-center",
                                                    ),
                                                    *[
                                                        html.Span(
                                                            "", className="price")
                                                        for _ in range(6)
                                                    ],
                                                ],
                                                className="price-head",
                                            ),
                                            html.Span(
                                                "Best", className="price-label"),
                                            html.H1(
                                                "$99", className="price text-center"
                                            ),
                                            html.H5(
                                                "Monthly", className="text-center"),
                                            html.Div([

                                                html.Ul(
                                                    [
                                                        html.Li(
                                                            "Item 1"),
                                                        html.Li(
                                                            "Item 2"),
                                                        html.Li(
                                                            "Item 3"),
                                                        html.Li(
                                                            "Item 4"),
                                                        html.Li(
                                                            "Item 5"),
                                                        html.Li(
                                                            "Item 6"),
                                                    ],
                                                    className="text-start"),
                                            ], className="d-flex justify-content-center"),

                                            dbc.Button(
                                                "Get start",
                                                href="/register",
                                                className="text-center text-white",
                                            ),
                                        ],
                                        className="single-pricing single-pricing-white",
                                    ),
                                ],
                                className="col-lg-4 col-sm-4 col-xs-12 fadeInUp",
                            ),
                        ],
                        className="row text-center",
                    ),
                ],
                className="container",
            ),
        ],
        id="pricing",
    )
    return html.Div(
        [
            home_section,
            services_section,
            pricing_section,
        ], className="content-wrapper")
