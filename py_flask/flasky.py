import flask
import rapidjson as json


app = flask.Flask(__name__, template_folder='.')


@app.route('/json')
def api_json():
    data = json.dumps({"message": "Hello, World!"})
    res = flask.Response(data, mimetype="application/json")
    return res


if __name__ == '__main__':
    app.run('0.0.0.0')

