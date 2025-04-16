from flask import Flask, render_template, request
import pyshorteners

app = Flask(__name__)


@app.route("/", methods=['POST', 'GET'])
def home():
    if request.method == "POST":
        url_received = request.form["url"]
        short_url = pyshorteners.Shortener().tinyurl.short(url_received)
        return render_template("form.html", new_url=short_url, old_url=url_received)
    else:
        return render_template('form.html')


if __name__ == "__main__":
    app.run()
