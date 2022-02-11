from flask import Flask, jsonify, request
import requests

mapsApiKey = 'Enter your apy key here'

app = Flask(__name__)

# find Place

@app.route('/find-place', methods=['POST'])
def call_api_maps():
    query = {
        'fields': 'formatted_address,name,rating,opening_hours,geometry',
        'input': request.json['text'],
        'inputtype': 'textquery',
        'key': mapsApiKey
    }
    api_url = "https://maps.googleapis.com/maps/api/place/findplacefromtext/json"
    try:
        response = requests.get(api_url, params=query)
        result = response.json()
        if result['status'] == 'OK':
            return result
        else:
            return jsonify({'status': 'ZERO_RESULTS', 'message': 'No results found'})

    except requests.exceptions.HTTPError as error:
        print(error)


if __name__ == '__main__':
    app.run(debug=True, port=4000)