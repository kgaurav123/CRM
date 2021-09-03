
from django.http import HttpResponse
from django.shortcuts import redirect


def allowed_users(allowed_roles=[]):
    def decorator(view_func):
        def wrapper_func(request, *args, **kwargs):

            group = None
            if request.user.groups.exists():
                group = request.user.groups.all()[0].name
                print(group)

            if group in allowed_roles:
                return view_func(request, *args, **kwargs)

            else:
                return HttpResponse("You are not authorized person")

        return wrapper_func

    return decorator


def admin_only(view_func):
    def wrapper_func(request, *args, **kwargs):
        group = None
        if request.user.groups.exists():
            group = request.user.groups.all()[0].name
            #group == admin
            #groip == customer

        if group == "admin":
            return view_func(request, *args, **kwargs)

        elif group == "customer":
            return redirect("user_page")

    return wrapper_func
