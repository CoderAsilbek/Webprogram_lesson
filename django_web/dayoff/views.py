from django.shortcuts import render

# Create your views here.
from datetime import datetime

def dayoff(request):
    now = datetime.now()
    weakday= now.strftime("%A")
    if weakday == "Saturday" or weakday == "Sunday":
        return render(request, "dayoff/main.html", {"status": "dayoff"})
    else:
        return render(request, "dayoff/main.html", {"status": "No dayoff"})
    