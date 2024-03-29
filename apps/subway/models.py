from django.db import models

from shanghai_subway_backend.settings import station_lng_diff, station_lat_diff, running_lng_diff, running_lat_diff


class Station(models.Model):
    class Meta:
        db_table = 'tb_station'
        verbose_name = '站点'
        verbose_name_plural = '站点数据管理'

    id = models.AutoField(primary_key=True, auto_created=True, verbose_name='编号')
    name = models.CharField(max_length=50, verbose_name='名称')
    longitude = models.FloatField(verbose_name='经度')
    latitude = models.FloatField(verbose_name='纬度')
    line_name = models.CharField(max_length=50, verbose_name='线路名称')

    def __str__(self):
        return self.name

    def to_dict(self):
        return {
            'id': self.id,
            'name': self.name,
            'longitude': self.longitude,
            'latitude': self.latitude,
            'line_name': self.line_name,
            'position': {
                'lng': self.longitude + station_lng_diff,
                'lat': self.latitude + station_lat_diff
            }
        }


class RunningData(models.Model):
    class Meta:
        db_table = 'tb_running_data'
        verbose_name = '运行数据'
        verbose_name_plural = '运行数据管理'

    id = models.AutoField(primary_key=True, auto_created=True, verbose_name='编号')
    alias = models.CharField(max_length=50, verbose_name='车厢号')
    line_name = models.CharField(max_length=50, verbose_name='线路名称')
    timestamp = models.DateTimeField(verbose_name='时间戳')
    write_time = models.DateTimeField(verbose_name='写入时间')
    longitude = models.FloatField(verbose_name='经度')
    latitude = models.FloatField(verbose_name='纬度')
    station_from = models.CharField(max_length=50, verbose_name='出发站')
    station_to = models.CharField(max_length=50, verbose_name='到达站')
    direction = models.CharField(max_length=50, verbose_name='方向')
    departure = models.CharField(max_length=50, verbose_name='发车时间')
    status = models.CharField(max_length=50, verbose_name='状态', default='', null=True, blank=True)
    speed = models.FloatField(verbose_name='速度')

    def __str__(self):
        return self.alias

    def to_dict(self):
        return {
            'id': self.id,
            'alias': self.alias,
            'line_name': self.line_name,
            'timestamp': self.timestamp,
            'write_time': self.write_time,
            'longitude': self.longitude,
            'latitude': self.latitude,
            'station_from': self.station_from,
            'station_to': self.station_to,
            'direction': self.direction,
            'departure': self.departure,
            'status': self.status,
            'speed': self.speed,
            'position': {
                'lng': self.longitude + running_lng_diff,
                'lat': self.latitude + running_lat_diff
            }
        }


class IteData(models.Model):
    class Meta:
        db_table = 'tb_ite_data'
        verbose_name = 'ite数据'
        verbose_name_plural = 'ite数据管理'

    id = models.AutoField(primary_key=True, auto_created=True, verbose_name='编号')
    alias = models.CharField(max_length=50, verbose_name='车厢号')
    timestamp = models.DateTimeField(verbose_name='时间戳')
    write_time = models.DateTimeField(verbose_name='写入时间')
    wifi_time = models.DateTimeField(verbose_name='wifi时间')
    freq = models.IntegerField(verbose_name='频率')
    gain = models.IntegerField(verbose_name='增益')
    nummeasurements = models.IntegerField(verbose_name='测量次数')
    fn = models.IntegerField(verbose_name='fn', null=True, blank=True)
    m_type = models.CharField(max_length=50, verbose_name='m_type')
    frequencyid = models.IntegerField(verbose_name='frequencyid', null=True, blank=True)
    timeoffset = models.IntegerField(verbose_name='timeoffset')
    cellid = models.IntegerField(verbose_name='cellid')
    cfo = models.FloatField(verbose_name='cfo', null=True, blank=True)
    rssi = models.FloatField(verbose_name='总功率')
    rsrp = models.FloatField(verbose_name='信号强度')
    cir = models.FloatField(verbose_name='cir', null=True, blank=True)
    rfGain = models.FloatField(verbose_name='rfGain', null=True, blank=True)
    agc_cnt = models.IntegerField(verbose_name='agc_cnt')
    agc_mean_power = models.FloatField(verbose_name='agc_mean_power')
    mode = models.CharField(max_length=50, verbose_name='mode')
    idx_5ms = models.IntegerField(verbose_name='idx_5ms')
    pss_timing = models.IntegerField(verbose_name='pss_timing')
    freq_offset = models.FloatField(verbose_name='freq_offset')
    sinr = models.FloatField(verbose_name='信噪比')
    rsrq = models.FloatField(verbose_name='信号质量')
    gps_time = models.DateTimeField(verbose_name='gps_time', null=True, blank=True)
    longitude = models.FloatField(verbose_name='经度')
    latitude = models.FloatField(verbose_name='纬度')
    ros_time = models.DateTimeField(verbose_name='ros_time', null=True, blank=True)
    cnt = models.IntegerField(verbose_name='cnt')
    trans_time = models.DateTimeField(verbose_name='trans_time')

    def __str__(self):
        return self.alias

    def to_dict(self):
        return {
            'id': self.id,
            'alias': self.alias,
            'timestamp': self.timestamp,
            'write_time': self.write_time,
            'wifi_time': self.wifi_time,
            'freq': self.freq,
            'gain': self.gain,
            'nummeasurements': self.nummeasurements,
            'fn': self.fn,
            'm_type': self.m_type,
            'frequencyid': self.frequencyid,
            'timeoffset': self.timeoffset,
            'cellid': self.cellid,
            'cfo': self.cfo,
            'rssi': self.rssi,
            'rsrp': self.rsrp,
            'cir': self.cir,
            'rfGain': self.rfGain,
            'agc_cnt': self.agc_cnt,
            'agc_mean_power': self.agc_mean_power,
            'mode': self.mode,
            'idx_5ms': self.idx_5ms,
            'pss_timing': self.pss_timing,
            'freq_offset': self.freq_offset,
            'sinr': self.sinr,
            'rsrq': self.rsrq,
            'gps_time': self.gps_time,
            'longitude': self.longitude,
            'latitude': self.latitude,
            'ros_time': self.ros_time,
            'cnt': self.cnt,
            'trans_time': self.trans_time,
            'type': 'B' if self.freq > 1800000000 else 'A'
        }


class WifiData(models.Model):
    class Meta:
        db_table = 'tb_wifi_data'
        verbose_name = 'wifi数据'
        verbose_name_plural = 'wifi数据管理'

    id = models.AutoField(primary_key=True, auto_created=True, verbose_name='编号')
    alias = models.CharField(max_length=50, verbose_name='车厢号')
    timestamp = models.DateTimeField(verbose_name='时间戳')
    write_time = models.DateTimeField(verbose_name='写入时间')
    wifi_time = models.DateTimeField(verbose_name='wifi时间')
    mac = models.CharField(max_length=50, verbose_name='mac')
    channel = models.IntegerField(verbose_name='channel')
    channel2 = models.CharField(max_length=50, verbose_name='channel2')
    ssid = models.CharField(max_length=50, verbose_name='ssid')
    freq = models.IntegerField(verbose_name='freq')
    level = models.IntegerField(verbose_name='level')
    longitude = models.FloatField(verbose_name='经度')
    latitude = models.FloatField(verbose_name='纬度')
    ros_time = models.DateTimeField(verbose_name='ros_time', null=True, blank=True)
    cnt = models.IntegerField(verbose_name='cnt', null=True, blank=True)
    trans_time = models.DateTimeField(verbose_name='trans_time', null=True, blank=True)

    def __str__(self):
        return self.alias

    def to_dict(self):
        return {
            'id': self.id,
            'alias': self.alias,
            'timestamp': self.timestamp,
            'write_time': self.write_time,
            'wifi_time': self.wifi_time,
            'mac': self.mac,
            'channel': self.channel,
            'channel2': self.channel2,
            'ssid': self.ssid,
            'freq': self.freq,
            'level': self.level,
            'longitude': self.longitude,
            'latitude': self.latitude,
            'ros_time': self.ros_time,
            'cnt': self.cnt,
            'trans_time': self.trans_time
        }


class SpectrumData(models.Model):
    class Meta:
        db_table = 'tb_spectrum_data'
        verbose_name = '光谱数据'
        verbose_name_plural = '光谱数据管理'

    id = models.AutoField(primary_key=True, auto_created=True, verbose_name='编号')
    alias = models.CharField(max_length=50, verbose_name='车厢号')
    timestamp = models.DateTimeField(verbose_name='时间戳')
    write_time = models.DateTimeField(verbose_name='写入时间')
    freq = models.IntegerField(verbose_name='频率')
    gain = models.IntegerField(verbose_name='增益', null=True, blank=True)
    red = models.IntegerField(verbose_name='红色', null=True, blank=True)
    blue = models.IntegerField(verbose_name='蓝色', null=True, blank=True)
    bin = models.IntegerField(verbose_name='bin')
    fft = models.IntegerField(verbose_name='fft', null=True, blank=True)
    channel = models.IntegerField(verbose_name='channel', null=True, blank=True)
    wifi_time = models.DateTimeField(verbose_name='wifi时间')
    gps_time = models.DateTimeField(verbose_name='gps时间')
    longitude = models.FloatField(verbose_name='经度')
    latitude = models.FloatField(verbose_name='纬度')
    rssi = models.IntegerField(verbose_name='rssi')
    normal_alarm_state = models.IntegerField(verbose_name='正常报警状态')
    strong_alarm_state = models.IntegerField(verbose_name='强报警状态')
    ros_time = models.DateTimeField(verbose_name='ros_time', null=True, blank=True)
    cnt = models.IntegerField(verbose_name='cnt', null=True, blank=True)
    trans_time = models.DateTimeField(verbose_name='trans_time', null=True, blank=True)

    def __str__(self):
        return self.alias

    def to_dict(self):
        return {
            'id': self.id,
            'alias': self.alias,
            'timestamp': self.timestamp,
            'write_time': self.write_time,
            'freq': self.freq,
            'gain': self.gain,
            'red': self.red,
            'blue': self.blue,
            'bin': self.bin,
            'fft': self.fft,
            'channel': self.channel,
            'wifi_time': self.wifi_time,
            'gps_time': self.gps_time,
            'longitude': self.longitude,
            'latitude': self.latitude,
            'rssi': self.rssi,
            'normal_alarm_state': self.normal_alarm_state,
            'strong_alarm_state': self.strong_alarm_state,
            'ros_time': self.ros_time,
            'cnt': self.cnt,
            'trans_time': self.trans_time
        }

