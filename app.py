from flask import Flask, render_template, request
from music_processing import Analyser

app = Flask(__name__)
app.config['SEND_FILE_MAX_AGE_DEFAULT'] = 60


@app.route('/')
def index():
    return render_template("index.html")


@app.route("/", methods=["POST"])
def register():
    device_id = request.form["deviceID"]
    artists_number = request.form["artNum"]
    concerts = Analyser().analyse(device_id, artists_number)
    if concerts:
        return render_template("result.html", concerts=concerts)
    else:
        return render_template("noresult.html")


if __name__ == '__main__':
    app.run()
