def start_finish(func):
    def wrapper(*args, **kwargs):
        print("Start")
        result=func(*args, **kwargs)
        print("Finish")
        return result
    return wrapper

@start_finish
def inititate_start_finish(a,b):
    return a + b

print(inititate_start_finish(3,5))