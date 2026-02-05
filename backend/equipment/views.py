from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from django.conf import settings
import os

from .csv_utils import calculate_summary
from .models import UploadHistory


# test summary API
def summary_api(request):
    file_path = "data/sample_equipment_data.csv"
    result = calculate_summary(file_path)
    return JsonResponse(result)


# upload API
@csrf_exempt
def upload_csv_api(request):
    if request.method == 'POST' and request.FILES.get('file'):
        uploaded_file = request.FILES['file']

        file_path = os.path.join(settings.BASE_DIR, uploaded_file.name)

        with open(file_path, 'wb+') as destination:
            for chunk in uploaded_file.chunks():
                destination.write(chunk)

        result = calculate_summary(file_path)

        # save upload history
        UploadHistory.objects.create(
            file_name=uploaded_file.name,
            total_count=result["total_count"],
            avg_flowrate=result["avg_flowrate"],
            avg_pressure=result["avg_pressure"],
            avg_temperature=result["avg_temperature"],
        )

        # keep only last 5 records
        if UploadHistory.objects.count() > 5:
            oldest = UploadHistory.objects.order_by('upload_time').first()
            oldest.delete()

        return JsonResponse(result)

    return JsonResponse({"error": "No file uploaded"}, status=400)

from .models import UploadHistory


def history_api(request):
    records = UploadHistory.objects.order_by('-upload_time')[:5]

    data = []
    for r in records:
        data.append({
            "file_name": r.file_name,
            "upload_time": r.upload_time,
            "total_count": r.total_count,
            "avg_flowrate": r.avg_flowrate,
            "avg_pressure": r.avg_pressure,
            "avg_temperature": r.avg_temperature,
        })

    return JsonResponse(data, safe=False)
from reportlab.pdfgen import canvas
from django.http import HttpResponse


def generate_pdf_report(request):
    latest = UploadHistory.objects.order_by('-upload_time').first()

    if not latest:
        return JsonResponse({"error": "No history available"}, status=400)

    response = HttpResponse(content_type='application/pdf')
    response['Content-Disposition'] = 'attachment; filename="report.pdf"'

    p = canvas.Canvas(response)

    p.drawString(100, 800, "Equipment Data Report")
    p.drawString(100, 770, f"File Name: {latest.file_name}")
    p.drawString(100, 740, f"Total Count: {latest.total_count}")
    p.drawString(100, 710, f"Avg Flowrate: {latest.avg_flowrate}")
    p.drawString(100, 680, f"Avg Pressure: {latest.avg_pressure}")
    p.drawString(100, 650, f"Avg Temperature: {latest.avg_temperature}")

    p.showPage()
    p.save()

    return response


