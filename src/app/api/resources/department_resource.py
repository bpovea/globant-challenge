from flask import request
from flask_restful import Resource

from app.db import db
from app.api.models import Department


class DepartmentResource(Resource):
    def get(self, department_id):
        department = Department.query.get(department_id)
        if department:
            return {"id": department.id, "department": department.department}
        return {"message": "Department not found"}, 404

    def put(self, department_id):
        department = Department.query.get(department_id)
        if department:
            data = request.get_json()
            department.department = data["department"]
            db.session.commit()
            return {"id": department.id, "department": department.department}
        return {"message": "Department not found"}, 404

    def delete(self, department_id):
        department = Department.query.get(department_id)
        if department:
            db.session.delete(department)
            db.session.commit()
            return {"message": "Department deleted"}
        return {"message": "Department not found"}, 404


class DepartmentListResource(Resource):
    def get(self):
        departments = Department.query.all()
        return [
            {"id": department.id, "department": department.department}
            for department in departments
        ]

    def post(self):
        data = request.get_json()
        department = Department(department=data["department"])
        db.session.add(department)
        db.session.commit()
        return {"id": department.id, "department": department.department}, 201
