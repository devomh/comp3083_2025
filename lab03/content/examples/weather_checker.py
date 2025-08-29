import requests
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
    # SECURE METHOD: Use environment variables for API keys
    import os
    api_key = os.getenv('WEATHER_API_KEY')
    
    # Check if API key is set
    if not api_key:
        print("❌ Error: API key not found!")
        print("Please set your API key as an environment variable:")
        print("  Windows: set WEATHER_API_KEY=your-actual-key-here")
        print("  Mac/Linux: export WEATHER_API_KEY=your-actual-key-here")
        print("Then restart this program.")
        return
    
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
            description = weather_data['weather'][0]['description']
            feels_like = weather_data['main']['feels_like']
            
            print(f"\nWeather in {city}:")
            print(f"Temperature: {temp}°C (feels like {feels_like}°C)")
            print(f"Conditions: {description.title()}")
            
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
