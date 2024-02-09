from django.shortcuts import render
from django.http import HttpResponse, HttpResponseNotFound

# Create your views here.


def monthly_challenges(request, month):
    challenge_text = None
    if month == "january":
        challenge_text = "ohhh winter! Shut up"
    elif month == "february":
        challenge_text = "Why dont you just break one finger bro?"
    elif month == "march":
        challenge_text = "Shut up again for a month!"
    else:
        return HttpResponseNotFound("Not supported!")
    return HttpResponse(challenge_text)
