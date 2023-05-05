from django.conf import settings
from django.utils import timezone
from django.http import Http404
from django.middleware.csrf import CsrfViewMiddleware

class CorsMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        response = self.get_response(request)
        response["Access-Control-Allow-Origin"] = "https://asanodeme.net"
        response["Access-Control-Allow-Methods"] = "GET, POST, PUT, DELETE, OPTIONS"
        response["Access-Control-Allow-Headers"] = "X-Requested-With, Content-Type, Accept, Origin, Authorization"
        return response

class DisableCSRFMiddleware(CsrfViewMiddleware):
    def process_view(self, request, callback, callback_args, callback_kwargs):
        if request.path.startswith('/admin/'):
            return None
        return super().process_view(request, callback, callback_args, callback_kwargs)
class VisitCountMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        # Check if the session already contains a visit count
        visit_count = request.session.get('visit_count', 0)
        
        # Increment the visit count and update the session
        request.session['visit_count'] = visit_count + 1/20
        
        # Update the last visit timestamp
        request.session['last_visit'] = str(timezone.now())

        response = self.get_response(request)
        return response
class BanIPMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        banned_ips = ['2a09:bac2:456:126e::1d6:115']  # Replace with the IP address you want to ban
        if request.META['REMOTE_ADDR'] in banned_ips:
            raise Http404('Page not found')
        response = self.get_response(request)
        return response
