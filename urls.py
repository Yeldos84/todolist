from django.urls import path, re_path, include
from . import views
from .views import TodoUserView
from django.contrib.auth.views import LoginView, LogoutView, PasswordChangeView, PasswordChangeDoneView, PasswordResetView, PasswordResetDoneView

urlpatterns = [
    # ex: /todolist/
    # Стартовая страница
    path("", views.TodoViewCreate.as_view(), name="todo"),
    path("pdf/", views.some_view, name="some_view"),
    path("users/", views.TodoUserView.as_view(), name="users"),
    path("succes/", views.TodoLoginView.as_view(), name="succes"),
    path("succes_login/", views.succes_login, name="succes_login"),
    path("404/", views.notfound, name="404"),
    path("delete/", views.tododelete, name="delete"),
    path("show/", views.TodoShow.as_view(), name="show"),
    path("base/", views.render_base_template, name="base"),
    path("showallusers/", views.TodoShowAllUsers.as_view(), name="showallusers"),
    path("showaoneuser/<int:id>", views.show_one_user, name="showaoneuser"),
    path("captcha/", views.Captcha.as_view(), name="captcha"),
    path("nav/", views.render_navbar, name="nav"),
    path("search/", views.search, name="search"),

    #URL с помощью регулярных выражений
    re_path(r'^info/about', views.about, name="about"),
    # начало должно быть info/about
    re_path(r'^info/[A-Z]{2}/', views.lang, name="lang"),
    # начало должно быть info/ и заканчиваться на две заглавные латин буквы KZ
    re_path(r'^info$', views.info, name="info"),
    # начало и конец должно быть info
    re_path(r'^contact/\d+', views.contact, name="contact"),
    # после contact принимает только цифры


    #Authenticated urls - LoginView
    path("login/", LoginView.as_view(template_name = 'todolist/login.html'), name="login"),
    path("logout/", LogoutView.as_view(), name="logout"),
    path("login_ok/", views.render_login_ok, name="login_ok"),
    path("change_password/", PasswordChangeView.as_view(template_name='todolist/change_password.html',
                                                        success_url='/todolist/change_password_done'), name="change_password"),
    path("change_password_done/", PasswordChangeDoneView.as_view(template_name='todolist/password_changechange_done.html'), name="change_password_done"),
    path("password_reset/", PasswordResetView.as_view(template_name='todolist/password_reset.html',
                                                      success_url='/todolist/password_reset_done'), name="password_reset"),
    path("password_reset_done/", PasswordResetDoneView.as_view(template_name='todolist/password_reset_done.html',
                                                      ), name="password_reset_done"),
    path('google', views.google, name='google'),

]