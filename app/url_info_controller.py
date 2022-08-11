from flask import Flask, request
from app.url_info_db import get_url_info, insert_url_info
import json

app = Flask(__name__)

@app.route('/urlinfo/1/<hostname>/<path>')
def get_url_information(hostname, path):
    malware_info = get_url_info(hostname)
    if not malware_info:
        malware_info = "NOT_MALWARE"
    return malware_info


@app.route('/urlinfo', methods=['POST'])
def save_url_info_api():
    url = request.form['url']
    malware_info = request.form['malware_info']
    return insert_url_info(url, malware_info)

