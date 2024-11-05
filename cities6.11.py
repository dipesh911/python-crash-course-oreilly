cities={
    'london':{
        'country':'UK',
        'population':'1.1M',
        'fact':''
    },
    'paris':{
         'country':'France',
        'population':'2M',
        'fact':''
    }
}
for city,city_info in cities.items():
    print(f"Info abount {city.title()}")
    country=city_info['country']
    population=city_info['population']
    print(f"It is in {country} and population is {population}")
