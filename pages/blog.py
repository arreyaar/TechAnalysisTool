import dash
import dash_bootstrap_components as dbc
import dash_html_components as html

dash.register_page(__name__)




def layout():
    # ...
    return html.Div([
    dbc.Card(
    [
        dbc.CardBody(
           [
            html.H4("Details about the indicators and hints about the selected params like exchange/stocks/graphs", className="card-title"),
            html.P(
                'An easy way to determine which company match your indicator',
                className="card-text",
            ),
            dbc.Button("Read more", color="primary",href='/blogs/register')
        ]
        ),
        dbc.CardBody(
           [
            html.H4("Are tips fullproof?", className="card-title"),
            html.P(
                "Keep in mind that generating trading tips using technical indicators requires a sound strategy, risk management, and a thorough understanding of the markets. Additionally, it's crucial to stay informed about market news and events that can impact your trades. Trading is speculative and can lead to financial loss, so be cautious and consider seeking advice from financial professionals. "
                ,
                className="card-text",
            ),
            dbc.Button("Read more", color="primary",href='/blogs/rsi')
        ]
        )
    ],)
],className='blog')