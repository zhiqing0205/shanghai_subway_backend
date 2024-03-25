from django.contrib import admin
from .models import Station, RunningData, IteData, WifiData


class StationAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'longitude', 'latitude', 'line_name')
    search_fields = ('id', 'name', 'line_name')
    list_filter = ('line_name',)
    ordering = ('id',)
    list_editable = ('longitude', 'latitude')


class RunningDataAdmin(admin.ModelAdmin):
    list_display = (
    'id', 'alias', 'line_name', 'timestamp', 'write_time', 'longitude', 'latitude', 'station_from', 'station_to',
    'direction', 'departure', 'status', 'speed')
    search_fields = list_display
    list_filter = ('line_name', 'status', 'station_from', 'station_to', 'direction', 'departure', 'status')
    ordering = ('id',)


class IteDataAdmin(admin.ModelAdmin):
    list_display = ('id', 'alias', 'timestamp', 'freq', 'cellid', 'rssi', 'rsrp', 'sinr', 'rsrq')
    search_fields = list_display
    ordering = ('id',)


class WifiDataAdmin(admin.ModelAdmin):
    list_display = ('id', 'alias', 'timestamp', 'mac', 'ssid', 'freq', 'level')
    search_fields = list_display
    ordering = ('id',)


admin.site.register(Station, StationAdmin)
admin.site.register(RunningData, RunningDataAdmin)
admin.site.register(IteData, IteDataAdmin)
admin.site.register(WifiData, WifiDataAdmin)
