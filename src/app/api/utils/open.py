import os
import _io
from typing import Optional

import boto3
import smart_open


def open_s3(
    filepath: str,
    permissions: str = "rb",
    client: Optional[boto3.resources.base.ServiceResource] = None,
) -> _io.TextIOWrapper:
    if not client:
        client = boto3.client(
            "s3",
            endpoint_url=os.environ["AWS_ENDPOINT"],
            aws_access_key_id=os.environ["ACCESS_KEY"],
            aws_secret_access_key=os.environ["SECRET_KEY"],
            region_name="us-east-1",
        )
    params = {"client": client}
    return smart_open.open(filepath, permissions, transport_params=params)
