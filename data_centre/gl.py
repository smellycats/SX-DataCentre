# -*- coding: utf-8 -*-
import Queue

# SQL队列
SQLQUE = None
# 全局锁
LOCK = None
# 退出系统
IS_QUIT = False
# memory数据库队列
MEMORYQUE = Queue.Queue()
