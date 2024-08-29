from dash import clientside_callback, Output, Input

clientside_callback(
    """
    function change_lang(checked) {
        return `?lang=${checked ? 'de' : 'en'}`;
    }
    """,
    Output("url", "search"),
    Input("lang-toggle", "checked"),
)
