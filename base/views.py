from django.shortcuts import render

from activity.models import Action

# Create your views here.


def home(request):
    actions = Action.objects.all()[:5]
    return render(request, "home.html", {"actions": actions})
