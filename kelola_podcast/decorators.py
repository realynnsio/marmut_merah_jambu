from django.http import HttpResponseForbidden

def podcaster_required(view_func):
    def _wrapped_view_func(request, *args, **kwargs):
        if request.session.get('is_podcaster'):
            return view_func(request, *args, **kwargs)
        else:
            return HttpResponseForbidden("You do not have permission to access this page.")
    return _wrapped_view_func