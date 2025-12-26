from dash import Dash, Output, Input, State, html
import dash_mantine_components as dmc
from requests_api import get_users, login, current_user
from schemas import Credentials
app = Dash()


app.layout = dmc.MantineProvider(
    theme={
        "fontFamily": "Montserrat, sans-serif",
        "defaultRadius": "md",
    },
    children=[
        dmc.Flex([
            dmc.Flex([
                dmc.Stack([
                 dmc.Title('Login', order=1),
                 dmc.Title('Acessar Conta', order=2),
                 html.Form([
                     dmc.TextInput(
                         # props as configured above:
                         placeholder="Your Email",
                         label="Email",
                         description="Enter your email as it appears on your card",
                         size="sm",
                         radius="sm",
                         variant="default",
                         required=True,
                         id="email"
                     ),
                     dmc.PasswordInput(
                         # props as configured above:
                         placeholder="Password",
                         label="Enter your password",
                         description="Password must include at least one letter, number and special character",
                         size="sm",
                         radius="sm",
                         variant="default",
                         required=True,
                         id="password"
                         # other props...
                     ),
                                    dmc.Button(
                    "Entrar",
                    id="login-btn"
                )

                 ], id="login-form"),

                 ], )

            ], direction='column', justify="center", align="center", gap="md", className="container-main"),
            dmc.Stack(
                [
                    dmc.Text(id="greeting-text", size=12),

                    dmc.Button("Clique aqui pra ver os usuarios",
                               id="triggered-users"),
                    dmc.Text(id="users-div", size=12)

                ], gap=25)

        ], direction='column', justify="center", align="center", className="whole"),

    ]
)


@app.callback(
    Output("greeting-text", "children"),
    Input("login-btn", "n_clicks"),
    State("email", "value"),
    State("password", "value")
)
def do_login(n_submit, email, password):
    print(email)
    print(password)
    
    token = login(email, password)
    
    current_user = current_user()
    
    return f"Olá {current_user['name']}"


@app.callback(
    Output("users-div", "children"),
    Input("triggered-users", "n_clicks")
)
def display_users(n_clicks):

    list_users = get_users(n_clicks)

    text = ""

    for user in list_users:
        text += f"{user["name"]}\n"

    return text


app.run()
