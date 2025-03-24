import dash

from dash import html, dcc

dash.register_page(__name__, path="/")

pageContent = open("page_content/home.md").read()

layout = html.Div([dcc.Markdown(pageContent)])
