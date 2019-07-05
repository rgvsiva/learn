
from calc_module import *

print('hello :',__name__)
#special variable  (__name__)
#where the code start first (__name__==__main__
def fun():
    print(add(3,4))
    print('fun')
def fun1():
    print('fun1')
def main():
    fun()
    fun1()

main()