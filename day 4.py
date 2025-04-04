
#chai
from abc import ABC, abstractmethod
class Chai(ABC):
    def __init__(self, name, base_price, stock):
        self.name = name
        self.base_price = base_price
        self.stock = stock

    @abstractmethod
    def calculate_price(self):
        pass

    def display_info(self):
        print(f"{self.name} | Price: ₹{self.calculate_price()} | Stock: {self.stock}")

# Subclasses
class MasalaChai(Chai):
    def calculate_price(self):
        return self.base_price + 10

class GingerChai(Chai):
    def calculate_price(self):
        return self.base_price + 8

class ElaichiChai(Chai):
    def calculate_price(self):
        return self.base_price + 12

# Inventory Class
class ChaiInventory:
    def __init__(self):
        self.chais = []

    def add_chai(self, chai):
        self.chais.append(chai)

    def show_inventory(self):
        for chai in self.chais:
            chai.display_info()

    def total_value(self):
        return sum(chai.calculate_price() * chai.stock for chai in self.chais)

# Test Code
inventory = ChaiInventory()
inventory.add_chai(MasalaChai("Masala Chai", 290, 750))
inventory.add_chai(GingerChai("Ginger Chai", 188, 840))
inventory.add_chai(ElaichiChai("Elaichi Chai", 275, 370))

inventory.show_inventory()
print("Total Inventory Value: ₹", inventory.total_value())









#Exception calculator


def calculator(a, b, operator):
    try:
        if type(a) not in [int, float] or type(b) not in [int, float]:
            raise TypeError("Invalid input type")
        elif operator == "+":
            return a + b
        elif operator == "-":
            return a - b
        elif operator == "*":
            return a * b
        elif operator == "/":
            if b == 0:
                raise ZeroDivisionError("Division by zero Error")
            return a / b
        elif operator == "%":
            if b == 0:
                raise ZeroDivisionError("Module by zero Error")
            return a % b
        elif operator == "**":
            return a ** b
        else:
            return "Unsupported operator"

    except ZeroDivisionError as e:
        return e
    except ValueError as e:
        return e
    except TypeError as e:
        return e
    except Exception as e:
        return e

print(calculator(10, 0, "/"))
print(calculator(10, "five", "+"))
print(calculator(10, 5, "$"))



#Exception bank

class InsufficientFundsError(Exception):
    pass
class BankAccount:
    def __init__(self, balance):
        self.balance = balance

    def withdraw(self, amount):
        try:
            if amount < 0:
                raise ValueError("Value Error")
            if amount >  self.balance:
                raise InsufficientFundsError("Insufficient funds")
            self.balance -= amount
            return f"Remaining Balance : {self.balance}"
        
        except ValueError as e:
            return e
        except InsufficientFundsError as e:
            return e
        except Exception as e:
            return e

account = BankAccount(100)
print(account.withdraw(150))
print(account.withdraw(-10))



#Exception Data


def process_data(data, index):
    pass
    try:
        IntData = [int(x) for x in data]
        result = IntData[index] / IntData[index - 1]
        return result 
    except ZeroDivisionError:
        return "Division by zero Error"
    except ValueError:
        return "Value Error"
    except IndexError:
        return "Index out of bounds"
    except Exception as e:
        return e
data_list = ["10", "20", "0", "40"]
print(process_data(data_list, 3))
print(process_data(["10", "abc", "30"], 1))
print(process_data([10, 20], 5))




#numpy Matrix

import numpy as np
resources = np.random.randint(15, 51, (6, 3))
total_resources = np.sum(resources, axis=0)
print(f"Total resources needed (tons): Oxygen: {total_resources[0]}, Water: {total_resources[1]}, Food: {total_resources[2]}")

max_per_month = np.max(resources, axis=1)
max_total = np.max(total_resources)
max_total_resource = ["Oxygen", "Water", "Food"][np.argmax(total_resources)]
max_month = np.unravel_index(np.argmax(resources), resources.shape)[0] + 1
max_resource = ["Oxygen", "Water", "Food"][np.argmax(resources[max_month - 1])]
max_value = np.max(resources)
print(f"Highest consumption in a month: {max_resource} ({max_value} tons in month {max_month})")

std_dev = np.std(resources, axis=0)
print(f"Standard deviation of consumption: Oxygen: {std_dev[0]:.2f}, Water: {std_dev[1]:.2f}, Food: {std_dev[2]:.2f}")

transposed_matrix = resources.T
print("Transposed matrix:")
print(transposed_matrix)


#numpy Stock

import numpy as np
array = np.random.uniform(100,500, (30,5))
stock_prices = np.round(array, decimals=2)
average = np.average(array, axis=0)
print("Average stock prices:", average)
max_day, max_company = np.unravel_index(np.argmax(stock_prices), stock_prices.shape)
print("Highest price recorded:", max, "at Day", max_day, "Company", max_company)
max = np.max(stock_prices)
min = np.min(stock_prices)
Normalized = (array-min)/(max-min)
Normalized_prices = np.round(Normalized, decimals=2)
print("Normalized prices:", Normalized_prices)
risky_investment_days = []
for day in range(30):
    risky_stocks = stock_prices[day] < 200
    if np.any(risky_stocks):
        risky_investment_days.append((day, stock_prices[day][risky_stocks].tolist()))
print("Risky Investment Days:", risky_investment_days)































