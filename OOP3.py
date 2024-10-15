# from abc import ABC, abstractmethod
# from datetime import datetime
#
#
# class ValidatorPerformance():
#     def __get__(self, instance, owner):
#         return instance._performance
#
#     def __set__(self, instance, value):
#         if not  isinstance(value, (int, float)) or value < 0:
#             raise ValueError('Производительность не может быть отрицательна')
#         instance._performance = value
#
#
# def log_operation(func):
#     def wrapper(*args, **kwargs):
#         result = func(*args, **kwargs)
#         data_time = datetime.now()
#         with open('performance.txt', 'a') as f:
#             f.write(f'{data_time}--{func.__name__} выполнен\n')
#         return result
#     return wrapper
#
#
#
# class Component(ABC):
#     performance = ValidatorPerformance()
#
#     @abstractmethod
#     def __init__(self, name, performance):
#         self._name = name
#         self.performance = performance
#
#
#     @property
#     def name(self):
#         return self._name
#
#
#     @abstractmethod
#     def __str__(self):
#         return f'{self.name}: {self.performance}'
#
#
#
#
# class Monitor():
#     def __init__(self):
#         self._components = []
#
#
#     @log_operation
#     def add_component(self, component):
#         self._components.append(component)
#
#
#     @log_operation
#     def remove_component(self, neme_component):
#         self._components = [c for c in self._components if c.name != neme_component]
#
#
#     @log_operation
#     def get_info_performance(self):
#         return '\n'.join(str(c) for c in self._components)
#
#
#     @staticmethod
#     def get_status():
#         return f'Система работает стабильно'
#
#
#
#
# class Logger():
#     def __init__(self, log_file='log_performance.txt'):
#         self.log_file = log_file
#
#
#     def log(self, massage):
#         dt = datetime.now()
#         with open(self.log_file, 'a', encoding='utf-8') as f:
#             f.write(f'({dt}) = {massage}\n')
#
#
#
# class CPU(Component):
#     def __init__(self, name, performance):
#         super().__init__(name, performance)
#
#
#     def __str__(self):
#         return f'CPU: {self.name}| Производительность: {self.performance}'
#
#
#
#
# class Memory(Component):
#     def __init__(self, name, performance):
#         super().__init__(name, performance)
#
#     def __str__(self):
#         return f'Memory: {self.name}| Производительность: {self.performance}'
#
#
#
#
# class Disk(Component):
#     def __init__(self, name, performance):
#         super().__init__(name, performance)
#
#
#     def __str__(self):
#         return f'Disk: {self.name}| Производительность: {self.performance}'
#
#
# import psutil
#
# def get_info_ps():
#     cpu_name = 'CPU' + str(psutil.cpu_freq()) + 'hg'
#     cpu_perf = psutil.cpu_percent(interval=1)
#     memory_name = 'Memory'
#     memory_info = psutil.vertual_memory().percent
#     disk_name = 'Disk'
#     disk_info = psutil.disk_usage('/')
#     return cpu_name, cpu_perf, memory_name, memory_inf, disk_name, disk_info
#
# cpu_name, cpu_perf, memory_name, memory_info, disk_name, disk_info = get_info_ps()
#
# cpu = CPU(cpu_name, cpu_perf)
# memory = Memory(memory_name, memory_info)
# disk = Disk(disk_name, disk_info)
#
# monitor = Monitor()
# logger = Logger()
#
# monitor.add_component(cpu)
# monitor.add_component(memory)
# monitor.add_component(disk)
# report = monitor.get_info_performance()
# print(report)
# logger.log(report)
#
#
# monitor.remove_component('Corsair')
# report = monitor.get_info_performance()
# print(report)
# logger.log(report)
#
# print(Monitor.get_status())






import random
class BoardExeption(Exception):
    pass


class BoardOutEx(BoardExeption):
    def __str__(self):
        return 'Координаты вне доски'


class BoardUsedEx(BoardExeption):
    def __str__(self):
        return 'В эта клетка уже обстрелянна'


class Ship():
    pass


class Coord():
    def __init__(self, x, y):
        self.x = x
        self.y = y


    def __eq__(self, other):
        return self.x == other.x and self.y == other.y


class Board():
    def __init__(self, size=6, hide=False):
        self.size = size
        self.hide = hide
        self.ships = []
        self.field = [['0'] * size for _ in range(size)]
        self.busy = []
        self.count = 0


    def __str__(self):
        res = ''
        res += '   | 1 | 2 | 3 | 4 | 5 | 6 |'
        for i, row in enumerate(self.field):
            res += f'\n {i+1} | '+' | '.join(row) + ' |'
        if self.hide:
            res = res.replace('#', '0')
        return res

print(Board())

#     def contur(self):
#         pass
#
#
#     def add_ship(self):
#         pass
#
#
#     def shot(self):
#         pass
#
#
# class Player():
#     pass
#
#
# class User(Player):
#     pass
#
#
# class AI(Player):
#     pass
#
#
# class Game():
#     pass


