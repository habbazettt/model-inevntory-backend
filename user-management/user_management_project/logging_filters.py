import logging
import threading

class RequestContextFilter(logging.Filter):
    def filter(self, record):
        ctx = getattr(threading.current_thread(), "request_context", {})
        record.request_id = ctx.get("request_id")
        record.user_id = ctx.get("user_id")
        record.service = ctx.get("service")
        record.env = ctx.get("env")
        return True