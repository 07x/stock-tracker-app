from django.urls import path
from .views import stockPicker,stockTracker

urlpatterns = [
    path('',stockPicker,name="stock-picker"),
    path('stocktracker/',stockTracker,name="stock-tracker"),



]
