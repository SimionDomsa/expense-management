import datetime

class User:
    def __init__(self, user: str , password: str, token: str):
        self.user = user
        self.password = password
        self.token = token


class Income:
    def __init__(self, name: str, value: float, date: datetime):
        self.name = name
        self.value = value


class ExpenseCategory:
    def __init__(self, name: str, expenses: list, date: datetime):
        self.name = name
        self.expenses = expenses
        

class Expense:
    def __init__(self, description: str, value: float, date: datetime):
        self.description = description
        self.value = value
        self.date = date
        

class Investment:
    def __init__(self, name: str, value: float, date: datetime):
        self.name = name
        self.value = value
        self.date = date


class Stable(Investment):
    def __init__(self, name: str, value: float, date: datetime, gain: float):
        super().__init__(name, value)
        self.gain = gain


class Volatile(Investment):
    def __init__(self, name: str, value: float, date: datetime, gamble: float):
        super().__init__(name, value)
        self.gamble = gamble


class Repository:
    def __init__(self):
        self.incomes_list = []
        self.expenses_categories = []

    def create_income(self, new_income):
        self.incomes.append(new_income)
    
    def get_incomes(self):
        return self.incomes
    
    def delete_income(self, rm_income):
        for income in self.incomes_list:
            if income.name == rm_income:
                self.incomes.remove(income)
    
    def update_income(self):
        pass

    def update_income_starting_month(self):
        pass
    
    def add_current_month_income(self):
        pass

    def add_specific_month_income(self):
        pass

    def incomes_to_dict(self):
        incomes = []
        for income in self.incomes_list:
            keys = ['name', 'value']
            values = [income.name, income.value]
            incomes.append(dict(zip(keys, values)))
        return incomes

    def create_expense_category(self, new_expense_category):
        self.expenses_categories.append(new_expense_category)

    def create_expense(self):
        pass
    
    def delete_expense(self):
        pass


class Service:
    def __init__(self) -> None:
        self.repository: Repository = Repository()


class Controller:
    def __init__(self) -> None:
        self.service: Service = Service()