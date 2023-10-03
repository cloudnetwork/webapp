from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
import sqlalchemy
import os

@csrf_exempt
def healthz(request):
    if request.method == 'GET':
        try:
            db_url = os.getenv('DATABASE_URL')
            engine = sqlalchemy.create_engine(db_url)
            connection = engine.connect()
            connection.close()
            return JsonResponse({}, status=200, content_type='application/json', headers={'Cache-Control': 'no-cache, no-store, must-revalidate', 'Pragma': 'no-cache'})
        except:
            return JsonResponse({}, status=503, content_type='application/json', headers={'Cache-Control': 'no-cache, no-store, must-revalidate', 'Pragma': 'no-cache'})
    else:
        return JsonResponse({"detail": "Method Not Allowed"}, status=405, content_type='application/json', headers={'Cache-Control': 'no-cache, no-store, must-revalidate', 'Pragma': 'no-cache'})
