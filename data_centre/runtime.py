# -*- coding: utf-8 -*-
import time
import threading

from app import db, logger
from models import Carinfo


class RunTime:
    def __init__(self):
        # 创建数据表
        Carinfo.create_table(True)
        # 系统推出标记
        self.is_quit = False

        self.rest = 100000

    def loop_run(self):
        count = 0
        while 1:
            try:
                if count > 60:
                    db.connect()
                    maxid = self.get_maxid()
                    self.delete(maxid - self.rest)
                    count = 0
                    db.close()
                else:
                    count += 1
            except Exception as e:
                logger.error(e)
                time.sleep(1)
            finally:
                time.sleep(1)
                if self.is_quit:
                    break

    def get_maxid(self):
        c = Carinfo.raw('select max(id) as max from carinfo')
        for i in c:
            return i.max

    def delete(self, id):
        query = Carinfo.delete().where(Carinfo.id < id)
        query.execute()

    def main(self):
        t = threading.Thread(target=self.loop_run, args=())
        t.start()
