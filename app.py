from flask import Flask, request
from search import core

import json

app = Flask(__name__)


@app.route('/')
def search():
    verification_id = request.args.get('id')
    print(verification_id)
    res = core.search(verification_id)

    return json.dumps(res)
