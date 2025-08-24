
# exception.py
import sys
import logging

class MyException(Exception):
    def __init__(self, message: str, error_detail: sys):
        super().__init__(message)
        self.message = message
        self.error_detail = error_detail

    def __str__(self):
        return self._get_detailed_error_message()

    def _get_detailed_error_message(self) -> str:
        _, _, exc_tb = self.error_detail.exc_info()
        if exc_tb:
            filename = exc_tb.tb_frame.f_code.co_filename
            line_number = exc_tb.tb_lineno
            return f"Error occurred in file: {filename}, line: {line_number}, message: {self.message}"
        return self.message


# Helper function to raise a detailed exception
def raise_detailed_exception(e: Exception):
    logging.error(f"Exception occurred: {str(e)}")
    raise MyException(str(e), sys)
