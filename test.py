# -*- coding: utf-8 -*-

import threading
import time

from data_centre import app, RunTime, gl
from data_centre import debug_logging


def run_test():
    debug_logging('log\datacentre.log')
    rt = RunTime()
    rt.main()
    app.run(host='0.0.0.0', port=8089, threaded=True)

    rt.is_quit = True
    del rt

def run_test2():
    debug_logging('log\datacentre.log')
    rt = RunTime()
    t = threading.Thread(target=rt.loop_run, args=())
    t.start()
    time.sleep(30)
    rt.is_quit = True
    del rt

def run_test3():
    debug_logging('log\datacentre.log')
    rt = RunTime()
    rt.main()
    time.sleep(20)
    rt.is_quit = True
    del rt

def run_test4():
    debug_logging('log\datacentre.log')

    app.run(host='0.0.0.0', port=8089, threaded=True)
    gl.IS_QUIT = True
    #t.is_quit = True
    #del rt

def max_test():
    rt = RunTime()
    #print rt.get_maxid()
    #rt.delete(-1000)
    rt.loop_run()
    #r = rt.get_carinfo(1)
    #print r.id
    del rt

if __name__ == "__main__":
    #run_test3()
    #run_test2()
    #run_test4()
    max_test()




