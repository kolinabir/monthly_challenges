from django.http import HttpResponse, HttpResponseNotFound, HttpResponseRedirect
from django.urls import reverse
from django.shortcuts import render
from django.template.loader import render_to_string

# Create your views here.
monthly_challenges_dict = {
    "january": "winter! Shut up",
    "february": "Why dont you just break one finger bro?",
    "march": "Shut up again for a month!",
    "april": "Ohh! You are still alive?",
    "may": "What about a month of silence?",
    "june": "How about a month of no internet?",
    "july": "How about a month of no ?",
    "august": "How about a month of no internet?",
    "september": "How about a month of no internet?",
    "october": "How about a month of no internet?",
    "november": "How about a month of no internet?",
    "december": None,
}  # type: ignore


def index(request):
    months = list(monthly_challenges_dict.keys())

    return render(request, "challenges/index.html", {"months": months})


def monthly_challenge_by_number(request, month):
    """
    Redirects the user to the challenge page corresponding to the given month number.
    Args:
        request (HttpRequest): The HTTP request object.
        month (int): The month number.

    Returns:
        HttpResponseRedirect: A redirect response to the challenge page.

    """
    # Get the list of months from the dictionary keys
    months = list(monthly_challenges_dict.keys())
    if month > len(months):
        return HttpResponseNotFound("Invalid month")
    # Calculate the index of the redirect month based on the given month number
    redirect_month = months[month - 1]
    redirect_path = reverse(
        "month-challenge",
        args=[redirect_month],
    )
    # # Redirect the user to the challenge page for the redirect month
    return HttpResponseRedirect(redirect_path)


def monthly_challenges(request, month):  
    try:
        challenge_text = monthly_challenges_dict[month]
        return render(
            request,
            "challenges/challenge.html",
            {"text": challenge_text, "month_name": month},
        )

    except:
        response_data = render_to_string("404.html")
        return HttpResponseNotFound(response_data)
