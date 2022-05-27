from flask_restful import Api
from Api.Task import Task
from Api.taskById import taskById
from App import FlaskInstance
restServer = Api(FlaskInstance)
restServer.add_resource(Task,"/Api/getMessage")
restServer.add_resource(taskById,"/Api/v1.0/taskById/<string:TaskId>")