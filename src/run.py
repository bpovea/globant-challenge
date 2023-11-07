from flask import Flask
from flask_restful import Api
from app.api.resources import *
from app.config import *
from app.db import db


app = Flask(__name__)
app.debug = DEBUG
api = Api(app)

app.config["SQLALCHEMY_DATABASE_URI"] = SQLALCHEMY_DATABASE_URI
db.init_app(app)

api.add_resource(DepartmentListResource, "/departments")
api.add_resource(DepartmentResource, "/departments/<int:department_id>")
api.add_resource(JobListResource, "/jobs")
api.add_resource(JobResource, "/jobs/<int:job_id>")
api.add_resource(EmployeeListResource, "/employees")
api.add_resource(EmployeeResource, "/employees/<int:employee_id>")

api.add_resource(PopulateDataResource, "/populate_data")
