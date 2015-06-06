# -*- encoding: utf-8 -*-
import ConfigParser


class MyIni:

    def __init__(self, confpath='datacentre.conf'):
        self.cf = ConfigParser.ConfigParser()
        self.cf.read(confpath)

    def __del__(self):
        del self.cf

    def get_sys_conf(self):
        """获取系统配置参数"""
        sysconf = {}
        sysconf['threads'] = self.cf.getint('SYSSET', 'threads')
        sysconf['port'] = self.cf.getint('SYSSET', 'port')
        sysconf['selfip'] = self.cf.get('SYSSET', 'selfip')

        return sysconf

    def get_ser_centre_conf(self):
        """获取中心服务参数"""
        sysconf = {}
        sysconf['ip'] = self.cf.get('SERCENTRE', 'ip')

        return sysconf
