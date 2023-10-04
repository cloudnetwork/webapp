from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
import sqlalchemy
from sqlalchemy.exc import OperationalError  # Import OperationalError
import os

@csrf_exempt
def healthz(request):
    if request.method == 'GET':
        try:
            db_url = os.getenv('DATABASE_URL')
            engine = sqlalchemy.create_engine(db_url)

            # Check the database connection status using SQLAlchemy's ping method
            with engine.connect():
                pass  # If the connection is successful, no exception will be raised

            return JsonResponse({}, status=200, content_type='application/json', headers={'Cache-Control': 'no-cache, no-store, must-revalidate', 'Pragma': 'no-cache'})
        except OperationalError:
            return JsonResponse({}, status=503, content_type='application/json', headers={'Cache-Control': 'no-cache, no-store, must-revalidate', 'Pragma': 'no-cache'})
    else:
        return JsonResponse({"detail": "Method Not Allowed"}, status=405, content_type='application/json', headers={'Cache-Control': 'no-cache, no-store, must-revalidate', 'Pragma': 'no-cache'})
