from django.urls import path
from . import views

urlpatterns = [
    path('home1/',views.home1,name='home1' ),
    path('logout/',views.logout,name='logout'),

    path('category/',views.category,name='category' ),
    path('disablecat/<int:id>',views.disablecat,name='disablecat' ),
    path('enablecat/<int:id>',views.enablecat,name='enablecat' ),

    path('district/',views.district,name='district' ),
    path('disabledistrict/<int:id>',views.disabledistrict,name='disabledistrict' ),
    path('enabledistrict/<int:id>',views.enabledistrict,name='enabledistrict' ),

    path('place/',views.place,name='place' ),
    path('disablePlaces/<int:id>',views.disablePlaces,name='disablePlaces' ),
    path('enablePlaces/<int:id>',views.enablePlaces,name='enablePlaces' ),

    path('addPackage/',views.addPackage,name='addPackage' ),
    path('geteditPackage/',views.geteditPackage,name='geteditPackage' ),
    path('editstock/',views.editstock,name='editstock' ),
    path('gettitles/',views.gettitles,name='gettitles'),
    path('updatePackage/',views.updatePackage,name='updatePackage'),

    path('latestorders',views.latestorders,name='latestorders'),
    path('enableusers',views.enableusers,name='enableusers'),
    path('enableUser/<int:id>',views.enableUser,name='enableUser'),
    path('viewusers',views.viewusers,name='viewusers')

]