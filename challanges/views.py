from django.shortcuts import render
from django.http import HttpResponse, HttpResponseNotFound, HttpResponseRedirect
from django.urls import reverse

monthly_challanges = {
    "january": "Eat no meat for entire month",
    "february": "walk 20 minute at least every day",
    "march": "walk 20 minute at least every day",
    "april": "drakor",
    "may": "warnet",
    "june": "latihan coding",
    "july": "jalan-jalan",
    "august": "makan mie",
    "september": "makan bakso",
    "october": "ke toko vape",
    "november": "beli pakan ikan",
    "december": "maen ke warnet",

}

# Create your views here.

def index(request):
    list_items = ""
    months = list(monthly_challanges.keys())

    for month in months:
        capitalize_month = month.capitalize()
        month_path = reverse("month-challenge", args=[month])
        list_items += f"<li><a href=\"{month_path}\">{capitalize_month}</a></li>"

        response_data = f"<ul>{list_items}</ul>"
    return HttpResponse(response_data)

def monthly_challange_by_number(request, month):
    months = list(monthly_challanges.keys())

    if month > len(months):
        return HttpResponseNotFound("invalid month")

    redirect_month = months[month - 1 ]
    redirect_path = reverse("month-challenge", args=[redirect_month]) # /challenge/january -> itu yang akan di redirect
    return HttpResponseRedirect(redirect_path)

# def january(request):
#     return HttpResponse("Eat no meat for entire month")

# def february(request):
#     return HttpResponse("walk 20 minute at least every day")

#dynamic url for call in browser 
def monthly_challange(request, month):
    try:
        challange_text = monthly_challanges[month]
        response_data = f"<h1>{challange_text}</h1>"
        return HttpResponse(response_data)
    except:
        return HttpResponseNotFound("<h1>This month is not supported !</hq>")
    


