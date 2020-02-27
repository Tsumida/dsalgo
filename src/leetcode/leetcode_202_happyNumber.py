# 2018-11-1

def isHappyNum(x, count):
    print(f"{count} - {x}")
    if x == 1:
        return True
    elif x == 0:
        return False
    elif count <=0 :
        return False
    else :
        next_num = 0
        count -= 1
        while x > 0:
            next_num += (x % 10) **2
            x = x // 10
        x = next_num
        # print(x)
        if count > 0:
            return isHappyNum(x, count)
        else :
            return False

def next_num(x):
    next_num = 0
    while x > 0:
            next_num += (x % 10) **2
            x = x // 10
    return next_num

if __name__ == "__main__":
    # 最多循环20次
    # isHappyNum(6, 100)
    x = list(range(1, 100))
    y = [next_num(num) for num in x]

    print(x)
    print(y)
