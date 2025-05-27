from flask import Flask, render_template, request
import requests

app = Flask(__name__)


GIPHY_API_KEY = 'dATHBlMCF3Pbyeu1nUYET65bfDou1tCS'

@app.route('/', methods=['GET', 'POST'])
def index():
    gifs = []
    if request.method == 'POST':
        search_term = request.form['search']
        response = requests.get(
            'https://api.giphy.com/v1/gifs/search',
            params={
                'api_key': GIPHY_API_KEY,
                'q': search_term,
                'limit': 5,
                'rating': 'g'
            }
        )
        if response.status_code == 200:
            data = response.json()
            gifs = [gif['images']['original']['url'] for gif in data['data']]
    return render_template('index.html', gifs=gifs)

if __name__ == '__main__':
    app.run(debug=True)
