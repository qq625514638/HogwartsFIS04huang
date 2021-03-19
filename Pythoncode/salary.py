#存入工资
import money  #引入money模块，如果不引入，就不能使用该模块代码

def money1(salary,op):  #定义方法salary,op
    money.operation = op   #赋值给money模块的operation变量
    if money.operation:    #判断money模块的operation变量是否转账成功，如果符合条件就执行if
        money.saved_money = money.saved_money + salary  #把money模块的saved_money的变量与salary参数相加赋给money类的saved_money变量
        print(money.saved_money)    #打印出money模块的saved_money变量
    else:                  #否则执行else，打印出正在转账中
        print("正在转账中")



if __name__ == '__main__':    #入口，方便调用
    money1(1000,True)
