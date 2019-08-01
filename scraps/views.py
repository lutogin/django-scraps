from django.shortcuts import render, get_object_or_404
from scraps import models


def index(req):
    technologies = models.Technology.objects.all().values()

    return render(req, 'index.html', context={'technologies': technologies})


def get_info(req):
    technologies = models.Technology.objects.all().values()
    select_tech = req.GET['t'] or 'python'
    content = models.Content.objects.filter(technology__link_name=select_tech).values()

    return render(req, 'info_page.html', context={'content': content, 'technologies': technologies})
