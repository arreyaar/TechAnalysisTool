import dash
import dash_bootstrap_components as dbc
import dash_labs as dl
import dash_html_components as html

app = dash.Dash(
    __name__, plugins=[dl.plugins.pages], external_stylesheets=[dbc.themes.YETI]
)
#Deploy
server = app.server

#LOGO = 'https://raw.githubusercontent.com/vuthanhdatt/web-indicator/main/images/brand-img.png'

LOGO = 'https://raw.githubusercontent.com/arreyaar/TechAnalysisTool/main/brand-img.png'

# navbar = dbc.NavbarSimple(
    
#     dbc.Nav(
#         [
#             dbc.NavLink('Home', href='/'),
#             dbc.NavLink('Chart', href='/chart'),
#             dbc.NavLink('Blog', href='/blog')
            
#         ],
#     ),
#     brand="Indicator Bot",
#     dark=True,
#     brand_href= '/',
#     color="primary",
#     className="mb-2",
# )

navbar = dbc.Navbar(
    dbc.Container(
        [
            html.A(
                # Use row and col to control vertical alignment of logo / brand
                dbc.Row(
                    [
                        dbc.Col(html.Img(src=LOGO, height="30px")),
                        dbc.Col(dbc.NavbarBrand("Reasoning By Elimination", className="ms-2")),
                    ],
                    align="center",
                    className="g-0",
                ),
                #href="/",
                href="/chart",
                style={"textDecoration": "none"},
            ),
            dbc.Nav(
        [
            dbc.NavLink('Technical Analysis', href='/chart'),
            #dbc.NavLink('Chart', href='/chart'),
            dbc.NavLink('Hints/Tips', href='/blog')
            
        ],
    ),
        ]
    ),
    color="primary",
    dark=True,
)


app.layout = dbc.Container(
    [navbar, dl.plugins.page_container],
    fluid=True,
)

if __name__ == "__main__":
    app.run_server(debug=True)