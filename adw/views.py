from django.shortcuts import render
from django.http.response import HttpResponse
from django.http.request import HttpRequest
from adw.models import Form
from django.views import View


class Index(View):
    def get(self, request: HttpRequest) -> HttpResponse:
        return render(request, 'main.html')

    def post(self, request: HttpRequest) -> HttpResponse:
        desc = request.POST['descriptions']
        d = Form.objects.get_or_create(descriptions={"descriptions": desc})
        return render(request, 'main.html')


class Output(View):
    def get(self, request: HttpRequest) -> HttpResponse:
        items = Form.objects.all()
        return render(request, 'secondary.html', {'items': items})
