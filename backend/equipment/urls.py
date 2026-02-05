from django.urls import path
from .views import summary_api, upload_csv_api, history_api
from .views import generate_pdf_report

urlpatterns = [
    path('summary/', summary_api),
    path('upload/', upload_csv_api),
    path('history/', history_api),
    path('report/', generate_pdf_report),
]
