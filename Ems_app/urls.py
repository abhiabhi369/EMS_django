from django.urls import path
from Ems_app.views import (Home,Signup, Login, Check, VotersCreate,VillageIssues,
                           FavourToView, CasteFilter)

urlpatterns = [
    path('home/',Home.as_view(),name='Home'),
    path('signup/',Signup.as_view(),name='Signup'),
    path('login/',Login.as_view(),name='Login'),
    path('check/',Check.as_view(),name='Check'),
    path('voters/',VotersCreate.as_view(),name='Voters'),
    path('issues/',VillageIssues.as_view(),name='Issues'),
    path('favour/',FavourToView.as_view(),name='Favour'),
    path('caste/',CasteFilter.as_view(),name='Caste')
]
