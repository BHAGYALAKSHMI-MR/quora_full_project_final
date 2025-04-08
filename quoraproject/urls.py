from django.contrib import admin
from django.urls import path
from quoraapp import views
from django.contrib.auth import views as auth_views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.home, name='home'),
    path('ask/', views.ask_question, name='ask_question'),
    path('question/<int:pk>/', views.question_detail, name='question_detail'),
    path('question/<int:question_id>/like/', views.like_question, name='like_question'),
    path('answer/<int:answer_id>/like/', views.like_answer, name='like_answer'),
    path('signup/', views.signup_view, name='signup'),
    path('login/', auth_views.LoginView.as_view(template_name='login.html'), name='login'),
    path('logout/', views.custom_logout, name='logout'),
    path('question/<int:question_id>/like/', views.like_question, name='like_question'),
    path('question/<int:pk>/delete/', views.delete_question, name='delete_question'),


]
