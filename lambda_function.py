import json
import requests

def lambda_handler(event, context):
    url = "https://cdn.nba.com/static/json/liveData/scoreboard/todaysScoreboard_00.json"

    response = requests.get(url)
    data = response.json()

    games = data.get("scoreboard", {}).get("games", [])

    hornets_game = None

    for game in games:
        home = game["homeTeam"]["teamName"]
        away = game["awayTeam"]["teamName"]

        if "Hornets" in home or "Hornets" in away:
            hornets_game = game
            break

    if not hornets_game:
        return {
            "statusCode": 200,
            "body": json.dumps({"message": "No Hornets game today"})
        }

    home_score = hornets_game["homeTeam"]["score"]
    away_score = hornets_game["awayTeam"]["score"]
    status = hornets_game["gameStatusText"]

    return {
        "statusCode": 200,
        "headers": {"Access-Control-Allow-Origin": "*"},
        "body": json.dumps({
            "home": home_score,
            "away": away_score,
            "status": status
        })
    }