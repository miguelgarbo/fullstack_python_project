from dash import Dash
import dash_mantine_components as dmc

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

                 dmc.TextInput(
                     # props as configured above:
                     placeholder="Your Email",
                     label="Email",
                     description="Enter your email as it appears on your card",
                     size="sm",
                     radius="sm",
                     variant="default",
                     required=True,
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
                     # other props...
                 )
                 ])

            ], direction='column', justify="center", align="center", gap="md", className="container-main")
        ], direction='column', justify="center", align="center", className="whole"),

    ]
)

app.run()
