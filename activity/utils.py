from django.contrib.contenttypes.models import ContentType
from .models import Action


def create_action(user, verb, target):
    action = Action(user=user, verb=verb, target=target)
    action.save()
    print(action)
