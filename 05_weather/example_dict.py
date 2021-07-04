#example dictionary
def main():
    d = {
        'city':'Portland',
        'state':'ME',
        'details':['Cold','Snowy','Winter']
    }
    # key = 'city'
    # print(f'the city is {d[key]}')
    # d['country'] = 'AU'
    # print(f"the city is {d.get('city','country')}")
    # print(d)
    # print(d.get('country'))

w = {
    "weather":{"description":"light rain","category":"Rain"},
    "wind":{"speed":8.05,"deg":30},
    "units":"imperial",
    "forecast":{
        "temp":48.99,
        "feels_like":45.52,
        "pressure":1010,
        "humidity":87,
        "low":48,
        "high":50
        },
    "location":{
        "city":"Charlottesville",
        "state":'VA',
        "country":"US"
        },
    "rate_limiting":{
        "unique_lookups_remaining":49,
        "lookup_reset_window":"1 hour"
    }}
print(f"the temperature in {w.get('location').get('city')} is:",w.get('forecast').get('temp'),"F")


if __name__ == '__main__':
    main()
