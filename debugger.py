"""
這是一個名為 debug 的裝飾器，主要目的是協助程式的除錯，它會列印出被裝飾的函數的名稱、
輸入參數和返回結果。這可以讓我們對程式的執行流程有更清晰的了解，
而不需要在程式中加入大量的列印語句。
這種裝飾器在進行程式除錯時非常有用，特別是在處理複雜的程式時。使用這種裝飾器，
你可以很輕鬆地查看各個函數的執行情況，而不必手動在函數中加入大量的列印語句。
"""

# Decorator


def debug(func):
    def wrapper(*args, **kwargs):
        # print the name and arguments of function
        print(f"Calling {func.__name__} with args: {args}, kargs: {kwargs}")
        # call the function
        res = func(*args, **kwargs)
        # print the res
        print(f"{func.__name__} function returned: {res}")
        return res
    return wrapper


# application
@debug
def add_nums(x, y):
    return x + y


add_nums(7, y=2)
