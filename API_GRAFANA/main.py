from flask import Flask, render_template, jsonify, request

from mongodb import mongodb_stations_infos, mongodb_stations_bikes, stations

app = Flask(__name__)



@app.route('/')
def main():
    return "<h1>ca marche !</h1>regarde la doc mnt. <b>#y a pas de doc.</b></br></br><h1>Documentation</h1>Infos sur les stations : <a href='./api/stations_infos'>/api/stations_infos</a></br>Vélo dispo dans chaque stations : <a href='./api/stations_bikes'>/api/stations_bikes</a>"


@app.route("/search", methods=['POST'])
def search():
    return jsonify(["available_bike_stands","available_bikes","all_bike_stands","all_available_bikes","id"])

@app.route("/query", methods=['POST'])
def query():
    req = request.get_json()
    data = stations(req['targets'][0]['target'])
    return jsonify(data)

@app.route("/annotations")
def annotations():
    req = request.get_json()
    data = [
        {
            "annotation": 'This is the annotation',
            "time": (convert_to_time_ms(req['range']['from']) +
                     convert_to_time_ms(req['range']['to'])) / 2,
            "title": 'Deployment notes',
            "tags": ['tag1', 'tag2'],
            "text": 'Hm, something went wrong...'
        }
    ]
    return jsonify(data)



@app.route('/api/stations_infos')
def get_stations_info():
    data = mongodb_stations_infos()
    return jsonify(data)


@app.route('/api/stations_bikes')
def get_stations_bikes():
    data = mongodb_stations_bikes()
    return jsonify(data)

if __name__ == "__main__":
    app.run(debug=False, host="0.0.0.0", port=8888)