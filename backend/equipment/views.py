from django.shortcuts import render
from django.http import JsonResponse
from .csv_utils import calculate_summary


def summary_api(request):
  
    file_path = "data/sample_equipment_data.csv"  
    result = calculate_summary(file_path)

    return JsonResponse(result)
