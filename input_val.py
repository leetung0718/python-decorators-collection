"""
這是一個名為 validate_input 的裝飾器工廠，它的主要目的是為了讓被裝飾的函數在執行前
對其輸入參數進行驗證。裝飾器會根據提供的驗證函數 validations（一組可調用的物件）來進行驗證。
每一個驗證函數都應該接收一個參數並返回一個布林值，表示該參數是否符合驗證條件。
如果任何參數未通過驗證，裝飾器會引發一個 ValueError 異常。
這種裝飾器在處理需要進行輸入驗證的函數時非常有用。使用這種裝飾器，
你可以保證你的函數只會接收到符合特定條件的參數，
避免因不合規的輸入數據而產生錯誤或不可預期的行為。"""


def validate_input(*validations):
    def decorator(func):
        def wrapper(*args, **kwargs):
            for i, val in enumerate(args):
                if i < len(validations):
                    if not validations[i](val):
                        raise ValueError(f"Invalid argument: {val}")
            for key, val in kwargs.items():
                if key in validations[len(args):]:
                    if not validations[len(args):][key](val):
                        raise ValueError(f"Invalid argument: {key}={val}")
            return func(*args, **kwargs)
        return wrapper
    return decorator


# application


def is_int(value):
    return isinstance(value, int)


@validate_input(is_int)
def square(n):
    return n ** 2


square(2.2)
