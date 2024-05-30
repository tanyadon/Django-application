from django.urls import path

from . import views

app_name = "polls"
urlpatterns = [
    #ДЛЯ ЧАСТИ 1.
    path("", views.index, name="index"),
    # ДЛЯ ЧАСТИ 3.
    #path("<int:question_id>/", views.detail, name="detail"),
    #path("<int:question_id>/results/", views.results, name="results"),
    # ДЛЯ ЧАСТИ 4.
    path("<int:pk>/", views.DetailView.as_view(), name="detail"),
    path("<int:pk>/results/", views.ResultsView.as_view(), name="results"),
    path("<int:question_id>/vote/", views.vote, name="vote"),
]