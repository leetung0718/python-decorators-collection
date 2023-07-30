"""
這是一個名為 retry 的裝飾器工廠，它的主要目的是為了讓被裝飾的函數具有自動重試的功能。
如果裝飾的函數在執行過程中引發異常，該裝飾器會讓函數重新執行，
直到達到最大嘗試次數 max_attempts。如果每次嘗試後都失敗，它將等待 delay 秒再次嘗試。
這種裝飾器在處理網絡請求或者其他可能會暫時失敗的操作時非常有用。使用這種裝飾器，
你可以讓你的程式在這些操作失敗時自動重試，而不是立即給用戶報告一個錯誤。
"""

import random
import time


def retry(max_attempts, delay=1):
    def decorator(func):
        def wrapper(*args, **kwargs):
            attempts = 0
            while attempts < max_attempts:
                try:
                    return func(*args, **kwargs)
                except Exception as e:
                    attempts += 1
                    print(f"Attempt {attempts} failed: {e}")
                    time.sleep(delay)
            print(f"Function failed after {max_attempts} attempts")
        return wrapper
    return decorator


# application
@retry(max_attempts=5, delay=2)
def unstable_function():
    if random.random() < 0.9:  # 90% chance to raise an error
        raise ValueError("Random failure!")
    else:
        return "Success!"


result = unstable_function()
print(result)
