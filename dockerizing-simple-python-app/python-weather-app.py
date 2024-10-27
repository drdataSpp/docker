# import the module
import python_weather

import asyncio

async def getweather(v_cityName):
    try:

    # declare the client. the measuring unit used defaults to the metric system (celcius, km/h, etc.)
        async with python_weather.Client(unit=python_weather.METRIC) as client:
        
        # fetch a weather forecast from a city
            weather = await client.get(str(v_cityName))
            print(f"{str(v_cityName)}'s current temperature is {str(weather.temperature)} degree (C).")

    except Exception as e:
        print(f"Sorry there was an issue, please check. {str(e)}")
    
if __name__ == '__main__': 
  get_user_val_city = input('Enter the city name to fetch its temperature: ') 
  asyncio.run(getweather(get_user_val_city))