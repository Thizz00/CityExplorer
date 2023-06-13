import dash
import dash_bootstrap_components as dbc
import dash_html_components as html
from dash.dependencies import Input, Output, State
from Api.country_info import CountryName
from Api.city_info import CityName
from Api.capital_info import CapitalInfo
from Api.weather_info import WeatherInfo
from Api.temperature_info import TemperatureInfo
from Api.population_info import PopulationInfo
from Api.map_generator import MapGenerator, MapCreator
import os
from dotenv import load_dotenv

app = dash.Dash(external_stylesheets=[dbc.themes.MINTY])

input_layout = dbc.Container(
    [
        html.Div(
            [
                dbc.Input(id="input-data", type="text", placeholder="Enter the city name in English"),
                dbc.Button("Search", id="push-button", className="mt-3 btn-lg", style={"width": "100px"}),
            ],
            className="text-center",
        ),
    ],
    className="mt-5",
)

app.layout = dbc.Container(
    [
        html.H1("CityExplorer Dashboard", className="text-center mt-4"),
        input_layout,
        dbc.Row(id="card-container", className="mt-4"),
    ]
)

@app.callback(
    Output("card-container", "children"),
    [Input("push-button", "n_clicks")],
    [State("input-data", "value")],
)
def show_cards(n_clicks, input_data):
    if n_clicks and input_data:
        try:
            load_dotenv()
            path = "city_explorer/maps/map.html"
            Adress = CountryName(input_data).get_address()
            city = CityName().get_city_name(input_data)
            is_capital = CapitalInfo().is_capital(input_data)
            weather_data = WeatherInfo(input_data).get_weather()
            temperature_data = TemperatureInfo(input_data).get_temperature()
            population = PopulationInfo().get_population(input_data)

            map_gen = MapGenerator(path)
            map_gen.create_map_html()
            if os.path.exists(path):
                map_creator = MapCreator(input_data)
                map_creator.get_coordinates()
                map_creator.create_map()
                map_creator.save_map(path)

            cards = []
            data = [
                ("Adress", Adress),
                ("City Name", city),
                ("Capital", is_capital),
                ("Weather", weather_data),
                ("Temperature", temperature_data),
                ("Population", population)
            ]

            for title, value in data:
                card = dbc.Col(
                    dbc.Card(
                        dbc.CardBody(
                            [
                                html.H5(title, className="card-title"),
                                html.P(str(value)),
                            ]
                        ),
                        className="mb-2 text-center",
                    ),
                    width=4,
                    style={"height": "150px", "border-radius": "10px"},
                )
                cards.append(card)
            map_html = html.Iframe(srcDoc=open(path, 'r').read(), width='100%', height='600')
            return dbc.Row(cards, justify="center"), map_html

        except Exception as e:
            error_message = html.H3("Błąd: " + str(e), style={"text-align": "center"})
            return error_message

