# import requests  <- ERROR 1: The 'requests' library is not imported. The line 'response = requests.get(url)' will fail.
import json

def get_weather(city, api_key):
    """Get weather data for a specific city"""
    url = f"http://api.openweathermap.org/data/2.5/weather?q={city}&appid={api_key}&units=metric"
    
    try:
        response = requests.get(url)
        if response.status_code == 200:
            return response.json()
        else:
            return None
    except requests.RequestException:
        return None

def main():
    api_key = "YOUR_API_KEY_HERE"  # Students insert their key
    
    print("Weather Checker App")
    print("Enter 'exit' to quit")
    
    while True:
        city = input("\nEnter city name: ").strip()
        
        if city.lower() == 'exit':
            print("Thanks for using Weather Checker!")
            break
            
        weather_data = get_weather(city, api_key)
        
        if weather_data:
            temp = weather_data['main']['temp']
            # ERROR 2: This variable is named 'descrip', but the code later tries to use 'description'.
            descrip = weather_data['weather'][0]['description']
            feels_like = weather_data['main']['feels_like']
            
            print(f"\nWeather in {city}:")
            print(f"Temperature: {temp}°C (feels like {feels_like}°C)")
            print(f"Conditions: {description.title()}") # This line will fail!
            
            # Smart recommendations
            if 'rain' in description or 'drizzle' in description:
                print("💧 Recommendation: Take an umbrella!")
            elif 'snow' in description:
                print("❄️  Recommendation: Dress warmly and wear boots!")
            elif temp > 25:
                print("☀️  Recommendation: Perfect day for outdoor activities!")
        else:
            print(f"❌ Could not find weather data for '{city}'. Please check the city name.")

if __name__ == "__main__":
    main()
