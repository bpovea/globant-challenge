from app.db import db


class Job(db.Model):
    __tablename__ = "jobs"
    __table_args__ = {"schema": "challenge_data"}

    id = db.Column(db.Integer, primary_key=True)
    job = db.Column(db.String(100), nullable=False)

    def __init__(self, id, job):
        self.id = id
        self.job = job

    def on_conflict_do_update(self, rec):
        self.job = rec["job"]

    @staticmethod
    def dtype():
        return {
            "id": int,
            "job": str,
        }
