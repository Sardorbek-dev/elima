import datetime

def export_vars(request):
    return {
        'TEMPLATE_STATIC_VERSION': f"{datetime.datetime.now()}"
    }