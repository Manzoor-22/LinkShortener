import random
import string

from flask import Flask, render_template, redirect, request

app = Flask(__name__)
shortened_urls= {}

def generate_url(length = 5):
    chars = string.ascii_letters + string.digits
    short_url = "".join(random.choice(chars) for _ in range(length))
    return short_url

@app.route("/", methods=["GET", "POST"])
def index():
    if request.method == "POST":
        long_url = request.form['long_url']
        short_url = generate_url()
        while short_url in shortened_urls:
            short_url = generate_url()

        shortened_urls[short_url] = long_url
        return f"Shortened URL:  {request.url_root}{short_url}"
    return render_template("index.html")


@app.route("/<short_url>")
def redirect_url(short_url):
    long_url = shortened_urls.get(short_url)
    if long_url:
        return redirect(long_url)
    else:
        return "URL not found!"
    
if __name__ == "__main__":
    app.run(debug = True)
