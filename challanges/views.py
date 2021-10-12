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

monthly_title = {
    "january": "January challenge",
    "february": "february challenge",
    "march": "march challenge",
    "april": "april challenge",
    "may": "may challenge",
    "june": "june challenge",
    "july": "july challenge",
    "august": "august challenge",
    "september": "september challenge",
    "october": "october challenge",
    "november": "november challenge",
    "december": "december challenge",
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
        tantangan_text = monthly_title[month]
        # code bellow is how to render a html file
        return render(request, "challenges/challenge.html", {
            "tittle": month.capitalize(),
            "text": challange_text
        })
        # response_data = render_to_string("challenges/challenge.html")
        # return HttpResponsse(response_data)
    except:
        return HttpResponseNotFound("<h1>This month is not supported !</hq>")
    


