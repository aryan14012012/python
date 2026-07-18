import requests
import sys
from datetime import datetime


def get_weather(city):
    """Fetch weather and AQI data for a given city"""
    try:
        # Fetch weather data
        response = requests.get(f"https://wttr.in/{city}?format=j1", timeout=10)
        response.raise_for_status()
        data = response.json()
        
        current = data["current_condition"][0]
        weather_info = {
            "city": city.title(),
            "temperature": int(float(current["temp_C"])),
        }
        
        # Try to get AQI data from wttr.in
        # wttr.in provides air quality in the aqi field
        if "air_quality" in current:
            aqi = current["air_quality"]
            if "pm2.5" in aqi:
                weather_info["aqi"] = aqi["pm2.5"]
            elif "co" in aqi:
                weather_info["aqi"] = aqi["co"]
        
        return weather_info
    except requests.exceptions.RequestException as e:
        print(f"Error fetching weather data: {e}")
        return None
    except (KeyError, IndexError, ValueError) as e:
        print(f"Error parsing data: {e}")
        return None


def display_weather(weather):
    """Display temperature and AQI"""
    if not weather:
        return
    
    print("\n" + "="*40)
    print(f"🌡️  {weather['city']}")
    print("="*40)
    print(f"Temperature: {weather['temperature']}°C")
    
    if "aqi" in weather:
        print(f"AQI:        {weather['aqi']}")
    else:
        print("AQI:        N/A")
    
    print("="*40 + "\n")


def main():
    """Main function to run the weather app"""
    print("\n🌍 Weather App")
    print("="*40)
    
    # Get city from command line arguments or prompt user
    if len(sys.argv) > 1:
        city = " ".join(sys.argv[1:])
    else:
        city = input("Enter city name: ").strip()
    
    if not city:
        print("Error: Please provide a city name.")
        sys.exit(1)
    
    weather = get_weather(city)
    
    if weather:
        display_weather(weather)
    else:
        print(f"\n❌ Could not fetch data for '{city}'.")
        print("Please check the city name and try again.\n")
        sys.exit(1)


if __name__ == "__main__":
    main()