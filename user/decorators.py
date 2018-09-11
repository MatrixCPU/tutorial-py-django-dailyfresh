# -*- encoding: utf-8 -*-
from django.http import HttpResponseRedirect
from django.urls import reverse


def login_required(func):
    def wrapper(request, *args, **kwargs):
        if request.session.has_key('user_id'):
            return func(request, *args, **kwargs)
        else:
            resp = HttpResponseRedirect(reverse('user:login'))
            # save referrer for later use
            resp.set_cookie('url', request.get_full_path())
            return resp

    return wrapper
