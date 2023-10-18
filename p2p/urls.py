# chat/urls.py

from django.urls import path
from . import views

urlpatterns = [
    path('post-cert/', views.OfferListCreateAPIView.as_view()),
    path('post-answer/', views.AnswerListCreateAPIView.as_view()),
    path('get-answers/<str:host_uuid>/', views.GetAnswers.as_view()),
    path('get-offer/', views.GetOffer.as_view()),

]
