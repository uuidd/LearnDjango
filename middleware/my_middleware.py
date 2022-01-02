from django.utils.deprecation import MiddlewareMixin


class MyMW(MiddlewareMixin):
    def process_request(self, request):
        print('MyMW process_request do ---')

    def process_view(self, request, callback, callback_args, callback_kwargs):
        print('MyMW process_view do ---')

    def process_response(self, request, response):
        print('MyMW process_response do ---')
        return response
