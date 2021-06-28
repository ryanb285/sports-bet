# web_app/routes/weather_routes.py

from flask import Blueprint, request, jsonify, render_template, redirect, flash

from app.bets import sport, team

weather_routes = Blueprint("weather_routes", __name__)

@weather_routes.route("/weather/forecast.json")
def weather_forecast_api():
    print("WEATHER FORECAST (API)...")
    print("URL PARAMS:", dict(request.args))

    team = request.args.get("team") or "New York Yankees"
    sport = request.args.get("sport") or "baseball_mlb"

    results = get_hourly_forecasts(team=team, sport=sport)
    if results:
        return jsonify(results)
    else:
        return jsonify({"message":"Invalid inputs. Please try again."}), 404

@weather_routes.route("/weather/form")
def weather_form():
    print("WEATHER FORM...")
    return render_template("weather_form.html")

@weather_routes.route("/weather/forecast", methods=["GET", "POST"])
def weather_forecast():
    print("WEATHER FORECAST...")

    if request.method == "GET":
        print("URL PARAMS:", dict(request.args))
        request_data = dict(request.args)
    elif request.method == "POST": # the form will send a POST
        print("FORM DATA:", dict(request.form))
        request_data = dict(request.form)

    team = request_data.get("team") or "New York Yankees"
    sport = request_data.get("sport") or "baseball_mlb"

    results = get_hourly_forecasts(team=team, sport=sport)
    if results:
        #flash("Weather Forecast Generated Successfully!", "success")
        return render_template("weather_forecast.html", team=team, sport=sport, results=results)
    else:
        #flash("Geography Error. Please try again!", "danger")
        return redirect("/weather/form")

