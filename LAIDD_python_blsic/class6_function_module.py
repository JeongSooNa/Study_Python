# module for class6_function

def sum_function(x,y):
    return x+y
if __name__ == "__main__":
    print(sum_function(1,2))
    # 여기서 실행하면 출력되지만 다른 file에서 import하면 false가 되어 출력되지 않는다.
    # 따로 module안의 다른 method를 사용해 main에서 print 해야 함.