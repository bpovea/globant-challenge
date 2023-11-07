from typing import Optional, List, Generator, Union

import pandas as pd

from app.api import models
from app.api.utils import error, open


class CSVRecords:
    def __init__(
        self,
        data_path: str,
        data_type_id: str,
        delimiter: str = "|",
        columns: Optional[List] = None,
    ):
        self.data_path = data_path
        self.data_type_id = data_type_id
        self.delimiter = delimiter
        self.columns = columns

    def generator(self, start_at: int = 0) -> Generator:
        df = self._csv_data_frame()
        if isinstance(df, Exception):
            return df

        records = df.to_dict("records")
        for i, rec in enumerate(records):
            if i < start_at:
                continue
            yield rec

    def _csv_data_frame(self) -> Union[pd.DataFrame, error.FileNotFound]:
        csv_file = open.open_s3(self.data_path)
        try:
            data_type_class = models.index[self.data_type_id]
            dtype = data_type_class.dtype()
            params = {
                "delimiter": self.delimiter,
                "na_values": "",
                "keep_default_na": False,
                "dtype": dtype,
                "header": None,
                "names": dtype.keys(),
            }
            if self.columns:
                params["usecols"] = self.columns
            df = pd.read_csv(csv_file, **params)
            df = df.where(pd.notnull(df), None)
            return df
        except FileNotFoundError:
            return error.FileNotFound(self.data_path)
