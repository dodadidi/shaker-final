from django.urls import path
from . import views
from django.conf.urls.static import static
from django.conf import settings
from projects import views



urlpatterns = [
    path('', views.home, name='projects-home'),
    #path('about/', views.about, name='project-about'),
    path('homepage/',views.homepage, name="homepage"),
    path('register/',views.registerForm, name="register"),
    path('logout/', views.logoutuser, name='logoutuser'),
    path('Login/', views.loginuser, name='loginuser'),

    #crud

    path('myprojects/',views.myprojects, name="my-projects"),
    path('createNewProject/', views.createNewProject, name='createNewProject'),
    path('project/<int:project_pk>', views.updateproject, name='updateproject'),        
    path('project/<int:project_pk>/delete', views.deleteproject, name='deleteproject'),
    path('project/<int:project_pk>/done', views.doneproject, name='doneproject'),
    path('project/<int:project_pk>/about', views.projectabout, name='project-about'),        

    path('allprojects/',views.allProjects, name="all-projects"),    
    #path('assigntome/<int:project_pk>', views.assigntome, name='assigntome'),
]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)