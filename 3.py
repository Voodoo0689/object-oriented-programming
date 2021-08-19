# Реализовать базовый класс Worker (работник), в котором определить атрибуты: 
# name, surname, position (должность), income (доход). Последний атрибут должен 
# быть защищенным и ссылаться на словарь, содержащий элементы: оклад и премия, 
# например, {"wage": wage, "bonus": bonus}. Создать класс Position (должность) на базе класса Worker. 
# В классе Position реализовать методы получения полного имени сотрудника (get_full_name) и 
# дохода с учетом премии (get_total_income). Проверить работу примера на реальных данных 
# (создать экземпляры класса Position, передать данные, проверить значения атрибутов, вызвать методы экземпляров).





class Worker:
	_income = {}

	def __init__(self, name, surname, wage, bonus):
		self.name = name
		self.surname = surname
		self.wage = wage
		self.bonus = bonus
		Worker._income = {"wage": self.wage, "bonus": self.bonus}


class Position(Worker):
	get_full_name = ""
	get_total_income = ""
	
	def __init__(self, name, surname, wage, bonus):
		super().__init__(name, surname, wage, bonus)
			
		Position.get_full_name = f'{name} {surname}'
		Position.get_total_income = f'{sum(Position._income.values())}'
 

p = Position("Worker", "Man", 15000, 2700)


print(p.get_full_name, p.get_total_income)

