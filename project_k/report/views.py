from django.contrib.auth.decorators import login_required
from django.shortcuts import render
from .models import CreateDGU, ReportDGU
from django.http import HttpResponseRedirect, HttpResponseNotFound


# получение данных из бд
@login_required
def index(request):
    dgus = CreateDGU.objects.all()
    report_dgu = ReportDGU.objects.all()
    return render(request, "index.html", {'dgus': dgus, 'report_dgu': report_dgu, })


@login_required
def create_report(request, id):
    dgu_name = CreateDGU.objects.get(id=id)
    name = dgu_name.name
    # если запрос POST, сохраняем данные
    if request.method == "POST":
        report = ReportDGU()
        report.dgu_id = id
        report.title = request.POST.get("title")
        report.tc = request.POST.get("tc")
        report.author = request.user
        report.save()
        return HttpResponseRedirect("/")

    return render(request, "create_report.html", {'name_dgu': name,} )

@login_required
def create_dgu(request):
    # если запрос POST, сохраняем данные
    if request.method == "POST":
        dgu = CreateDGU()
        dgu.name = request.POST.get("name")
        dgu.title = request.POST.get("title")
        dgu.save()
        return HttpResponseRedirect("/")
    return render(request, "create_dgu.html", )

@login_required
def edit_dgu(request, id):
    try:
        dgu = CreateDGU.objects.get(id=id)
        if request.method == "POST":
            dgu.name = request.POST.get("name")
            dgu.title = request.POST.get("title")
            dgu.save()
            return HttpResponseRedirect("/")
        else:
            return render(request, "edit_dgu.html", {"dgu": dgu,})
    except :
        return HttpResponseNotFound("<h2>Product not found</h2>")


@login_required
def delete_dgu(request, id):
    try:
        dgu = CreateDGU.objects.get(id=id)
        dgu.delete()
        return HttpResponseRedirect("/")
    except:
        return HttpResponseNotFound("<h2>Product not found</h2>")
