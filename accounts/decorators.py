from django.shortcuts import redirect


def unauthenticated_only(view):
    def wrapper_function(request, *args, **kwargs):
        if request.user.is_authenticated:
            return redirect('/')
        else:
            return view(request, *args, **kwargs)

    return wrapper_function