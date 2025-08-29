# 3. APIs & Real-World Data Integration

Now that you have a professional IDE set up, it's time to connect your Python code to the outside world. We'll do this using APIs (Application Programming Interfaces).

An API is a set of rules that allows different software applications to communicate with each other. Think of it as a waiter in a restaurant: you (your application) give the waiter (the API) your order (a request for data), and the waiter brings you your food (the data) from the kitchen (the server).

---

## 3.1. Understanding APIs and HTTP Requests

Most web APIs work using the HTTP protocol, the same protocol your browser uses to fetch websites. When we interact with an API, we are making an **HTTP request** to a specific URL (an "endpoint").

This extends the `input-compute-output` paradigm from Lab 02 into a more powerful workflow: `input -> API request -> compute -> output`.

### Exploring a Public API

Let's look at a simple API in the browser. [JSONPlaceholder](https://jsonplaceholder.typicode.com/todos/1) is a free fake API for testing.

**Activity**: Click the link above. You'll see a response in your browser that looks like this:

```json
{
  "userId": 1,
  "id": 1,
  "title": "delectus aut autem",
  "completed": false
}
```

This format is called **JSON (JavaScript Object Notation)**. It is the standard language for data exchange on the web. Notice how it resembles a Python dictionary—this makes it very easy to work with in Python.

---

## 3.2. Weather API Implementation Project

**Project Goal**: Build a command-line weather checker application that fetches live data from the internet.

We will use the [OpenWeatherMap API](https://openweathermap.org/api), a popular service for accessing weather data.

### Step 1: OpenWeatherMap API Registration and Setup 

**Complete Registration Walkthrough:**

1. **Navigate to OpenWeatherMap**
   - Go to [openweathermap.org/api](https://openweathermap.org/api)
   - Click "Sign Up" in the top right corner

2. **Create Your Account**
   - **Email**: Use your student email address
   - **Username**: Choose something professional (you might use this for other APIs)
   - **Password**: Create a strong, unique password
   - Click "Create Account"

3. **Verify Your Email**
   - Check your email inbox (and spam folder)
   - Click the verification link in the email from OpenWeatherMap
   - **Critical**: Your API won't work without email verification

4. **Access Your API Key**
   - After verification, log in to [home.openweathermap.org/api_keys](https://home.openweathermap.org/api_keys)
   - You'll see a "Default" API key already created for you
   - Copy this key (format: `abc123def456ghi789jkl012` - 32 characters)
   - **Security Note**: Keep this key private - never share it or commit it to Git

5. **Test Your API Key**
   - Open a new browser tab
   - Use this URL, replacing `YOUR_KEY_HERE` with your actual API key:
     ```
     https://api.openweathermap.org/data/2.5/weather?q=London&appid=YOUR_KEY_HERE&units=metric
     ```
   - **Success**: JSON weather data appears for London
   - **Error**: Double-check your key and email verification status

**Understanding the Response:**
The JSON contains structured weather data:
```json
{
  "main": {
    "temp": 15.3,
    "feels_like": 14.8
  },
  "weather": [
    {
      "description": "light rain"
    }
  ]
}
```

**Free Tier Details:**
- 1,000 API calls per month (sufficient for this lab)
- Weather data updates every 10 minutes
- No credit card required

### API Key Security: Environment Variables

**Why Environment Variables?**
Environment variables are the professional standard for storing sensitive information like API keys. Here's why:

- **Security**: Never accidentally commit secrets to Git repositories
- **Flexibility**: Different keys for development/testing/production
- **Access Control**: Only authorized users can see the values

**How Environment Variables Work:**
1. **Operating System Storage**: Your OS stores key-value pairs (like `WEATHER_API_KEY=abc123`)
2. **Application Access**: Python reads these values with `os.getenv('WEATHER_API_KEY')`
3. **Session Scope**: Variables exist until terminal closes or system restart

**Setting Environment Variables:**

**Windows (Command Prompt/PowerShell):**
```cmd
set WEATHER_API_KEY=your-actual-api-key-here
python weather_checker.py
```

**Mac/Linux (Terminal):**
```bash
export WEATHER_API_KEY="your-actual-api-key-here"
python weather_checker.py
```

**VS Code Integrated Terminal:**
Use the same commands as above in VS Code's built-in terminal.

### Step 2: Core Implementation

Now, let's build the application. In your `weather_app` project, open the `src/weather_checker.py` file and enter the following code. Read through the comments to understand how each part works.

```python
import requests
import json

def get_weather(city, api_key):
    """Gets weather data for a specific city from the OpenWeatherMap API."""
    # The API endpoint URL, formatted with the city and API key
    url = f"http://api.openweathermap.org/data/2.5/weather?q={city}&appid={api_key}&units=metric"
    
    try:
        # Make the HTTP GET request to the API
        response = requests.get(url)
        
        # If the request was successful (status code 200)
        if response.status_code == 200:
            # Parse the JSON response into a Python dictionary and return it
            return response.json()
        else:
            # If the request failed (e.g., city not found), return None
            return None
    except requests.RequestException:
        # Handle network-related errors (e.g., no internet connection)
        return None

def main():
    """Main function to run the weather checker app."""
    # SECURE METHOD: Use environment variables for API keys
    import os
    api_key = os.getenv('WEATHER_API_KEY')
    
    # Check if API key is set
    if not api_key:
        print("❌ Error: API key not found!")
        print("Please set your API key as an environment variable.")
        print("Instructions:")
        print("  Windows: set WEATHER_API_KEY=your-actual-key-here")
        print("  Mac/Linux: export WEATHER_API_KEY=your-actual-key-here")
        print("  Then restart this program.")
        return
    
    print("--- Weather Checker App ---")
    print("Enter 'exit' to quit.")
    
    while True:
        # Get user input for the city name
        city = input("\nEnter city name: ").strip()
        
        # Check if the user wants to exit
        if city.lower() == 'exit':
            print("Thanks for using Weather Checker!")
            break
            
        # Call our function to get the weather data
        weather_data = get_weather(city, api_key)
        
        # Check if we got valid data back
        if weather_data:
            # Extract the specific pieces of data we want from the dictionary
            temp = weather_data['main']['temp']
            description = weather_data['weather'][0]['description']
            feels_like = weather_data['main']['feels_like']
            
            # Display the weather information in a user-friendly format
            print(f"\nWeather in {city.title()}:")
            print(f"  Temperature: {temp}°C (feels like {feels_like}°C)")
            print(f"  Conditions:  {description.title()}")
            
            # Bonus: Provide a smart recommendation based on the weather
            if 'rain' in description or 'drizzle' in description:
                print("  💧 Recommendation: Don't forget your umbrella!")
            elif 'snow' in description:
                print("  ❄️  Recommendation: Dress warmly and wear boots!")
            elif temp > 25:
                print("  ☀️  Recommendation: It's a great day for outdoor activities!")
        else:
            # Handle cases where the city was not found or an error occurred
            print(f"❌ Could not find weather data for '{city}'. Please check the city name.")

# This standard Python construct ensures that main() runs only when the script is executed directly
if __name__ == "__main__":
    main()
```

> **⭐ Best Practice: API Key Security**
> 
> In this lab, we might place the API key directly in the script for simplicity. In any real-world application, you should **never** do this! Committing code with visible keys or passwords is a major security risk.
> 
> Professionals use **environment variables** or secret management tools to handle sensitive data. This involves storing the key outside the code and loading it in dynamically, ensuring it never gets exposed in your Git repository.

### Step 3: Debugging and Enhancement

-   **Run Your Code**: Open the integrated terminal in VS Code, activate your `conda` environment (`conda activate lab03`), navigate to your `src` directory, and run the script: `python weather_checker.py`.
-   **Debugging Practice**: VS Code has a powerful debugger. Try setting a breakpoint by clicking to the left of a line number in `get_weather`. Then press `F5` to start debugging. When the code pauses, you can inspect variables and step through the execution line by line.
-   **Enhancement Challenges**:
    1.  Add the current humidity (`humidity`) and wind speed (`wind['speed']`) to the output.
    2.  Can you think of other "smart recommendations" to add?

---

## 3.3. Advanced Features and Error Handling

The code above includes basic error handling, but professional applications need to be even more robust.

-   **Robust Error Handling**: What happens if the API is down? Or your API key is invalid? A professional app would have specific `try...except` blocks to handle `requests.Timeout`, `requests.ConnectionError`, and check for specific HTTP status codes like `401 Unauthorized` (invalid key) or `404 Not Found` (city not found).
-   **Data Validation**: What if the API response changes and the `'main'` key is missing? Before accessing `weather_data['main']['temp']`, you should check if `'main'` and `'temp'` actually exist in the dictionary.
-   **User Experience**: You could make the city search case-insensitive or even add a feature to save a list of favorite cities to a file.

These advanced topics are crucial for building real-world applications and are great next steps for you to explore as you enhance your weather app.
