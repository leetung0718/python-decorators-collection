"""
這是一個名為 exception_handler 的裝飾器，
它的主要目的是為了捕獲並處理被裝飾的函數在執行過程中可能引發的異常。
這種裝飾器在處理可能會引發異常的函數時非常有用。使用這種裝飾器，
你可以在函數級別進行統一的異常處理，而不必在每一個可能引發異常的操作後面
都寫一個 try/except 語句。
"""


def exception_handler(func):
    def wrapper(*args, **kwargs):
        try:
            return func(*args, **kwargs)
        except Exception as e:
            # Handler the exception
            print(f"An exception occurred: {str(e)}")
            # Optionally, perform additional error handling or logging
            # Reraise the exception if needed
    return wrapper

# application

@exception_handler
def divide(x, y):
    result = x / y
    return result


divide(10, 0)  
