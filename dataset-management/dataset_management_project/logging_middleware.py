import os
import uuid
import threading
from django.utils.deprecation import MiddlewareMixin

def _get_request_id(request):
    rid = request.headers.get("X-Correlation-Id") or request.META.get("HTTP_X_CORRELATION_ID")
    return rid or str(uuid.uuid4())

class RequestLoggingMiddleware(MiddlewareMixin):
    def process_request(self, request):
        request.request_id = _get_request_id(request)
        request.user_id = getattr(request.user, "id", None)
        ctx = {
            "request_id": request.request_id,
            "user_id": request.user_id,
            "service": os.getenv("SERVICE_NAME"),
            "env": os.getenv("ENV"),
            "path": request.path,
            "method": request.method,
        }
        threading.current_thread().request_context = ctx

    def process_response(self, request, response):
        try:
            response["X-Correlation-Id"] = request.request_id
        except Exception:
            pass
        return response