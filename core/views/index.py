from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
from ..report import report
from django.http import HttpResponse
from django.http import HttpResponseRedirect


@csrf_exempt
def index(request):
    return render(request, 'index.html')


def download(request):
    date = request.GET.get('date').split('/')
    day = date[0]
    month = date[1]
    year = date[2]
    file = report.Report('test', day, month, year)
    file = file.report_maker()
    response = HttpResponse(content_type='application/vnd.openxmlformats-officedocument.wordprocessingml.document')
    file_name = 'test'
    response['Content-Disposition'] = 'attachment; filename=%s' % file_name
    file.save(response)
    return response
