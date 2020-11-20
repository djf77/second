# utils.py
# 自定义错误
class HttpError(Exception):
    def __init__(self, status, mag):
        super().__init__()
        self.status_code = status
        self.message = mag

    def show(self):
        return {
            'status_code': self.status_code,
            'message': self.message
        }


