# web_app/routes/weather_routes.py

from flask import Blueprint, request, jsonify

from app.bets import get_hourly_forecasts
#these need to be updated so they can connect to our bets. the import we need from the def fcn



weather_routes = Blueprint("weather_routes", __name__)

@weather_routes.route("/weather/forecast.json")
def weather_forecast_api():
    print("WEATHER FORECAST (API)...")
    print("URL PARAMS:", dict(request.args))

    country_code = request.args.get("country_code") or "US"
    zip_code = request.args.get("zip_code") or "20057"

    results = get_hourly_forecasts(country_code=country_code, zip_code=zip_code)
    if results:
        return jsonify(results)
    else:
        return jsonify({"message":"Invalid Geography. Please try again."}), 404

