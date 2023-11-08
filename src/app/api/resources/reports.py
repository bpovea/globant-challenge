import csv
from flask import request
from flask_restful import Resource
import pandas as pd

from app.db import db
from app.api.utils import write


class EmployeesHiredByJob(Resource):
    def get(self):
        data = request.get_json()
        output_path = data["output_path"]
        chunksize = data["chunk_size"]
        year = data["year"]
        sql_engine = db.get_engine()
        conn = sql_engine.connect()
        run_query = f"""
            SELECT
                d.department  AS department,
                j.job AS job,
                EXTRACT(quarter FROM e.hire_datetime) AS quarter,
                COUNT(e.id) AS employee_count
            FROM
                challenge_data.employees AS e
            JOIN
                challenge_data.departments AS d ON e.department_id = d.id
            JOIN
                challenge_data.jobs AS j ON e.job_id = j.id
            WHERE
                EXTRACT(year FROM e.hire_datetime) = {year}
            GROUP BY
                d.department, j.job, EXTRACT(quarter FROM e.hire_datetime)
            ORDER BY
                department, job
        """
        record_count = 0
        df_chunks = pd.read_sql(run_query, conn, chunksize=chunksize)
        for chunk in df_chunks:
            chunked_df = pd.DataFrame(chunk)
            df_pivoted = chunked_df.pivot(
                index=["department", "job"], columns="quarter", values="employee_count"
            ).reset_index()
            df_pivoted.columns = ["Department", "Job", "Q1", "Q2", "Q3", "Q4"]

            # ensure first time open in write mode (replace file if exist) and header True
            if record_count == 0:
                mode = "w"
                need_header = True
            else:
                mode = "a"
                need_header = False

            kwargs = {
                "mode": mode,
                "header": need_header,
                "quoting": csv.QUOTE_MINIMAL,
                "index": False,
            }
            record_count += write.df_to_csv(df_pivoted, output_path, **kwargs)

        return {
            "output_path": output_path,
            "record_count": record_count,
        }


class EmployeesHiredByDepartment(Resource):
    def get(self):
        data = request.get_json()
        output_path = data["output_path"]
        chunksize = data["chunk_size"]
        year = data["year"]
        sql_engine = db.get_engine()
        conn = sql_engine.connect()
        run_query = f"""
            SELECT
                d.id AS department_id,
                d.department  AS department,
                COUNT(e.id) AS employee_count
            FROM
                challenge_data.employees AS e
            JOIN
                challenge_data.departments AS d ON e.department_id = d.id
            WHERE
                EXTRACT(year FROM e.hire_datetime) = {year}
            GROUP BY
                d.id, d.department
            ORDER BY
                employee_count DESC
        """
        record_count = 0
        df_chunks = pd.read_sql(run_query, conn, chunksize=chunksize)
        for chunk in df_chunks:
            chunked_df = pd.DataFrame(chunk)
            chunked_df.columns = ["id", "Department", "Hired"]

            # ensure first time open in write mode (replace file if exist) and header True
            if record_count == 0:
                mode = "w"
                need_header = True
            else:
                mode = "a"
                need_header = False

            kwargs = {
                "mode": mode,
                "header": need_header,
                "quoting": csv.QUOTE_MINIMAL,
                "index": False,
            }
            record_count += write.df_to_csv(chunked_df, output_path, **kwargs)

        return {
            "output_path": output_path,
            "record_count": record_count,
        }
