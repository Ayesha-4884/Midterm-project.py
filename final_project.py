import random
from datetime import datetime, timedelta
from rich.console import Console
from rich.table import Table

# Initialize console for colorful output
console = Console()

def generate_weather():
    """Simulate weather data."""
    conditions = ["Sunny", "Cloudy", "Rainy", "Stormy", "Foggy", "Windy"]
    return {
        "temperature": random.randint(15, 40),
        "humidity": random.randint(20, 90),
        "condition": random.choice(conditions),
        "wind_speed": round(random.uniform(2.5, 15.0), 1),
    }

def display_weather_report(days=3):
    """Display a weather report for the next 'days' days."""
    table = Table(title=" Weather Forecast Report", show_lines=True)

    table.add_column("Date", justify="center", style="cyan", no_wrap=True)
    table.add_column("Condition", justify="center", style="yellow")
    table.add_column("Temp (°C)", justify="center", style="red")
    table.add_column("Humidity (%)", justify="center", style="blue")
    table.add_column("Wind Speed (km/h)", justify="center", style="green")

    today = datetime.now()
    for i in range(days):
        forecast_date = (today.strftime("%A, %d %b %Y"))
        weather = generate_weather()
        table.add_row(
            forecast_date,
            weather["condition"],
            f"{weather['temperature']}°C",
            f"{weather['humidity']}%",
            f"{weather['wind_speed']} km/h",
        )
        today += timedelta(days=1)      

    console.print(table)

if __name__ == "__main__":
    console.print("[bold green]Welcome to the Professional Weather Report [/bold green]")
    display_weather_report(days=5)
    console.print("[bold magenta]Thank you for using this tool![/bold magenta]")