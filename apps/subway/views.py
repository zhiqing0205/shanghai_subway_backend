from django.shortcuts import render
from django.http import JsonResponse
from .models import Station, RunningData, WifiData, IteData


def get_all_data(request):
    stations = [station.to_dict() for station in Station.objects.all()]
    running_data = [running_data.to_dict() for running_data in RunningData.objects.all()]
    wifi_data = [wifi_data.to_dict() for wifi_data in WifiData.objects.all()]
    ite_data = [ite_data.to_dict() for ite_data in IteData.objects.all()]

    return JsonResponse({
        'stations': stations,
        'running_data': running_data,
        'wifi_data': wifi_data,
        'ite_data': ite_data,
        'message': 'success'
    })
