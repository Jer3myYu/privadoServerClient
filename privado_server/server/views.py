import os

from django.http import HttpResponse, JsonResponse, FileResponse
from django.apps import apps
from server.exception import PSException

_app_config = apps.get_app_config("server")

# Create your views here.
def privacy_check(request, user=None):
    try:
        print("Get an request")
        file = request.FILES['file']

        # handle uploaded file
        raw_file_path = "/home/ubuntu/project/storage/" + str(file)
        with open(raw_file_path, "wb+") as destination:
            for chunk in file.chunks():
                destination.write(chunk)

        _app_config.threads.privado_scan(user, file)
        return HttpResponse("OK")
    except PSException as e:
        return JsonResponse({
            "error": e.err, "detail": e.detail
        }, status=400)
    except Exception as e:
        return JsonResponse({
            "error": "Uncaught Exception", "detail": str(e)
        }, status=500)

def get_privacy_scan_result(request, user, filename):
    result_path = "/home/ubuntu/project/storage/{}/{}/.privado/privado.json".format(user, filename[:-4])
    if not os.path.exists(result_path):
        return JsonResponse({
            "msg": "the file is not ready"
        }, status=202)
    return FileResponse(
        open(result_path, 'rb'), as_attachment=True, filename="privado.json"
    )

