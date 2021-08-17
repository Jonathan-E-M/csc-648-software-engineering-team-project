from django.urls import path
from django.urls import include
from django.contrib.auth import views as auth_views
from . import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('', views.landing),
    path('homepage', views.homepage, name='homepage'),
    path('index/', views.index, name='index'),
    path('index/', include([
        path('khyo/', views.khyo, name='khyo'),
        path('david/', views.david, name='david'),
        path('darnell/', views.darnell, name='darnell'),
        path('brian/', views.brian, name='brian'),
        path('jonathan/', views.jonathan, name='jonathan'),
        path('srushti/', views.srushti, name='srushti'),
    ])),

    path('logSite/', views.logSite, name='logSite'),
    path('logSite/', include([
        path('sept10/', views.sept10, name='sept10'),
        path('sept12/', views.sept12, name='sept12'),
        path('sept16/', views.sept16, name='sept16'),
        path('sept19/', views.sept19, name='sept19'),
        path('sept23/', views.sept23, name='sept23'),
    ])),

    path('signup/', views.signup, name='signup'),
    path('signin/', auth_views.LoginView.as_view(template_name='users/signin.html'), name='signin'),
    path('signout/', auth_views.LogoutView.as_view(template_name='users/signout.html'), name='signout'),
    path('landing/', views.landing, name='landing'),
    path('food/', views.food, name='food'),
    path('search/', views.search, name='search'),
    path('about/', views.about, name='about'),
    path('invitations/', views.invitations, name='invitations'),
    path('group/', views.group, name='group'),
    path('membershome/', views.membershome, name='membershome'),
    path('removemember/', views.removemember, name='removemember'),
    path('leaveFridge/', views.leaveFridge, name='leaveFridge'),
    path('inviteMember/', views.inviteMember, name='inviteMember'),
    path('mygrouplist/', views.mygrouplist, name='mygrouplist'),
    path('grouplist/', views.grouplist, name='grouplist'),
    path('addListItem/', views.addListItem, name='addListItem'),
    path('removeListItem/', views.removeListItem, name='removeListItem'),
    path('editListItem/', views.editListItem, name='editListItem'),
    path('recipe/', views.recipe, name='recipe'),
    path('addListItemFromRecipe/', views.addListItemFromRecipe, name='addListItemFromRecipe'),
    path('recipeGroup/', views.recipeGroup, name='recipeGroup'), 
    path('receipt/', views.receipt, name='receipt'),
    path('imageSave/', views.imageSave, name='imageSave'),
    path('inventory/', views.inventory, name='inventory'),
    
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

     
