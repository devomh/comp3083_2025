# Introduction to APIs and HTTP Requests

## Overview

Now that you've mastered JSON, you're ready to learn one of its most powerful applications: **consuming web APIs**. APIs (Application Programming Interfaces) let your Python programs access data from across the internet—weather information, stock prices, social media posts, and much more. Since most APIs return data in JSON format, all your JSON skills will be put to immediate use!

### Prerequisites
- JSON mastery (Modules 1-3)
- Understanding of Python dictionaries and error handling
- Basic command-line usage

## What is an API?

An **API (Application Programming Interface)** is a set of rules that allows different software applications to communicate with each other. Think of it as a menu at a restaurant:

- **You** (your Python program) look at the menu (API documentation)
- **You order** (make a request) specific items with specific options
- **The waiter** (the API) takes your order to the kitchen (the server)
- **The kitchen** (the server) prepares your food (processes data)
- **The waiter brings your food** (the API returns JSON data)

### The Request-Response Cycle

```
Your Python Program  →  HTTP Request  →  API Server
                                            ↓
                                      Process Request
                                            ↓
Your Python Program  ←  JSON Response  ←  API Server
```

### Extending the Input-Compute-Output Paradigm

Remember the basic programming pattern from earlier labs?

```
Input → Compute → Output
```

APIs extend this to:

```
Input → API Request → Process JSON → Compute → Output
```

---

## Understanding HTTP Requests

Most web APIs use the **HTTP protocol**—the same protocol your browser uses to load websites.

### Key HTTP Concepts

**1. URL (Endpoint)**
The address of the API service:
```
https://api.example.com/v1/weather?city=Miami
```

**2. HTTP Methods**
- `GET`: Retrieve data (most common for APIs)
- `POST`: Send data to create something
- `PUT`: Update existing data
- `DELETE`: Remove data

For this lab, we'll focus on `GET` requests.

**3. Status Codes**
The server responds with a code indicating success or failure:

| Code | Meaning | Description |
|------|---------|-------------|
| 200 | OK | Request succeeded |
| 400 | Bad Request | Invalid request parameters |
| 401 | Unauthorized | Missing or invalid API key |
| 404 | Not Found | Resource doesn't exist |
| 500 | Server Error | Problem on the server side |

**4. Response Body**
The actual data returned, usually in JSON format.

---

## Exploring a Public API (No Code!)

Let's start by understanding APIs without writing code.

### Activity: Browser-Based API Exploration

1. **Visit JSONPlaceholder** - A free fake API for testing:
   ```
   https://jsonplaceholder.typicode.com/todos/1
   ```

2. **Observe the Response**:
   ```json
   {
     "userId": 1,
     "id": 1,
     "title": "delectus aut autem",
     "completed": false
   }
   ```

3. **Notice**:
   - The URL is the **endpoint**
   - The data is **JSON** (looks like a Python dictionary!)
   - Your browser made a **GET request**
   - The server responded with **JSON data**

4. **Try Different Endpoints**:
   - All todos: `https://jsonplaceholder.typicode.com/todos`
   - Specific user: `https://jsonplaceholder.typicode.com/users/1`
   - Posts: `https://jsonplaceholder.typicode.com/posts`

**Key Insight**: When you visit these URLs in your browser, you're making the same type of request your Python program will make!

---

## Making Your First API Request in Python

Python's `requests` library makes API calls simple.

### Installing `requests`

If not already installed:
```bash
pip install requests
```

### Basic GET Request

```python
import requests
import json

# Make a GET request
response = requests.get('https://jsonplaceholder.typicode.com/todos/1')

# Check if request was successful
if response.status_code == 200:
    # Parse JSON response
    data = response.json()  # Same as json.loads(response.text)

    print("✓ Request successful!")
    print(f"Title: {data['title']}")
    print(f"Completed: {data['completed']}")
else:
    print(f"❌ Request failed with status code: {response.status_code}")
```

**Output:**
```
✓ Request successful!
Title: delectus aut autem
Completed: False
```

### Anatomy of a Request

```python
import requests

# 1. Make the request
response = requests.get('https://api.example.com/endpoint')

# 2. Check the status
print(f"Status Code: {response.status_code}")

# 3. Get the JSON data
data = response.json()  # Automatically parses JSON to Python dict

# 4. Access the data (just like Module 3!)
print(data['some_field'])
```

---

## Practical Example: Name Age Predictor

Let's use a simple API that predicts age based on name (no API key required!).

```python
import requests

def predict_age(name):
    """
    Use the Agify API to predict age based on name.
    API: https://api.agify.io
    """
    # Build the URL with query parameter
    url = f"https://api.agify.io?name={name}"

    try:
        # Make the request
        response = requests.get(url)

        # Check if successful
        if response.status_code == 200:
            data = response.json()

            # The API returns: {"name": "alice", "age": 42, "count": 12345}
            predicted_age = data.get('age')

            if predicted_age:
                print(f"📊 Predicted age for '{name}': {predicted_age}")
                print(f"   (Based on {data['count']:,} data points)")
            else:
                print(f"⚠️  No prediction available for '{name}'")
        else:
            print(f"❌ Request failed: {response.status_code}")

    except requests.RequestException as e:
        print(f"❌ Network error: {e}")

# Test it
predict_age("Alice")
predict_age("Bob")
predict_age("Maria")
```

**Output:**
```
📊 Predicted age for 'Alice': 42
   (Based on 234,567 data points)
📊 Predicted age for 'Bob': 43
   (Based on 187,234 data points)
📊 Predicted age for 'Maria': 39
   (Based on 456,789 data points)
```

---

## Error Handling for APIs

APIs can fail for many reasons. Always use proper error handling!

### Comprehensive Error Handling Pattern

```python
import requests

def safe_api_call(url):
    """Template for safe API calls with error handling."""
    try:
        # Make the request with a timeout
        response = requests.get(url, timeout=5)

        # Check status code
        if response.status_code == 200:
            return response.json()
        elif response.status_code == 404:
            print("❌ Resource not found")
            return None
        elif response.status_code == 401:
            print("❌ Unauthorized - check your API key")
            return None
        else:
            print(f"❌ Request failed: {response.status_code}")
            return None

    except requests.Timeout:
        print("❌ Request timed out")
        return None
    except requests.ConnectionError:
        print("❌ Network connection error")
        return None
    except requests.RequestException as e:
        print(f"❌ Request error: {e}")
        return None
    except json.JSONDecodeError:
        print("❌ Invalid JSON in response")
        return None

# Usage
data = safe_api_call("https://api.example.com/data")
if data:
    print("✓ Data received successfully!")
```

---

## Working with API Keys

Many APIs require authentication via an **API key**—a unique identifier that tracks your usage.

### What is an API Key?

- A long string like: `abc123def456ghi789jkl012`
- Identifies you to the API service
- Tracks your usage (most APIs have free tier limits)
- **Must be kept secret!** Never share or commit to Git

### Environment Variables: The Secure Approach

**Why Environment Variables?**
1. **Security**: Keys never appear in your code
2. **Flexibility**: Different keys for different environments
3. **Safety**: Can't accidentally commit secrets to Git

**Setting Environment Variables:**

**Mac/Linux:**
```bash
export API_KEY="your-actual-api-key-here"
python your_script.py
```

**Windows (PowerShell):**
```powershell
$env:API_KEY="your-actual-api-key-here"
python your_script.py
```

**Windows (Command Prompt):**
```cmd
set API_KEY=your-actual-api-key-here
python your_script.py
```

**Using in Python:**
```python
import os

# Read environment variable
api_key = os.getenv('API_KEY')

if not api_key:
    print("❌ Error: API_KEY environment variable not set!")
    print("Set it with:")
    print("  Mac/Linux: export API_KEY='your-key'")
    print("  Windows: set API_KEY=your-key")
    exit(1)

# Use the key
url = f"https://api.example.com/data?key={api_key}"
```

---

## Exercises

### Exercise 1: Explore an API in Browser

Visit these APIs in your web browser and identify the JSON structure:
1. `https://api.agify.io?name=Michael`
2. `https://api.nationalize.io?name=Maria`
3. `https://jsonplaceholder.typicode.com/users`

For each:
- What is the top-level structure? (object or array)
- What fields are present?
- What data types do you see?

### Exercise 2: First Python API Call

Write a script that:
1. Makes a GET request to `https://api.agify.io?name=YourName`
2. Parses the JSON response
3. Prints: "The predicted age for [name] is [age]"
4. Handles errors gracefully

### Exercise 3: Nationality Predictor

Use the `https://api.nationalize.io` API to predict nationality from a name.

Example URL: `https://api.nationalize.io?name=Maria`

Response format:
```json
{
  "name": "Maria",
  "country": [
    {"country_id": "BR", "probability": 0.12},
    {"country_id": "MX", "probability": 0.10},
    ...
  ]
}
```

Write a function that:
1. Takes a name as input
2. Calls the API
3. Prints the top 3 predicted countries with probabilities

### Exercise 4: Multi-API Data Combiner

Combine data from two APIs:
1. Get age prediction from `https://api.agify.io?name=NAME`
2. Get nationality from `https://api.nationalize.io?name=NAME`
3. Create a combined JSON object and print it

---

## Key Takeaways

1. **APIs enable data exchange** between your program and external services
2. **HTTP GET requests** are the most common API operation
3. **Status codes** tell you if the request succeeded or failed
4. **JSON is the standard** format for API responses
5. **Error handling is essential** - networks and APIs can fail
6. **API keys** must be stored securely using environment variables
7. **Your JSON skills** directly apply to parsing API responses!

**Next Module**: [Weather Checker Project - Putting It All Together](06_weather_checker.py)

---

## Additional Resources

### Free APIs for Practice (No Key Required)
- [JSONPlaceholder](https://jsonplaceholder.typicode.com/) - Fake REST API for testing
- [Agify](https://api.agify.io) - Predict age from name
- [Nationalize](https://api.nationalize.io) - Predict nationality from name
- [PokeAPI](https://pokeapi.co/) - Pokemon data
- [REST Countries](https://restcountries.com/) - Country information

### API Documentation
- [Requests Library Docs](https://requests.readthedocs.io/)
- [HTTP Status Codes](https://httpstatuses.com/)
