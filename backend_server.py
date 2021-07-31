from flask import Flask, request, jsonify
from flask_cors import CORS
from socket_client import send_message

app = Flask(__name__)
CORS(app)

@app.route("/multiplication-table", methods=["POST"])
def multiplication_table():
    data = request.get_json()
    number = data['number']
    output = []
    for i in range(1, 11):
        v = str(number) + " X " + str(i) + " = " + str(number*i)
        send_message("multiplication_table_server", v, "user1")
        output.append(v)    
    return jsonify({'table': output}), 200

if __name__ == "__main__":
    app.run(host='0.0.0.0', port='8080')
