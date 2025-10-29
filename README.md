# Weather App Django

Simple Weather app created using django

![alt text](https://github.com/parth0cb/weather-app-django/blob/main/readme_files/screenshot.png?raw=true)

## Installation

1. Clone the repository:
   ```bash
   git clone https://github.com/parth0cb/weather-app-django.git
   cd weather-app-django
   ```

2. Create a virtual environment:
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   ```

3. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```

4. Set up environment variables:
   ```bash
   cp .env.example .env
   ```
   Add your OpenWeatherMap API key to the `.env` file

5. Run migrations:
   ```bash
   python manage.py migrate
   ```

6. Start the development server:
   ```bash
   python manage.py runserver
   ```

## Features

- Real-time weather data
- Search for weather by city
- Displays temperature, humidity, wind speed, and more

## API Used

- [OpenWeatherMap API](https://openweathermap.org/api)
