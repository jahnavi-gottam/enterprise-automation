from flask import Flask, request, jsonify
from preprocess import preprocess_data
from utils import save_to_database

app = Flask(__name__)


@app.route('/')
def home():
    return "Welcome to the Data Entry API"

@app.route('/data-entry', methods=['POST'])
def data_entry():
    data = request.json
    preprocessed_data = preprocess_data(data)
    save_to_database(preprocessed_data)
    return jsonify({"message": "Data entry successful"}), 201

if __name__ == '__main__':

    app.run(debug=True)
