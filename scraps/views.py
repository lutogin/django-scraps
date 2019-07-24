from django.shortcuts import render, get_object_or_404
from scraps import models


def index(req):
    return render(req, 'index.html')


def get_info(req):
    t = req.GET['t'] or 'php'
    content = models.Content.objects.filter(technology__link_name=t).values()

    return render(req, 'info_page.html', context={'content': content})
