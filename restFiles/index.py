# import libraries
from flask_restful import Resource
from flask import Flask, make_response, render_template


class main(Resource):
    def get(self):
        headers = {'Content-Type': 'text/html'}
        return make_response(
                render_template('index.html'), 200, headers)
