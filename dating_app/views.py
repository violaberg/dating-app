from django.shortcuts import render
from django.core.exceptions import PermissionDenied


def error_404(request, exception):
    '''
    Renders 404 page
    '''
    return render(request, 'error_pages/404.html', status=404)


def error_500(request):
    '''
    Renders 500 page
    '''
    return render(request, 'error_pages/500.html', status=500)


def error_403(request, exception):
    '''
    Renders 403 page
    '''
    if isinstance(exception, PermissionDenied):
        return render(request, 'error_pages/403.html', status=403)
    else:
        return render(request, 'error_pages/500.html', status=500)
