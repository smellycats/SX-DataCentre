from psutil_func import disk_state, disk_human
from models import Users, Carinfo

def disk_test():
    print disk_state()
    print disk_human()

def model_test():
    Users.create_table(True)
    Carinfo.create_table(True)

if __name__ == '__main__':
    #model_test()
    disk_test()
