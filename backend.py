from flask import Flask,request,jsonify
from flask_cors import CORS

app = Flask(__name__)
CORS(app)
locations = []

@app.route('/gps',methods=['POST'])
def receive_gps():
    data = request.get_json()
    print("Received:",data)
    locations.append(data)
    return jsonify({"status":"success"}),200

@app.route('/locations',methods=['GET'])
def get_locations():
    return jsonify(locations)

if __name__ == '__main__':
    app.run(debug=True)