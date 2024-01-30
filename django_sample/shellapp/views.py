from django.shortcuts import render
from shellapp.models import OriginEmployee


# Create your views here.
def test():
    # python manage.py shell
    print("call from shell")
    OriginEmployee.transfer()
    return
