from flask import Flask, request
from search import core

import json

app = Flask(__name__)


@app.route('/')
def search():
    verification_id = request.args.get('id')
    res = core.query(verification_id)

    return json.dumps(res, indent=4, sort_keys=False, default=str)
