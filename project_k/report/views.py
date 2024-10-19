from django.contrib.auth.decorators import login_required
from django.shortcuts import render
from .models import CreateDGU, ReportDGU, ObjectKES, Location
from django.http import HttpResponseRedirect, HttpResponseNotFound, HttpResponse



# получение данных из бд
@login_required
def index(request):
    dgus = CreateDGU.objects.all()
    location = Location.objects.all()
    object_kes = ObjectKES.objects.filter(public=True,)
    return render(request, "index.html", {'dgus': dgus, 'location': location, 'object_kes': object_kes})


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

@login_required
def object_kes(request, id):
    try:
        dgu = CreateDGU.objects.get(id=id)
        if request.method == "POST":
            dgu.name = request.POST.get("name")
            dgu.title = request.POST.get("title")
            dgu.save()
            return HttpResponseRedirect("/")
        else:
            return render(request, "object_kes.html", {"dgu": dgu,})
    except :
        return HttpResponseNotFound("<h2>Product not found</h2>")

@login_required
def dgu_settings(request, id):
    try:
        dgu = CreateDGU.objects.get(id=id)
        if request.method == "POST":
            dgu.narabotka = (False if request.POST.get("narabotka") == None else True)
            dgu.nagruzka = (False if request.POST.get("nagruzka") == None else True)
            dgu.l1 = (False if request.POST.get("l1") == None else True)
            dgu.l2 = (False if request.POST.get("l2") == None else True)
            dgu.l3 = (False if request.POST.get("l3") == None else True)
            dgu.dmasla = (False if request.POST.get("dmasla") == None else True)
            dgu.tog = (False if request.POST.get("tog") == None else True)
            dgu.primechanie = (False if request.POST.get("primechanie") == None else True)

            dgu.save()
            return HttpResponseRedirect("../../")
        else:
            return render(request, "dgu_settings.html", {"dgu": dgu,})
    except :
        return HttpResponseNotFound("<h2>Product not found</h2>")

@login_required
def dgu(request, id):
    try:
        dgu = CreateDGU.objects.get(id=id)
        if request.method == "POST":
            dgu.name = request.POST.get("name")
            dgu.title = request.POST.get("title")
            dgu.save()
            return HttpResponseRedirect("../")
        else:
            return render(request, "dgu.html", {"dgu": dgu,})
    except :
        return HttpResponseNotFound("<h2>Product not found</h2>")