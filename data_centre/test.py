from psutil_func import disk_state, disk_human
from models import Users, Carinfo
from runtime import RunTime

def disk_test():
    print disk_state()
    print disk_human()

def model_test():
    #Users.create_table(True)
    db.create_all()

def create_table():
    Carinfo.create_table(True)
    Carinfo.create(passtime=123,
                   ip='127.0.0.1', place=2,
                   content='{"passtime":45}')
    c = Carinfo.select()
    print c

def fine_one():
    Users.dirty_fields

def max_test():
    rt = RunTime()
    #rt.get_maxid()
    r = rt.get_carinfo(1)
    print r
    del rt

if __name__ == '__main__':
    #model_test()
    #disk_test()
    #create_table()
    max_test()
