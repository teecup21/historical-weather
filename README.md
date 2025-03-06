## Historical Weather App
The Historical Weather App is a Python-based application that allows users to explore and visualize historical weather data for Hong Kong. The app provides a graphical user interface (GUI) built with customtkinter and includes features such as data visualization, graphing, and interactive date selection.

Features
1. Historical Weather Data:
- View historical weather data for Hong Kong, including temperature, precipitation, wind speed, and humidity.
- Data is available for a 5-year period (2020–2025). This can be easily amended by altering data_retriever.py and making changes to the #year input "self.year_entry" 
  
2. Interactive GUI:
- Built with customtkinter for a modern and user-friendly interface.
- Users can select a specific date to view weather details.
  
3. Graphing:
- Visualize weather trends using Matplotlib.
- Create graphs for temperature, precipitation, wind speed, and humidity for selected dates.

3. Data Management:
- Data is stored in a JSON file (weather.json) and processed using Python dictionaries.

## Files
The project consists of the following files:
1. data_retriever.py:
- Runs an API call to the Open Meteo website to retrieve 5-year historical weather data for Hong Kong.
- Saves the data to weather.json.

2. weather.json:
- Contains the 5-year historical weather data for Hong Kong.
  
3. data_cleaner.py:
- Converts the JSON object into a Python dictionary.
- The keys are dates, and the values are dictionaries containing temperature, wind speed, humidity, and precipitation.

4. historical_weather_app.py:
- The main application file.
- Implements the GUI using customtkinter.
- Allows users to select dates, view weather data, and generate graphs.

## Requirements
To run the Historical Weather App, you need the following Python packages:
- customtkinter (for the GUI)
- matplotlib (for graphing)
- requests (for API calls in data_retriever.py)
- datetime (for handling dates)
