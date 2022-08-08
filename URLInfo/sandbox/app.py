from flask import Flask, request
import json

app = Flask(__name__)

@app.route( '/urlinfo/1/<hostname_and_port>/<original_path_and_query_string>')
def get_url_information(hostname_and_port, original_path_and_query_string):
    malware_info = get_url_info(hostname_and_port)
    if not malware_info:
        malware_info = "NOT_MALWARE"
    return malware_info
