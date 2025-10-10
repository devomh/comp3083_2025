"""
Weather Checker - API Integration Capstone Project
Lab 05: JSON and APIs

This script demonstrates a complete API integration workflow:
1. Reading API keys from environment variables (security best practice)
2. Making HTTP requests to a real weather API
3. Parsing JSON responses
4. Error handling for network and API issues
5. Presenting data in a user-friendly format

Learning Objectives:
- Integrate all JSON skills (parsing, navigating nested structures)
- Make authenticated API requests
- Handle errors gracefully
- Build a complete interactive application

API Used: OpenWeatherMap (https://openweathermap.org/api)
"""

import requests
import json
import os


def get_weather(city, api_key):
    """
    Get current weather data for a specific city from OpenWeatherMap API.

    Args:
        city (str): City name (e.g., "Miami", "London", "Tokyo")
        api_key (str): Your OpenWeatherMap API key

    Returns:
        dict: Parsed JSON weather data, or None if request fails

    API Response Structure:
    {
      "name": "Miami",
      "main": {
        "temp": 25.5,
        "feels_like": 26.2,
        "humidity": 70,
        "pressure": 1013
      },
      "weather": [
        {
          "description": "scattered clouds",
          "main": "Clouds"
        }
      ],
      "wind": {
        "speed": 4.5
      }
    }
    """
    # TODO: Build the API URL
    # Base URL: http://api.openweathermap.org/data/2.5/weather
    # Query parameters:
    #   - q: city name
    #   - appid: your API key
    #   - units: "metric" (for Celsius)
    url = f"http://api.openweathermap.org/data/2.5/weather?q={city}&appid={api_key}&units=metric"

    try:
        # TODO: Make the GET request with a 5-second timeout
        response = requests.get(url, timeout=5)

        # TODO: Check status code
        if response.status_code == 200:
            # Success! Parse and return JSON
            return response.json()
        elif response.status_code == 404:
            # City not found
            print(f"❌ City '{city}' not found. Please check spelling.")
            return None
        elif response.status_code == 401:
            # Invalid API key
            print("❌ Invalid API key. Please check your credentials.")
            return None
        else:
            # Other error
            print(f"❌ API error: {response.status_code}")
            return None

    except requests.Timeout:
        print("❌ Request timed out. Check your internet connection.")
        return None
    except requests.ConnectionError:
        print("❌ Connection error. Check your internet connection.")
        return None
    except requests.RequestException as e:
        print(f"❌ Request error: {e}")
        return None
    except json.JSONDecodeError:
        print("❌ Invalid JSON response from API")
        return None


def format_weather_display(weather_data):
    """
    Format weather data for user-friendly display.

    Args:
        weather_data (dict): Parsed JSON from OpenWeatherMap API

    Returns:
        str: Formatted weather report
    """
    # TODO: Extract data from nested JSON structure
    # Hint: Review Module 3 - Nested Data Navigation

    city = weather_data.get('name', 'Unknown')

    # Temperature data (nested in 'main' object)
    main = weather_data.get('main', {})
    temp = main.get('temp', 'N/A')
    feels_like = main.get('feels_like', 'N/A')
    humidity = main.get('humidity', 'N/A')

    # Weather description (nested in 'weather' array)
    weather = weather_data.get('weather', [])
    description = weather[0].get('description', 'N/A') if weather else 'N/A'

    # Wind data (nested in 'wind' object)
    wind = weather_data.get('wind', {})
    wind_speed = wind.get('speed', 'N/A')

    # TODO: Build formatted string
    report = f"""
╔══════════════════════════════════════════
║ Weather in {city.title()}
╠══════════════════════════════════════════
║ 🌡️  Temperature: {temp}°C (feels like {feels_like}°C)
║ ☁️  Conditions:  {description.title()}
║ 💧 Humidity:    {humidity}%
║ 💨 Wind Speed:  {wind_speed} m/s
╚══════════════════════════════════════════
"""
    return report


def get_weather_recommendation(weather_data):
    """
    Provide smart recommendations based on weather conditions.

    Args:
        weather_data (dict): Parsed JSON from OpenWeatherMap API

    Returns:
        str: Recommendation message
    """
    # TODO: Extract necessary data
    main = weather_data.get('main', {})
    temp = main.get('temp', 20)

    weather = weather_data.get('weather', [])
    description = weather[0].get('description', '').lower() if weather else ''

    # TODO: Generate recommendations based on conditions
    recommendations = []

    if 'rain' in description or 'drizzle' in description:
        recommendations.append("💧 Don't forget your umbrella!")

    if 'snow' in description:
        recommendations.append("❄️  Dress warmly and wear boots!")

    if 'thunder' in description or 'storm' in description:
        recommendations.append("⚡ Stay indoors if possible!")

    if temp > 30:
        recommendations.append("🌡️  Very hot! Stay hydrated and seek shade.")
    elif temp > 25:
        recommendations.append("☀️  Great day for outdoor activities!")
    elif temp < 5:
        recommendations.append("🥶 Bundle up! It's freezing!")
    elif temp < 15:
        recommendations.append("🧥 Bring a jacket!")

    if main.get('humidity', 0) > 80:
        recommendations.append("💦 High humidity - might feel muggy!")

    if len(recommendations) > 0:
        return "📋 Recommendations:\n   " + "\n   ".join(recommendations)
    else:
        return "📋 Recommendation: Enjoy your day!"


def save_weather_history(city, weather_data, filename="weather_history.json"):
    """
    Save weather query to a local JSON file for history tracking.

    This demonstrates JSON file persistence from Module 2.

    Args:
        city (str): City name
        weather_data (dict): Weather data from API
        filename (str): History file name
    """
    import datetime

    # TODO: Load existing history or create new
    try:
        with open(filename, 'r') as f:
            history = json.load(f)
    except (FileNotFoundError, json.JSONDecodeError):
        history = {"queries": []}

    # TODO: Add new entry with timestamp
    entry = {
        "timestamp": datetime.datetime.now().isoformat(),
        "city": city,
        "temperature": weather_data.get('main', {}).get('temp'),
        "description": weather_data.get('weather', [{}])[0].get('description')
    }
    history['queries'].append(entry)

    # TODO: Save back to file
    try:
        with open(filename, 'w') as f:
            json.dump(history, f, indent=2)
        print(f"💾 Saved to history ({len(history['queries'])} total queries)")
    except IOError as e:
        print(f"⚠️  Could not save history: {e}")


def show_weather_history(filename="weather_history.json"):
    """Display weather query history."""
    try:
        with open(filename, 'r') as f:
            history = json.load(f)

        queries = history.get('queries', [])
        if not queries:
            print("No history yet!")
            return

        print(f"\n📜 Weather Query History ({len(queries)} entries):")
        print("─" * 60)

        # Show last 5 queries
        for entry in queries[-5:]:
            timestamp = entry['timestamp'][:19]  # Remove milliseconds
            city = entry['city']
            temp = entry['temperature']
            desc = entry['description']
            print(f"{timestamp} | {city}: {temp}°C, {desc}")

    except FileNotFoundError:
        print("No history file found yet!")
    except (json.JSONDecodeError, KeyError) as e:
        print(f"Error reading history: {e}")


def main():
    """Main application loop."""

    # TODO: Get API key from environment variable
    # This is the SECURE way to handle credentials!
    api_key = os.getenv('WEATHER_API_KEY')

    # TODO: Check if API key is set
    if not api_key:
        print("=" * 70)
        print("❌ ERROR: API key not found!")
        print("=" * 70)
        print("\nYou need to set the WEATHER_API_KEY environment variable.")
        print("\nSteps:")
        print("  1. Get a free API key from: https://openweathermap.org/api")
        print("  2. Set the environment variable:")
        print()
        print("     Mac/Linux:")
        print('       export WEATHER_API_KEY="your-actual-key-here"')
        print()
        print("     Windows (PowerShell):")
        print('       $env:WEATHER_API_KEY="your-actual-key-here"')
        print()
        print("     Windows (Command Prompt):")
        print('       set WEATHER_API_KEY=your-actual-key-here')
        print()
        print("  3. Run this script again")
        print("=" * 70)
        return

    # Application header
    print("=" * 70)
    print("🌦️  WEATHER CHECKER - API Integration Demo")
    print("=" * 70)
    print("\nCommands:")
    print("  - Enter a city name to check weather")
    print("  - Type 'history' to see past queries")
    print("  - Type 'exit' to quit")
    print()

    # TODO: Main interaction loop
    while True:
        # Get user input
        user_input = input("Enter city name (or command): ").strip()

        # Check for exit
        if user_input.lower() in ['exit', 'quit', 'q']:
            print("\n👋 Thanks for using Weather Checker!")
            break

        # Check for history command
        if user_input.lower() == 'history':
            show_weather_history()
            continue

        # Validate input
        if not user_input:
            print("⚠️  Please enter a city name")
            continue

        # TODO: Make API call
        print(f"\n🔍 Fetching weather for {user_input}...")
        weather_data = get_weather(user_input, api_key)

        if weather_data:
            # TODO: Display results
            print(format_weather_display(weather_data))
            print(get_weather_recommendation(weather_data))

            # TODO: Save to history
            save_weather_history(user_input, weather_data)
        else:
            print("⚠️  Could not retrieve weather data. Try again.")

        print()  # Blank line for readability


# ==============================================================================
# OFFLINE TESTING MODE
# ==============================================================================
def test_with_sample_data():
    """
    Test the application with sample JSON data (no API call required).
    Useful for offline development and testing JSON parsing logic.
    """
    # Sample response from OpenWeatherMap API
    sample_weather = {
        "name": "Miami",
        "main": {
            "temp": 28.5,
            "feels_like": 30.2,
            "humidity": 75,
            "pressure": 1012
        },
        "weather": [
            {
                "description": "scattered clouds",
                "main": "Clouds"
            }
        ],
        "wind": {
            "speed": 4.5
        }
    }

    print("=" * 70)
    print("🧪 TESTING MODE - Using Sample Data")
    print("=" * 70)

    print(format_weather_display(sample_weather))
    print(get_weather_recommendation(sample_weather))


# ==============================================================================
# ENTRY POINT
# ==============================================================================
if __name__ == "__main__":
    # Uncomment the line below to test without API key:
    # test_with_sample_data()

    # Run the main application:
    main()