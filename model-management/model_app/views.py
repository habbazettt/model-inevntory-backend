import logging
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

logger = logging.getLogger(__name__)

class HealthView(APIView):
    permission_classes = []
    authentication_classes = []

    def get(self, request):
        logger.info("Healthcheck OK")
        return Response({"status": "ok", "service": "model-management"}, status=status.HTTP_200_OK)