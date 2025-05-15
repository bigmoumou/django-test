from django.contrib import admin
from django.urls import path
from polls import views as polls_views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', polls_views.home, name='home'),  # 首頁

    path('login/', polls_views.login, name='login'),  # 顯示登入頁面用
    path('verify_login/', polls_views.verify_login, name='verify_login'),  # 登入邏輯用

    path('logout/', polls_views.logout, name='logout'),  # 登出邏輯
]
