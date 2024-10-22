from flask import Flask, jsonify
from select_info import SelectInfo
import logging

logging.basicConfig(filename='logs.log', level=logging.ERROR, format='%(asctime)s:%(message)s') 


app = Flask(__name__)

@app.route('/api/faults', methods=['GET'])
def get_open_tickets():
    try:
        select_info = SelectInfo()
        return jsonify(select_info.get_fault())

    except Exception as e:
        logging.error(e)

@app.route('/api/install_with_cable', methods=['GET'])
def get_install_with_cable():
    try:
        select_info = SelectInfo()
        return jsonify(select_info.get_install_with_cable())

    except Exception as e:
        logging.error(e)

@app.route('/api/install_without_cable', methods=['GET'])
def get_install_without_cable():
    try:
        select_info = SelectInfo()
        return jsonify(select_info.get_install_without_cable())

    except Exception as e:
        logging.error(e)

if __name__ == '__main__':
    app.run(host='192.168.80.138', port=5000)