 #Реализуйте базовый класс Car. У данного класса должны быть следующие атрибуты: 
 #speed, color, name, is_police (булево). А также методы: go, stop, turn(direction), 
 #которые должны сообщать, что машина поехала, остановилась, повернула (куда). 
 #Опишите несколько дочерних классов: TownCar, SportCar, WorkCar, PoliceCar. 
 #Добавьте в базовый класс метод show_speed, который должен показывать текущую 
 #скорость автомобиля. Для классов TownCar и WorkCar переопределите метод show_speed. 
 #При значении скорости свыше 60 (TownCar) и 40 (WorkCar) должно выводиться сообщение 
 #о превышении скорости.

class Car:


    def __init__(self, speed, color, name, is_police):
        self.speed = speed
        self.color = color
        self.name = name
        self.is_police = is_police
    
    def go(self):
        return f'{self.name} автомобиль тронулся'
        
    def stop(self):
        return f'{self.name} автомобиль остановился'
        
    def turn(self, direction):
        if direction == "right":
            return f'{self.name} автомобиль повернул на право'
        else:
            return f'{self.name} автомобиль повернул на лево'
            
            
    def show_speed(self):
        return f'Скорость автомобиля {self.name} {self.speed} км\ч'


class TownCar(Car):
    def __init__(self, speed, color, name, is_police):
        super().__init__(speed, color, name, is_police)
        
        
    def show_speed(self):
        print(f'Скорость автомобиля {self.name} {self.speed} км\ч')

        if self.speed > 40:
            return f'Скорость {self.name} была превышена'    
    
class SportCar(Car):
    def __init__(self, speed, color, name, is_police):
        super().__init__(speed, color, name, is_police)
    
class WorkCar(Car):
    def __init__(self, speed, color, name, is_police):
        super().__init__(speed, color, name, is_police)
        
        
    def show_speed(self):
        print(f'Скорость автомобиля {self.name} {self.speed} км\ч')

        if self.speed > 60:
            return f'Скорость {self.name} была превышена'    
    
class PoliceCar(Car):
    def __init__(self, speed, color, name, is_police):
        super().__init__(speed, color, name, is_police)    
    
    
    
priora = TownCar(70, 'green', 'Ауди', False)
methods = [priora.show_speed(), 
        priora.speed,
        priora.color,
        priora.go(), 
        priora.turn('right'), 
        priora.turn('left'), 
        priora.stop(), 
        priora.is_police
        ]
for i in methods:
    print(i)    
    
largus = WorkCar(160, 'red', 'Ауди', False)
methods = [largus.show_speed(), 
        largus.speed,
        largus.color,
        largus.go(), 
        largus.turn('right'), 
        largus.turn('left'), 
        largus.stop(), 
        largus.is_police
        ]
for i in methods:
    print(i)
    
audi_rs = SportCar(210, 'blue', 'Ауди', False)
methods = [audi_rs.show_speed(), 
        audi_rs.speed,
        audi_rs.color,
        audi_rs.go(), 
        audi_rs.turn('right'), 
        audi_rs.turn('left'), 
        audi_rs.stop(), 
        audi_rs.is_police
        ]
for i in methods:
    print(i)    
    
police_bmw = SportCar(120, 'grey', 'Ауди', True)
methods = [police_bmw.show_speed(), 
        police_bmw.speed,
        police_bmw.color,        
        police_bmw.go(), 
        police_bmw.turn('right'), 
        police_bmw.turn('left'), 
        police_bmw.stop(), 
        police_bmw.is_police
        ]
for i in methods:
    print(i)  
    