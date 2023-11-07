import pandas as pd

from app.db import db
from app.api.models import Job, Department


class Employee(db.Model):
    __tablename__ = "employees"
    __table_args__ = {"schema": "challenge_data"}

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    hire_datetime = db.Column(db.DateTime(timezone=True), nullable=True)
    department_id = db.Column(db.Integer, db.ForeignKey(Department.id), nullable=False)
    job_id = db.Column(db.Integer, db.ForeignKey(Job.id), nullable=False)

    def __init__(self, id, name, hire_datetime, department_id, job_id):
        self.id = id
        self.name = name
        self.department_id = department_id
        self.hire_datetime = hire_datetime
        self.job_id = job_id

    def on_conflict_do_update(self, rec):
        self.name = rec["name"]
        self.hire_datetime = rec["hire_datetime"]
        self.department_id = rec["department_id"]
        self.job_id = rec["job_id"]

    @staticmethod
    def dtype():
        return {
            "id": int,
            "name": str,
            "hire_datetime": str,
            "department_id": pd.Int64Dtype(),
            "job_id": pd.Int64Dtype(),
        }
