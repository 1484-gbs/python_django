from django.shortcuts import render

from syncapp.models import SyncEmployee


# Create your views here.
def test():
    SyncEmployee.execute()
