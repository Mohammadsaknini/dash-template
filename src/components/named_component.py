from dash import html


class NamedComponent(html.Div):
    """
    A component that has a label and a child component. The label is displayed above the child component.
    """
    def __init__(self, children, name, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.children = [
            html.Label(f"{name}:", className="font-weight-bold mb-3"),
            children
        ]