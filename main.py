from flask import Flask,  make_response, jsonify, Response
from flask_restful import reqparse, abort, Api, Resource
from resources.test import Command

import logging
import argparse
import os

app = Flask(__name__)
api = Api(app)

def custom_error(message, status_code):
    return make_response(jsonify(message), status_code)

class Test(Resource):
    def get(self):
        recon = Command.console()

        try:
            res = {
                "message": "msg",
            }

        except Exception as exp:
            logging.error(exp)

            return custom_error({"error": "command not found"}, 404)

        return res


class Root(Resource):
    def get(self):
        return Response(status=200)


api.add_resource(Test, '/test')
api.add_resource(Root, '/')

if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('--log-level', type=str, default='WARNING',
                        help='the logging level (default: WARNING)')

    args = parser.parse_args()

    log_level = getattr(logging, args.log_level.upper())
    logging.basicConfig(level=log_level)

    print('LOG_LEVEL: ', logging.getLevelName(logging.root.level))

    app.run(debug=True, host='0.0.0.0', port=8080)
