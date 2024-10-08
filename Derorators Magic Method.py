# class Decorator():
#     def __init__(self, func):
#         self.func = func
#
#
#     def __call__(self, *args, **kwargs):
#         print('До вызова')
#         result = self.func(*args, **kwargs)
#         print('После вызова')
#         return result
#
# @Decorator
# def func(name):
#     print('Привет')
#
#
# func('Артём')
#
#
# class CallCounter():
#     def __init__(self, func):
#         self.func = func
#         self.count = 0
#
#
#     def __call__(self, *args, **kwargs):
#         self.count += 1
#         print(f'Функция была вызвана {self.count} раз')
#         return  self.func(*args, **kwargs)
#
#
# @CallCounter
# def func(name):
#     print('Привет', name)
#
#
# func('Саша')
# func('Петя')
# func('Сёма')
#
# def log(func):
#     def wrapper(self, *args, **kwargs):
#         print(f'Вызван метод {func.__name__} из класса {self.__class__.__name__}')
#         return func(self, *args, **kwargs)
#     return wrapper
#
#
# class MyClass():
#     @log
#     def hello(self, name):
#         print(f'hello, {name}')
#
#
# obj = MyClass()
# obj.hello('Mike')






# import json
# import time
# import os
# from functools import wraps
# class CacheDecorator():
#     def __init__(self, file='cache.json',
#                  max_size=10, expire_time=60):
#         self.file = file
#         self.max_size = max_size
#         self.expire_time = expire_time
#         self.cache = self.load_cache()
#
#
#     def load_cache(self):
#         if os.path.exists(self.file):
#             with open(self.file, 'r') as f:
#                 return json.load(f)
#         return {}
#
#
#     def save_cache(self):
#         with open(self.file, 'w') as f:
#             json.dump(self.cache, f)
#
#
#     def clear_expired(self):
#         cur_time = time.time()
#         to_delete_keys = []
#         for key, value in self.cache.items():
#             if cur_time - value['time'] > self.expire_time:
#                     to_delete_keys.append(key)
#
#         for key in to_delete_keys:
#             del self.cache[key]
#
#         self.save_cache()
#
#
#     def __call__(self, func):
#         @wraps(func)
#         def wrapper(*args):
#             self.clear_expired()
#             key = json.dumps(args)
#             if key in self.cache:
#                 print('возвращаем кэшированый результат для', args)
#                 return self.cache[key]['result']
#
#
#             result = func(*args)
#             self.cache[key] = {'result': result, 'time': time.time()}
#             if len(self.cache) > self.max_size:
#                 old_key = min(self.cache, key=lambda k: self.cache[k]['time'])
#                 del self.cache[old_key]
#
#
#             self.save_cache()
#             return result
#         return wrapper
#
#
# @CacheDecorator(file='cache.json', max_size=4, expire_time=10)
# def func(x, y):
#     return x + y
#
#
# result1 = func(5, 8)
# print(result1)
#
# result1 = func(5, 8)
#
#
#
# result2 = func(3, 9)
# print(result2)
#
# resul2 = func(3, 9)
#
#
#
# result2 = func(6, 8)
# print(result2)
#
# resul2 = func(6, 8)






# import time
# import os
# import json
# from functools import wraps
#
# class Timing():
#     def __init__(self, porog=1.0, file='timing.json'):
#         self.porog = porog
#         self.file = file
#         self.results = []
#
#     def __call__(self, func):
#         @wraps(func)
#         def wrapper(*args, **kwargs):
#             start_time = time.time()
#             result = func(*args, **kwargs)
#             end_time = time.time()
#             different_time = end_time - start_time
#             print(f'Время выполнения {func.__name__}: {different_time}')
#
#
#             if different_time > self.porog:
#                 print(f'Внимание! Функция {func.__name__} выполняется дольше {self.porog} секунд!')
#
#
#             self.results.append({
#                 'function': func.__name__,
#                 'time': different_time,
#                 'args': args,
#                 'kwargs': kwargs
#             })
#             with open(self.file, 'w') as f:
#                 json.dump(self.results, f, indent=4)
#             return result
#         return wrapper
#
#
# @Timing(porog=2.0, file='timing.json')
# def func(seconds):
#     time.sleep(seconds)
#     return 'готово'
#
#
# func(3)
# func(2)
# print(func(1))






import time
from functools import wraps

class LimitCalls():
    def __init__(self, max_calls=3, period=None):
        self.max_calls = max_calls
        self.period = period
        self.count = 0
        self.start_time = None


    def __call__(self, func):
        @wraps(func)
        def wrapper(*args, **kwargs):
            if self.period is not None:
                cur_time = time.time()
                if self.start_time is None:
                    self.start_time = cur_time
                if cur_time - self.start_time > self.period:
                    self.count = 0
                    self.start_time = None
            if self.count > self.max_calls:
                raise Exception(f'Функция {func.__name__} первышает кол-во {self.max_calls} вызовов')
            self.count += 1
            return func(*args, **kwargs)
        return wrapper


@LimitCalls(max_calls=3, period=5)
def func():
    print('функция вызвана')


try:
    for _ in range(5):
        func()
        time.sleep(1)

except Exception as e:
    print(e)