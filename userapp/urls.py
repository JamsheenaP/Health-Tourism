from django.urls import path
from . import views

urlpatterns = [
    path('',views.index,name='index'),
    path('index2',views.index2,name='index2'),
    path('index3',views.index2,name='index3'),
    path('login/',views.login,name='login' ),
    path('profile/',views.profile,name='profile' ),
    path('editprofile/',views.editprofile,name='editprofile' ),
    path('profile2/',views.profile2,name='profile2' ),
    path('editprofile2/',views.editprofile2,name='editprofile2' ),
    path('register/', views.register, name='register'),
    path('cat_packages/<int:id>',views.cat_packages,name='cat_packages'),
    path('bestpackage/<int:id>', views.bestpackage2, name='bestpackage2'),
    path('cat_packages2/<int:id>', views.cat_packages2, name='cat_packages2'),
    path('bestpackage2/<int:id>', views.bestpackage, name='bestpackage'),
    path('payment/<int:id>',views.payment,name='payment'),
    path('logout/',views.logout,name='logout'),
    path('vieworders',views.vieworders,name='vieworders'),
    path('cancelorder/<int:id>',views.cancelorder,name='cancelorder')
]