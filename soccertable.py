from flask import Flask, render_template

app = Flask(__name__)

# Teams data
teams_data = [
    {"name": "Beitar Jerusalem", "place": 1, "points": 75, "wins": 24, "draws": 3, "losses": 1, "goals_scored": 80, "goals_conceded": 15},
    {"name": "Manchester City", "place": 2, "points": 71, "wins": 23, "draws": 2, "losses": 3, "goals_scored": 85, "goals_conceded": 20},
    {"name": "Barcelona", "place": 3, "points": 65, "wins": 20, "draws": 5, "losses": 3, "goals_scored": 72, "goals_conceded": 29},
    {"name": "PSG", "place": 4, "points": 64, "wins": 21, "draws": 1, "losses": 6, "goals_scored": 70, "goals_conceded": 36},
    {"name": "Bayern", "place": 5, "points": 54, "wins": 15, "draws": 9, "losses": 4, "goals_scored": 54, "goals_conceded": 35},
    {"name": "Juventus", "place": 6, "points": 52, "wins": 15, "draws": 7, "losses": 6, "goals_scored": 51, "goals_conceded": 42},
    {"name": "Hapoel tel aviv", "place": 7, "points": 41, "wins": 11, "draws": 8, "losses": 9, "goals_scored": 42, "goals_conceded": 46},
    {"name": "Dortmund", "place": 8, "points": 38, "wins": 10, "draws": 8, "losses": 10, "goals_scored": 41, "goals_conceded": 50},
    {"name": "Sakhnin", "place": 9, "points": 35, "wins": 9, "draws": 8, "losses": 11, "goals_scored": 40, "goals_conceded": 61},
    {"name": "Milan", "place": 10, "points": 32, "wins": 9, "draws": 5, "losses": 14, "goals_scored": 42, "goals_conceded": 69},
    {"name": "Ashdod", "place": 11, "points": 28, "wins": 8, "draws": 4, "losses": 16, "goals_scored": 33, "goals_conceded": 65},
    {"name": "Inter", "place": 12, "points": 27, "wins": 8, "draws": 3, "losses": 17, "goals_scored": 30, "goals_conceded": 68},
    {"name": "Spurs", "place": 13, "points": 26, "wins": 8, "draws": 2, "losses": 18, "goals_scored": 30, "goals_conceded": 75},
]

@app.route('/')
def index():
    return render_template('index.html', teams_data=teams_data)

if __name__ == '__main__':
    app.run(host="0.0.0.0", port=9119, debug=True)
