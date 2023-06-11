import flask
import json
from flask import Flask
from flask import Response
app = Flask(__name__)

@app.route('/')
@app.route('/<path:path>')
@app.route('/api/auth/login', methods=["POST"])
def login() -> Response | str:
    user_info = flask.request.get_json()
    print(user_info)
    res = {
        'status': 'success',
        'data': {
            'userId': "NEED CONNECTION WITH DB",
            'username': "NEED CONNECTION WITH DB",
            'accessToken': "NEED CONNECTION WITH DB"
        }
    }
    return json.dumps(res)

if __name__ == "__main__":
    app.run(threaded=True, host="127.0.0.1", port=3001, debug=True)