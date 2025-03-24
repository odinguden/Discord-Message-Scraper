import dash
from dash import Dash, html, dcc

app = Dash(__name__, use_pages=True)


app.layout = html.Div(
    [
        html.Div(
            [
                html.H1(
                    "A tool for data visualization",
                    style={
                        "padding": "10px",
                    },
                ),
                html.Div(
                    [
                        html.Div(
                            dcc.Link(
                                f"{page['name']}",
                                href=page["relative_path"],
                                style={
                                    "padding": "10px",
                                    "margin-right": "15px",
                                    "position": "relative",
                                    "display": "block",
                                    "background-color": "grey",
                                    "color": "white",
                                    "border-radius": "5px",
                                    "justify-content": "space-between",
                                    "text-decoration": "none",
                                },
                            )
                        )
                        for page in dash.page_registry.values()
                    ],
                    style={
                        "display": "flex",
                        "align-items": "center",
                        "justify-content": "space-between",
                    },
                ),
            ],
            style={
                "display": "flex",
                "margin": "0px",
                "border-bottom": "1px solid black",
            },
        ),
        dash.page_container,
    ],
    style={
        "backgroundColor": "white",
        "color": "#000000",
    },
)

if __name__ == "__main__":
    app.run(
        debug=True,
        port=8050,  # For azure deployment
    )

