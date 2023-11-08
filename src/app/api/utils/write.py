import os

import pandas as pd


def df_to_csv(
    df: pd.DataFrame,
    output_file_path: str,
    delimiter: str = ",",
    quotechar: str = '"',
    **kwargs,
) -> None:
    kwargs["storage_options"] = {
        "client_kwargs": {
            "endpoint_url": os.environ["AWS_ENDPOINT"],
        },
    }
    df.to_csv(output_file_path, sep=delimiter, quotechar=quotechar, **kwargs)
    return df.shape[0]
