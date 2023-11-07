from flask import request
from flask_restful import Resource

from app.db import db
from app.api.models import Employee, Department, Job


class EmployeeResource(Resource):
    def get(self, employee_id):
        employee = Employee.query.get(employee_id)
        if employee:
            return {
                "id": employee.id,
                "name": employee.name,
                "department_id": employee.department_id,
                "job_id": employee.job_id,
            }
        return {"message": "Employee not found"}, 404

    def put(self, employee_id):
        employee = Employee.query.get(employee_id)
        if employee:
            data = request.get_json()
            employee.name = data["name"]
            employee.department_id = data["department_id"]
            employee.job_id = data["job_id"]
            db.session.commit()
            return {
                "id": employee.id,
                "name": employee.name,
                "department_id": employee.department_id,
                "job_id": employee.job_id,
            }
        return {"message": "Employee not found"}, 404

    def delete(self, employee_id):
        employee = Employee.query.get(employee_id)
        if employee:
            db.session.delete(employee)
            db.session.commit()
            return {"message": "Employee deleted"}
        return {"message": "Employee not found"}, 404


class EmployeeListResource(Resource):
    def get(self):
        employees = Employee.query.all()
        return [
            {
                "id": employee.id,
                "name": employee.name,
                "department_id": employee.department_id,
                "job_id": employee.job_id,
            }
            for employee in employees
        ]

    def post(self):
        data = request.get_json()
        department = Department.query.get(data["department_id"])
        job = Job.query.get(data["job_id"])
        if not department or not job:
            return
