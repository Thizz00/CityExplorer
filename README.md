
## About The Project

This is a project that uses the Dash framework in Python to create a web-based dashboard called "CityExplorer Dashboard". It imports various components and dependencies, including Bootstrap components, HTML components, and modules from different APIs.

The project allows users to enter a city name in English and search for information about that city. When the user clicks the "Search" button, a callback function is triggered. The function retrieves data from different APIs related to the entered city, such as country information, city name, capital status, weather information, temperature, and population.

The project also generates a map using the MapGenerator and MapCreator classes. The map is saved as an HTML file and displayed in an iframe on the dashboard. The retrieved data is displayed on the dashboard as well, with each piece of information shown in a separate card. The cards are dynamically generated based on the retrieved data.

If any errors occur during the process, an error message is displayed on the dashboard.

## Screenshots
### Main page
![Screenshots](/Demo/ss1.PNG?raw=true)
### Cards and map
![Screenshots](/Demo/ss2.PNG?raw=true)


## Project Structure
### The project consists of the following modules:

- AdressName class from the country_info module is responsible for fetching the adress information based on the city name.

- CityName class from the city_info module is responsible for fetching the city name based on the input data.

- CapitalInfo class from the capital_info module is responsible for determining if the input city is a capital city.

- WeatherInfo class from the weather_info module is responsible for fetching the weather information based on the input city.

- TemperatureInfo class from the temperature_info module is responsible for fetching the temperature information based on the input city.

- PopulationInfo class from the population_info module is responsible for fetching the population information based on the input city.

- MapCreator class from the map_generator module is responsible for creating a map using the input city's coordinates.


## Requirements
```
dash==2.10.2
dash_bootstrap_components==0.13.1
dash_html_components==2.0.0
folium==0.14.0
geopy==2.3.0
python-dotenv==1.0.0
Requests==2.31.0

```
## Add .env file
Create an .env file, to which add two variables API_SECRET and API_KEY. 

Create an account on https://api-ninjas.com and copy your API Key. 

Create an account on https://openweathermap.org and copy your API Key. 

To the API_SECRET variable, assign the API key from https://api-ninjas.com, and to the API_KEY variable, assign the API key from https://openweathermap.org.

## Run the app
* Terminal
    ```
  
    # requirements
    pip install -r requirements.txt
    python main.py


    # quit
    ctrl-c
    ```
* VSCode
  * Open the repo directory in VSCode: git clone https://github.com/Thizz00/CityExplorer.git
  * Open `main.py`
  * Start debugging with F5
  * Stop debugging with Shift-F5
