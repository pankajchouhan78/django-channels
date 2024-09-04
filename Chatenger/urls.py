from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('chat/',include('chatapp.urls'), name="chat"),
    path('accounts/', include('accounts.urls')),
    path('blog/', include('blogapp.urls')),
    path('gameee/', include('tic_tac_toe.urls')),
]
