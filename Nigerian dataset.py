
# Day 1 - Python for Data Engineering
# Learning python to tell stories with Nigerian data

#print("The journey starts here")

name = "Larry"
country = "Nigeria"
current_skill = "SQL"
new_skill= "Python"
age= 20
is_student = True
goal = "Data Engineer"
city = "Lagos"

print(f" My name is {name} and I am from {country}. I want to become a {goal}, so i am learning {current_skill} and {new_skill}")


# Day 2 - Lists

skills = ["SQL","Python","Data Engineering","Excel"]
cities = ["Lagos","Abuja", "Port Harcourt", "Kano"]
ages = [20,25,26,30,45]


# for skill in skills:
#     print(f"{skill} is a skill I am learning on my Data Engineer journey")


for city in cities:
    print(f"{city} is a major city in Nigeria")



#Day 3 - Loops
skills = ["SQL","Python","Data Engineering","Excel"]
cities = ["Lagos","Abuja", "Port Harcourt", "Kano"]
ages = [20,25,26,30,45]




for skill in skills:
    if skill == "Python":
        print(f"Found it - {skill} is my new skill")


# DAY 4 - Functions

def greet_engineer(name,city):
    print(f"Hello {name}, a Data Engineer in training from {city}")

greet_engineer("Larry", "Lagos")
greet_engineer("Amaka", "Abuja")
greet_engineer("Wallace","Port Harcourt")


skills = ["SQL","Python","Data Engineering","Excel"]

def check_skill(skill_list, skill_name):
    for skill in skill_list:
        if skill == skill_name:
            print(f"Yes - {skill_name} is in your stack")

check_skill(skills, "Python")
check_skill(skills, "SQL")
check_skill(skills, "Java")


skills = ["SQL","Python","Data Engineering","Excel"]

def check_skill(skill_list, skill_name):
    for skill in skill_list:
        if skill == skill_name:
            print(f"Yes - {skill_name} is in your stack")
            return
        print(f"NO - {skill_name} is not in your stack yet")

check_skill(skills, "Python")
check_skill(skills, "SQL")
check_skill(skills, "Java")


cities = ["Lagos","Abuja", "Port Harcourt", "Kano"]

def describe_city(city_list,city_name):
    for city in city_list:
        if city == city_name:
            print(f"{city_name} is a major city in Nigeria")
            return
    print(f"{city_name} is not on our list yet")


describe_city(cities, "Lagos")
describe_city(cities, "Kano")
describe_city(cities, "Bayelsa")


# DAY 5 - Dictionaries

engineer = {
    "name": "Larry",
    "City": "Lagos",
    "country": "Nigeria",
    "skill" : "SQL",
    "learning": "Python",
    "age": 20
}

print(engineer)


engineer["new_skill"] = "pandas"
engineer["age"] = 21

for key, value in engineer.items():
    print(f"{key}: {value}")
    


engineer = [
    {"name":"Larry","city":"Lagos","skill":"SQL"},
    {"name":"Amaka","city":"Abuja","skill":"Python"},
    {"name":"Anselm","city":"Kano","skill":"Excel"}
    
]

for eng in engineer:
    print(f"{eng['name']} from {eng['city']} knows {eng['skill']}")



# Pandas





