import datetime

from pathlib import Path

from board.settings import BASE_DIR


class LoggerMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        request_datetime = datetime.datetime.now().strftime('%d.%m.%Y - %H:%M:%S')
        request_url = request.path
        request_method = request.method
        log_string = f'{request_datetime} - {request_method} - {request_url}\n'
        with open(Path(BASE_DIR, 'logs.log'), 'a') as log_file:
            log_file.write(log_string)

        response = self.get_response(request)

        return response


