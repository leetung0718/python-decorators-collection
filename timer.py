"""
這是一個稱為 timer 的裝飾器，它的主要功能是計算被裝飾的函數的執行時間。
這種裝飾器在分析並優化程式碼的效能時十分有用。只需要用 '@' 符號將這個裝飾器應用到目標函數上即可。
"""
import time


# Sample Functions
def train_model():
    print("Training...")
    time.sleep(3)
    print("Done!")


def val_model():
    print("Validation...")
    time.sleep(3)
    print("Done!")


# 1. Without decorator
start_time = time.time()
train_model()
end_time = time.time()
print(f"Used time: {end_time - start_time}s")

start_time = time.time()
val_model()
end_time = time.time()
print(f"Used time: {end_time - start_time}s")

print("-"*30)

# 2. With decorator


def timer(func):
    def wrapper(*arg, **kwargs):
        # start the timer
        start_time = time.time()
        # call the decorated function
        func(*arg, **kwargs)
        # remeasure the time
        end_time = time.time()
        # compute the elaspsed time and print it
        print(f"Used time: {end_time - start_time} seconds")
        return
    return wrapper


@timer
def train_model():
    print("Training...")
    time.sleep(3)
    print("Done!")


@timer
def val_model():
    print("Validation...")
    time.sleep(3)
    print("Done!")


train_model()
val_model()
