from django.http import HttpResponse, JsonResponse
from django.apps import apps
from server.exception import PSException

_app_config = apps.get_app_config("server")

# Create your views here.
def privacy_check(request, user=None):
    try:
        print("Get an request")
        file = request.FILES['file']
        _app_config.threads.privado_scan(user, file)
        return HttpResponse("OK")
    except PSException as e:
        return JsonResponse({
            "error": e.err, "detail": e.detail
        }, status=400)
    except Exception as e:
        return JsonResponse({
            "error": "Uncaught Exception", "detail": str(e)
        }, status=400)

            