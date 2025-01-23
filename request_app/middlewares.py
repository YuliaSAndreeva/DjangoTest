from datetime import time
import time
from django.conf import settings
from django.db.models.fields import return_None
from django.http import HttpRequest, HttpResponseForbidden


def set_useragent_middleware(get_response):

    print('Запуск middleware')

    def middleware(request: HttpRequest):
        print('До запроса')
        request.user_agent = request.META[('HTTP_USER_AGENT')]
        response = get_response(request)
        print('После запроса')
        return response

    return middleware

class CountRequestMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response
        self.requests_count = 0
        self.response_count = 0
        self.exceptions_count = 0

    def __call__(self, request: HttpRequest):
        self.requests_count += 1
        print('Количество запросов = ', self.requests_count)
        response = self.get_response(request)
        self.response_count += 1
        print('Количество ответов = ', self.response_count)
        return response

    def process_exception(self, request: HttpRequest, exception: Exception):
        self.exceptions_count += 1
        print('Получили', self.exceptions_count, 'ошибок')


class ThrottlingMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response
        self.request_timestamps = {}
        self.request_limits = getattr(settings, 'THROTTLING_LIMITS', {
            'default': {
                'rate': 60,
                'seconds': 60,
            },
        })
    def process_request(self, request: HttpRequest):
        user_ip = request.META.get('REMOTE_ADDR')
        current_timestamp = time.time()

        rate = self.get_rate_limit(request)

        if user_ip in self.request_timestamps:
            timestamp = self.request_timestamps[user_ip]
            timestamp = [ts for ts in timestamp if current_timestamp - ts < rate['seconds']]
            self.request_timestamps[user_ip] = timestamp

            if len(timestamp) >= rate['rate']:
                remaining_time = rate['seconds'] - (current_timestamp - timestamp[0])
                return HttpResponseForbidden(f"Слишком много запросов. Пожалуйста, подождите {remaining_time:.2f} секунд.")
        else:
            self.request_timestamps[user_ip] = []
        self.request_timestamps[user_ip].append(current_timestamp)



        #     last_timestamp = self.request_timestamps[user_ip]
        #     time_diff = current_timestamp - last_timestamp
        #
        #     if time_diff < (rate['seconds']/rate['rate']):
        #         remaining_time = (rate['seconds']/rate['rate']) - time_diff
        #         return HttpResponseForbidden(f"Слишком много запросов. Пожалуйста, подождите {remaining_time} секунд.")
        # self.request_timestamps[user_ip] = current_timestamp
        return None

    def get_rate_limit(self, request):
        for path, rate in self.request_limits.items():
            if request.path.startswith(path):
                return rate
        return self.request_limits['default']

    def __call__(self, request: HttpRequest):
        response = self.process_request(request)
        if response:
            return response
        response = self.get_response(request)
        return response
