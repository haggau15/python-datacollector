from flask import Flask, request
import pika
from pika import channel

app = Flask(__name__)

@app.route('/requestdata', methods=['POST'])
def handle_post():
    if request.method == 'POST':
        data = request.json  # Assuming JSON data is being sent
        # Do something with the data
        print("Received data:", data)
        return "Data received successfully", 200
    else:
        return "Only POST requests are allowed", 405


if __name__ == '__main__':
    app.run(debug=True, port=5000)
