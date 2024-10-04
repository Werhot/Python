# def my_decorator(func):
#     def wrapper():
#         print('до вызова функции')
#         func()
#         print('После выхода из функции')
#     return wrapper
#
#
# @my_decorator
# def hello():
#     print('Hello!')
#
# #h = my_decorator(hello)
# hello()




# def decor(func):
#     def wrapper(*args, **kwargs):
#         print('до вызова функции')
#         result = func(*args, **kwargs)
#         print('После выхода из функции')
#         return result
#     return wrapper
#
#
# @decor
# def greet(name):
#     print(f'Hello, {name}')
#
#
# greet('Alice')




# def repeat(n):
#     def decor(func):
#         def wrapper(*args, **kwargs):
#             for _ in range(n):
#                 func(*args, **kwargs)
#         return wrapper
#     return decor
#
#
# @repeat(4)
# def greet(name):
#     print(f'Hello, {name}')
#
#
# greet('Sasha')




# from functools import wraps
# def decor(func):
#     @wraps(func)
#     def wrapper(*args, **kwargs):
#         print('до вызова функции')
#         result = func(*args, **kwargs)
#         print('После выхода из функции')
#         return result
#     return wrapper
#
#
# @decor
# def greet(name):
#     """Это функция приветствует пользователя"""
#     print(f'Hello, {name}')
# greet('Alice')
#
#
# print(greet.__name__)
# print(greet.__doc__)




import os
import json
from functools import wraps
from datetime import datetime
import time


LOG_FILE = 'function_log.json'

def log_calls(level='info'):
    levels = ['info', 'warning', 'error']
    if level not in levels:
        raise ValueError(f'Уровень логирования должен быть {levels}')
    def decorator(func):
        @wraps(func)
        def wrapper(*args, **kwargs):
            call_time = datetime.now().isoformat()
            log_dict = {
                'function_name': func.__name__,
                'arguments': {
                    'args': args,
                    'kwargs': kwargs,
                },
                'call_time': call_time,
                'level': level
            }
            if os.path.exists(LOG_FILE):
                with open(LOG_FILE, 'r') as f:
                    logs = json.load(f)
            else:
                logs = []
            logs.append(log_dict)
            with open(LOG_FILE, 'w') as f:
                json.dump(logs, f, indent=4)


            return func(*args, **kwargs)
        return wrapper
    return decorator


def filter_log(start_time=None, end_time=None, func_name=None):
    if not os.path.exists(LOG_FILE):
        return []
    with open(LOG_FILE, 'r') as f:
        logs = json.load(f)
    filtered_logs = []
    for log in logs:
        log_time = datetime.fromisoformat(log['call_time'])

        if func_name and log['function_name'] != func_name:
            continue

        if start_time and log_time < datetime.fromisoformat(start_time):
            continue

        if end_time and log_time > datetime.fromisoformat(end_time):
            continue

        filtered_logs.append(log)
    return filtered_logs




@log_calls(level='info')
def ex_func(a, b):
    return a + b


ex_func(1, 7)
ex_func(9, 5)

start_time = '2024-10-04T00:00:00'
end_time = '2024-10-05T00:00:00'
logs = filter_log(start_time, end_time, 'ex_func')
print(logs)