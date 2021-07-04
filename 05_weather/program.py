import collections
import requests

#create named tuples
Location = collections.namedtuple('Location','city state country')
Weather = collections.namedtuple('Weather','location units temp condition')

def main():
    show_header()
    location_text = input('Where do you want the weather report?  ')
    loc = convert_plaintext_location(location_text)
    if not loc:
        print (f'Could not find "{location_text}" ')
        return

    # city, state, country = loc
    # weather_api_data = call_weather_api(loc)

    weather = call_weather_api(loc)
    if not weather:
        print (f'Could not get the weather for "{location_text}" from the API')
        return

    report_weather(loc,weather)
    
def report_weather(loc,weather):
    location_name = get_location_name(loc)
    scale = get_scale(weather)
    print(f'The weather in {location_name} is {weather.temp} {scale} and {weather.condition}.')

def get_scale(weather):
    if weather.units == 'imperial':
        scale = "F"
    else: 
        scale = "C"
    return scale

def get_location_name(location):
    if not location.state:
        return f'{location.city.capitalize()}, {location.country.upper()}'
    else:
        return f'{location.city.capitalize()},{location.state.upper()},{location.country.upper()}'
    
def call_weather_api(loc):
    url = f"https://weather.talkpython.fm/api/weather?city={loc.city}&country={loc.country}&units=imperial"
    if loc.state:
        url += f"&state={loc.state}"

    resp = requests.get(url)
    if resp.status_code not in {200}:
        # print(f"Error:{resp.text}")
        # data = resp.json()
        # print(data)
        return None

    data = resp.json()

    return convert_api_to_weather(data, loc)

def convert_api_to_weather(data,loc):
    temp = data.get('forecast').get('temp')
    w = data.get('weather')
    condition = f"{w.get('category')}: {w.get('description').capitalize()}"
    weather = Weather(loc,data.get('units'), temp, condition)
    return weather
 
def convert_plaintext_location(location_text):
    #first, avoid processing if nothing entered
    if not location_text or not location_text.strip():
        return None
    
    #if something's been entered, first make it all lowercase and strip out spaces
    location_text = location_text.lower().strip()
    
    # we have three use cases: (1) just city; (2) city, country; (3) city, state, country
    # regardless, we have to split it up
    parts = location_text.split(',')
    
    city = ""
    state = ""
    country = "us"

    if len(parts) == 1:
        city = parts[0].strip()
    elif len(parts) == 2:
        city = parts[0].strip()
        country = parts[1].strip()
    elif len(parts) == 3:
        city = parts[0].strip()
        state = parts[1].strip()
        country = parts[2].strip()
    else:
        return None
    # we then return the tuple containing the three items
    # return city, state, country
    # t = Location(city, state, country)
    # t.city

    #alternately, we can use a Name Tuple from Collections:
    return Location(city,state,country)

    # # print(f"City={city}, State={state}, Country={country}")
    # return location_text

def show_header():
    print()
    print('----------------------------------')
    print('       WEATHER CLIENT             ')
    print('----------------------------------')
    print()

if __name__ == "__main__":
    main()
