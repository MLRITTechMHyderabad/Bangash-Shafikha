'''n=int(input("enter no of students"))
students={}
for i in range(n):
    name = input("Enter name")
    grades = list(map(int, input("Enter grades ").split()))
    students[name] = grades
    avg_grades = {name: sum(grades) / len(grades) for name, grades in students.items()}
    top_student = max(avg_grades, key=avg_grades.get)
    passed_students = sum(1 for avg in avg_grades.values() if avg >= 50)

print("Student Grades:", students)
print("Average Grades:", avg_grades)
print("Top Student:", top_student)
print("Number of Students Passed:", passed_students)


                    


import random

class Character:
    def __init__(self, name, health, attack_power, defense, speed):
        self.name = name
        self.health = health
        self.attack_power = attack_power
        self.defense = defense
        self.speed = speed
    
    def attack(self, target):
        damage = max(1, self.attack_power - target.defense)
        print(f"{self.name} attacks {target.name}! Deals {damage} damage.")
        target.take_damage(damage)
    
    def take_damage(self, amount):
        self.health -= amount
        print(f"{self.name} takes {amount} damage. Remaining health: {self.health}")
    
    def is_alive(self):
        return self.health > 0

class Warrior(Character):
    def __init__(self, name):
        super().__init__(name, health=120, attack_power=20, defense=10, speed=5)
        self.rage = 0
    
    def attack(self, target):
        if self.health < 36:  
            print(f"{self.name} enters Berserk Mode! Attack power doubled!")
            damage = max(1, (self.attack_power * 2) - target.defense)
        else:
            damage = max(1, self.attack_power - target.defense)
        
        print(f" {self.name} swings a sword! Deals {damage} damage.")
        target.take_damage(damage)

class Mage(Character):
    def __init__(self, name):
        super().__init__(name, health=80, attack_power=30, defense=5, speed=7)
        self.mana = 50
    
    def fireball(self, target):
        if self.mana >= 10:
            self.mana -= 10
            damage = max(1, (self.attack_power + 10) - target.defense)
            print(f" {self.name} casts Fireball! Deals {damage} damage but loses 5 health.")
            target.take_damage(damage)
            self.take_damage(5)
        else:
            print(f"{self.name} has no mana left! Regular attack instead.")
            self.attack(target)

class Archer(Character):
    def __init__(self, name):
        super().__init__(name, health=90, attack_power=22, defense=8, speed=10)
        self.critical_chance = 30 
    
    def attack(self, target):
        if random.randint(1, 100) <= self.critical_chance:
            damage = max(1, (self.attack_power * 2) - target.defense)
            print(f" {self.name} lands a Critical Hit! Deals {damage} damage.")
        else:
            damage = max(1, self.attack_power - target.defense)
            print(f" {self.name} shoots an arrow! Deals {damage} damage.")
        target.take_damage(damage)

def battle(character1, character2):
    print("\nBattle Begins!\n")
    while character1.is_alive() and character2.is_alive():
        if character1.speed >= character2.speed:
            character1.attack(character2)
            if character2.is_alive():
                character2.attack(character1)
        else:
            character2.attack(character1)
            if character1.is_alive():
                character1.attack(character2)
        print("\n--- Next Turn ---\n")
    
    if character1.is_alive():
        print(f" {character1.name} wins the battle!")
    else:
        print(f" {character2.name} wins the battle!")

# Example Battle
warrior = Warrior("Thor")
mage = Mage("Gandalf")
archer = Archer("Alex")

battle(archer, warrior)






    '''




employees = [
    {"name":"Tony", "Salary":50000.00, "rating":5},
    {"name":"Steves", "Salary":45000.00, "rating":3},
    {"name":"Natasha", "Salary":40000.00, "rating":1},
    {"name":"Bruce", "Salary":48000.00, "rating":2}
]
print(employees)

salary_hike = lambda emp : {
    "name" : emp["name"], 
    "Salary": round(emp["Salary"] * 1.10) if emp["rating"] in [4, 5] else
              emp["Salary"] * 1.05 if  emp["rating"] == 3 else
              emp["Salary"] * 0.97,
    "rating": emp["rating"]
}
update_employees = list(map(salary_hike, employees))

for emp in update_employees:
    print(f"{emp['name']}'s new salary: {emp['Salary'] }")
      






































n = int(input("Enter number of employees: "))

employees = [ {"name": input("Enter employee name: "), "salary": float(input("Enter salary: ")), "rating": int(input("Enter rating (1-5): "))} for _ in range(n) ]

adjust_salary = lambda emp: { **emp, "salary": round( emp["salary"] * (1.1 if emp["rating"] >= 4 else 1.05 if emp["rating"] == 3 else 0.97), 2 ) }

updated_employees = list(map(adjust_salary, employees))

print("\nUpdated Employee Salaries:")
for emp in updated_employees: print(emp)























	

    
            

    
