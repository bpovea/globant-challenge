from app.db import db


class Department(db.Model):
    __tablename__ = "departments"
    __table_args__ = {"schema": "challenge_data"}

    id = db.Column(db.Integer, primary_key=True)
    department = db.Column(db.String(100), nullable=False)

    def __init__(self, id, department):
        self.id = id
        self.department = department

    def on_conflict_do_update(self, rec):
        self.department = rec["department"]

    @staticmethod
    def dtype():
        return {
            "id": int,
            "department": str,
        }
