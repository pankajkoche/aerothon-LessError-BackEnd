from flask_restful import Resource
import logging as log
class Task(Resource):
    def get(Self):
        log.debug("Inside GET Method")
        return ("hey!, You are Awesome. Now you are connected with backend. keep going",200 ) # 200 is a success call
    def post(Self):
        log.debug("Inside POST Method")
        return {" POST method"},200 
    def put(Self):
        log.debug("Inside PUT Method")
        return {" PUT method"},200 
    def delete(Self):
        log.debug("Inside DELETE Method")
        return {" DELETE method"},200  