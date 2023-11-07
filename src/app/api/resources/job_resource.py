from flask import request
from flask_restful import Resource

from app.db import db
from app.api.models import Job


class JobResource(Resource):
    def get(self, job_id):
        job = Job.query.get(job_id)
        if job:
            return {"id": job.id, "job": job.job}
        return {"message": "Job not found"}, 404

    def put(self, job_id):
        job = Job.query.get(job_id)
        if job:
            data = request.get_json()
            job.job = data["job"]
            db.session.commit()
            return {"id": job.id, "job": job.job}
        return {"message": "Job not found"}, 404

    def delete(self, job_id):
        job = Job.query.get(job_id)
        if job:
            db.session.delete(job)
            db.session.commit()
            return {"message": "Job deleted"}
        return {"message": "Job not found"}, 404


class JobListResource(Resource):
    def get(self):
        jobs = Job.query.all()
        return [{"id": job.id, "job": job.job} for job in jobs]

    def post(self):
        data = request.get_json()
        job = Job(job=data["job"])
        db.session.add(job)
        db.session.commit()
        return {"id": job.id, "job": job.job}, 201
