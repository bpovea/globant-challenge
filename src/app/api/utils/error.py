class Error(Exception):
    pass


class FileNotFound(Error):
    """
    The stream was expecting a file at `filepath`.
    """

    def __init__(self, file_path: str):
        self.file_path = file_path


class NoDataTypeSpecified(Error):
    """
    The stream was expecting a file at `filepath`.
    """
