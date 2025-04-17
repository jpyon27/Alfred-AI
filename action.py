import python_weather
import asyncio
import assistant

def parse_cmd(cmd):
    if "weather" in cmd:
        weather_description = asyncio.run(get_weather("Atlanta"))
        query = "System information: " + str(weather_description)
        print(query)
        response = assistant.directive_to_memory(query)
        done = assistant.get_tts(response)
        
async def get_weather(city_name):
    async with python_weather.Client(unit=python_weather.IMPERIAL) as client:# put degree in f
        weather = await client.get(city_name)
        return weather