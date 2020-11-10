import requests
import PySimpleGUI as sg

# OpenWeatherAPI key utilized to retrieve weather
key = 'a4833f37f86a1448f28b1d37fc7d6417'

# Using PySimpleGUI, define a GUI that has a text entry box for a zip code or city, a box for returning the weather, and two 
#buttons for entering input and canceling
layout = [[sg.Text('Enter a zip code or city name:')],
          [sg.Input(do_not_clear=False)],
          [sg.Button('Enter'), sg.Exit()],
          [sg.Output(size=(45, 20), key='output')]]
# Declare the GUI window with a title/header of 'Weather Forecast' and have it display the layout defined above
window = sg.Window('Weather Forecast', layout)


def printForecast(fc):
    """
    printForecast() prints out the contents of the json file returned from the weather API
    """
    print(f'City: {fc["name"]}\nCurrent Temperature: {fc["main"]["temp"]} *F\nLow/High {fc["main"]["temp_min"]}/{fc["main"]["temp_max"]} *F\nHumidity: {fc["main"]["humidity"]}%')
    print('-' * 78)


def retrieveWeather(input):
    """
    Using requests, retrieve the weather forecast from the weather API and return it as a json file
    :param input zip code or city name entered by the user
    :return json file of the forecast for that region
    """
    # If the input is all digits, it is a zip code and the 'zip=' identifier must be added to work with the weather API
    if str.isdigit(input):
        input = 'zip='+input
    else:  # Else, the input is a string or city name, meaning the 'q=' identifier must be added
        input = 'q='+input
    # Return the json file of the forecast from the weather API
    return requests.get('http://api.openweathermap.org/data/2.5/weather?'+input+'&APPID='+key+'&units=imperial').json()


def main():
    # While the program is running, continually check for user input and attempt to return the weather data for the
    # region the user enters
    while True:
        event, values = window.Read()
        if event is None or event == 'Exit':
            break
        try:  # Attempt to retrieve the weather and print out the result
            printForecast(retrieveWeather((values[0])))
        except:  # If an exception is thrown, print that the zip code was not found
            print('Error: Zip code or city not found')
    window.Close()


if __name__ == '__main__':
    main()
