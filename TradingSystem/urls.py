from django.contrib import admin
from django.urls import path

import system.views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', system.views.index),
    path('logout', system.views.logout, name='logout'),
    path('validate', system.views.validate, name='validate'),
    path('searchStock', system.views.searchStock, name='searchStock'),
    path('dashboard_page', system.views.dashboard_page, name='dashboard_page'),
    path('portfolio_page', system.views.portfolio_page, name='portfolio_page'),
    path('analytics_page', system.views.analytics_page, name='analytics_page'),
    path('platform_page', system.views.platform_page, name='platform_page'),
    path('trades_page', system.views.trades_page, name='trades_page'),
    path('search_page', system.views.search_page, name='search_page'),
]
