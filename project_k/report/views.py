from datetime import date
from django.contrib.auth.decorators import login_required
from django.shortcuts import render

from .models import CreateDGU, ReportDGU, ObjectKES, Location
from django.http import HttpResponseRedirect, HttpResponseNotFound, HttpResponse



@login_required
def index(request):
    dgus = CreateDGU.objects.all()
    location = Location.objects.all()
    object_kes = ObjectKES.objects.filter(public=True,)
    return render(request, "index.html", {'dgus': dgus, 'location': location, 'object_kes': object_kes})

@login_required
def create_report(request, id):
    def chec_zpt(text):
        return text.replace(',', '.') if ',' in text else text


    try:
        dgu_name = CreateDGU.objects.get(id=id)
        name = dgu_name.name
        lct = dgu_name.location.id
        alter = dgu_name.alternator.hours_alternator

        if request.method == "POST":
            report = ReportDGU()
            report.dgu_id = id
            report.author = request.user
            report.narabotka = chec_zpt(request.POST.get("narabotka"))
            dgu_name.alternator.hours_alternator = chec_zpt(request.POST.get("narabotka"))
            dgu_name.alternator.save(update_fields=["hours_alternator"])
            dgu_name.dvs.engine_hours = chec_zpt(request.POST.get("narabotka"))
            dgu_name.dvs.save(update_fields=["engine_hours"])
            report.nagruzka = request.POST.get("nagruzka")
            report.active = request.POST.get("active")
            report.reactive = request.POST.get("reactive")
            report.full_load = request.POST.get("full_load")
            report.l1 = request.POST.get("l1")
            report.l2 = request.POST.get("l2")
            report.l3 = request.POST.get("l3")
            report.dmasla = chec_zpt(request.POST.get("dmasla"))
            report.tc = chec_zpt(request.POST.get("tc"))
            report.akb = chec_zpt(request.POST.get("akb"))
            report.title = request.POST.get("title")
            report.save()
            return HttpResponseRedirect(f"/area/{lct}")
        else:
            return render(request, "create_report.html", {
                "name": name, 'lct': lct, "dgu_name": dgu_name, "alter": alter,})
    except:
        return HttpResponseNotFound("<h2>Product not found</h2>")

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
    dgus = CreateDGU.objects.all()
    location = Location.objects.filter(object_kes=id)
    object_kes = ObjectKES.objects.get(id=id)
    return render(request, "object_kes.html", {'dgus': dgus,
                                               'location': location, 'object_kes': object_kes})

@login_required
def area(request, id):
    y, m, d = (int(i) for i in date.today().isoformat().split("-"))
    dgus = CreateDGU.objects.filter(location=id)
    location = Location.objects.get(id=id)
    object_kes = Location.objects.get(id=id).object_kes.name
    report = ReportDGU.objects.filter(time_create__date=date(y, m, d), dgu__location__id=id)
    rpt = set(i.dgu.name for i in report)
    return render(request, "area.html",
                  {'dgus': dgus, 'location': location, 'object_kes': object_kes,
                   'report': report, 'rpt': rpt})

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