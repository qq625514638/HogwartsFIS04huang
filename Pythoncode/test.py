import salary    #引入salary模块，如果不引入，就不能使用该模块代码
import query     #引入query模块
if __name__ == '__main__':   #入口，封装用，其他模块不可调用
    query.queryMoney()       #调用query模块的queryMoney查询方法
    salary.money1(1000,False)   #调用salary模块的money1的增加方法
    salary.money1(1000,True)    #调用salary模块的money1的增加方法