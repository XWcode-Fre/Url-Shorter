from flask import Flask, request, redirect, url_for
import string
import random

app = Flask(__name__)
url_mapping = {}

def generate_short_url():
    characters = string.ascii_letters + string.digits
    short_url = ''.join(random.choice(characters) for _ in range(6))
    return short_url

@app.route('/shorted', methods=['POST'])
def shorten_url():
    original_url = request.form['url']
    short_url = generate_short_url()
    url_mapping[short_url] = original_url
    return f'Укороченый юрл: {request.host_url}{short_url}'

@app.route('/<short_url>')
def redirect_url(short_url):
    original_url = url_mapping.get(short_url)
    if original_url:
        return redirect(original_url)
    else:
        return 'Юрл не найден', 404
    
if __name__ == "__main__":
    app.run(debug=True)
