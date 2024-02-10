from django.urls import path

from . import views

urlpatterns = [
    path("", views.index),
    path("<int:month>", views.monthly_challenge_by_number),
    path(
        "<str:month>",
        views.monthly_challenges,
        name="month-challenge",
        # Refer to a specific URL in your Django code without hardcoding the actual URL. Instead of using the URL string directly in your code, you can use the reverse function along with the name to dynamically generate the URL.
    ),
]
