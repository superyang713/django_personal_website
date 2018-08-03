from django.shortcuts import render


def pressure_monitor(request):
    return render(request, 'lab/pressure_monitor.html')
