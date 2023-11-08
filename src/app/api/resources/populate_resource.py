import logging

from flask import request
from flask_restful import Resource

from app.db import db
from app.api import models
from app.api.utils.stream import CSVRecords
from app.api.utils.iter import chunked_iterable


class PopulateDataResource(Resource):
    def populate_resource(self, file_path, datatype, chunk_size, delimiter):
        stream = CSVRecords(file_path, datatype, delimiter).generator()
        data_type_class = models.index[datatype]
        new_records = 0
        chunk_index = 1
        chunk = []
        for chunk in chunked_iterable(stream, chunk_size):
            if not chunk:
                raise StopIteration
            logging.info(
                f"Loading {datatype} chunk {chunk_index} [{len(chunk)} records]"
            )
            # records = [data_type_class(rec) for rec in chunk]
            records = []
            for rec in chunk:
                existing_record = data_type_class.query.filter_by(id=rec["id"]).first()
                if existing_record:
                    existing_record.on_conflict_do_update(rec)
                    db.session.merge(existing_record)
                else:
                    new_records += 1
                    records.append(data_type_class(**rec))
            db.session.add_all(records)
            db.session.commit()

        return new_records

    def post(self):
        data = request.get_json()
        chunk_size = data.get("chunk_size", 1000)
        delimiter = data.get("delimiter", ",")
        jobs_file_path = data.get("jobs_file_path")
        new_jobs_count = 0
        if jobs_file_path:
            new_jobs_count = self.populate_resource(
                jobs_file_path, "job", chunk_size, delimiter
            )
        departments_file_path = data.get("departments_file_path")
        new_department_count = 0
        if departments_file_path:
            new_department_count = self.populate_resource(
                departments_file_path, "department", chunk_size, delimiter
            )
        employees_file_path = data.get("employees_file_path")
        new_employees_count = 0
        if employees_file_path:
            new_employees_count = self.populate_resource(
                employees_file_path, "employee", chunk_size, delimiter
            )

        return {
            "new_jobs_count": new_jobs_count,
            "new_department_count": new_department_count,
            "new_employees_count": new_employees_count,
        }
