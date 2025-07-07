from django.urls import path
from chatapp import views as chat_views
from django.contrib.auth.views import LoginView, LogoutView

urlpatterns = [
    path("", chat_views.home, name="home"),
    path("join-room/", chat_views.joinRoom, name="join-room"),
    path("create-room/", chat_views.createRoom, name="create-room"),
    path("chat/<str:room_name>/", chat_views.chatPage, name="chat-page"),

    path("login/", LoginView.as_view(template_name="chat/login.html"), name="login-user"),
    path("logout/", LogoutView.as_view(next_page='login-user'), name="logout-user"),
]