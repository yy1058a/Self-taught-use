#-*- coding: utf-8 -*

print("Hello world!")
message = "Hello"
print(message)

message ="Hello2"
print(message)

name ="ada lovelace"
print(name.title())
print(name.upper())
print(name.lower())
# title() upper() lower() 以上三个函数，开头大写，全部大写，全部小写。
first_name = "ada"
last_name ="lovelace"
full_name = first_name+" "+last_name

print(full_name)

print("hello, " + full_name.title()+"!")

print("\tPhython")
# \t表示制表符 tabs
print("Phython\nC\nJavaScript")
# \n表示换行符 Newline
print("language:\n\tPython\n\tC\n\tJavascript")

favorite_language = 'python '
print(favorite_language.rstrip())
# .rstrip()：删除最后的空格

favorite_language = " python "
print(favorite_language.lstrip())
# .lstrip()：删除开头的空格
print(favorite_language.strip())
# .strip()：删除前后的空格

age=23
message="Happy "+str(age)+ "rd Brithday!"
print(message)
# 使用str()将23变为字符串，因为无法分辨23是数字还是字符2和3.

print(2**2)
# **表示平方

bicycles = ['trek', 'cannondale', 'redline', 'specialized']
print(bicycles)
# []方括号表示列表，用逗号分隔其中的元素。

print(bicycles[0])
# 第一个元素的序号居然是0
print(bicycles[0].title())

print(bicycles[-2])
# 反向索引元素

message = "my first bicycle was a " + bicycles[0].title() + "."
print(message)

motorcycles = ['honda', 'yamaha', 'suzuki']
print(motorcycles)
motorcycles[0] = 'ducati'
print(motorcycles)
# 修改列表元素

motorcycles = ['honda', 'yamaha', 'suzuki']
print(motorcycles)
motorcycles.append('ducati')
print(motorcycles)
# .append() ：在末尾增加元素用

motorcycles = ['honda', 'yamaha', 'suzuki']
print(motorcycles)
motorcycles.insert(1, 'ducati')
print(motorcycles)
# .insert插入元素：在列表中插入元素，公式前数字表示插入的位置。可以视为插入在原位子的左边。

motorcycles = ['honda', 'yamaha', 'suzuki']
print(motorcycles)
del motorcycles[0]
print(motorcycles)
# del删除：注意这个不太一样的用法， del命令在前，按序号删除。

motorcycles = ['honda', 'yamaha', 'suzuki']
print(motorcycles)
popped_motorcycles = motorcycles.pop()
print(motorcycles)
print(popped_motorcycles)

motorcycles = ['honda', 'yamaha', 'suzuki']
last_owned = motorcycles.pop()
print("The lase motorcycle I owned was a " + last_owned + ".")
# .pop(): 如果pop()中不填写数值，用于选择列表中最后一个元素。

motorcycles = ['honda', 'yamaha', 'suzuki']
first_owned = motorcycles.pop(1)
# 指定1号位提取并删除。
print("The first motorcycle I owned was a " + first_owned + ".")
# del和pop的区别： del是直接从列表中进行删除。 pop在删除的同时，也把被删除的元素提取出来了。

motorcycles = ['honda', 'yamaha', 'suzuki']
motorcycles.remove('honda')
print(motorcycles)
# .remove(): 根据元素的值进行删除。在不知道元素位置的时候使用。
# 但是.remove()只会删除第一个这样的值，如果循环出现需要别的代码（第七章）。

cars = ['bmw', 'audi', 'toyota', 'subaru']
cars.sort()
print(cars)
# .sort():按字母排列，永久改变列表排序方式

cars.sort(reverse=True)
print(cars)
# 指定reverse=Ture， 反向排序。 reverse反向。

cars = ['bmw', 'audi', 'toyota', 'subaru']
print("Here is the original list:")
print(cars)
print("\nHere is the sorted list:")
print(sorted(cars))
print("\nHere is the original list again:")
print(cars)
# sorted():不会改变原来列表中的顺序，只是输出改变结果

cars = ['bmw', 'audi', 'toyota', 'subaru']
print(cars)
cars.reverse()
print(cars)
# .reverse()：用于反转原顺序

len(cars)
# 确定长度

magicians = ['alice', 'david', 'carolina']
for magician in magicians:
    print(magician)
# 手动定义列表及内容。通过 ‘for A in 列表’，临时定义元素的名字（A）。
# For in 是循环语句。对列表中的每个元素，都执行循环指定的步骤。

magicians = ['alice', 'david', 'carolina']
for magician in magicians:
    print(magician.title() + ", that was a great trick!")
    print("I can't wait to see your next trick, " + magician.title() + ".\n")
print("Thank you, everyone. That was a great magic show!")

for value in range(1,5):
    print(value)
# 从指定的第一个数字开始打印，并在指定的第二个数字时停止，并且不打印第二个数值。

number = list(range(1,6))
print(number)
# list()和range()创建数字列表。注意range的差一行为。

even_number = list(range(2, 11, 2))
print(even_number)
# 使用range指定步长，创建等差数列。上例步长位为2。

squares = []
for value in range(1, 11):
    square = value**2
    squares.append(square)
    print(squares)
# 创建一个平方的列表。

squares = []
for value in range(1, 11):
    squares.append(value**2)
print(squares)
# 上面步骤的简化版1。

digits = [1, 2, 3, 4, 5, 6, 7, 8, 9, 0]
min(digits)
max(digits)
sum(digits)

squares = [value**2 for value in range(1, 11)]
print(squares)
# 上面步骤的简化版2. 这叫列表解析。

players = ['charles', 'martina', 'michael', 'florence', 'eli']
print(players[0:3])
# 前三个
print(players[3])
# 第四个
# 列表中的部分元素称之为切片。想提取列表中的A~B个元素。索引因设定为[A-1,B].
print(players[:4])
# 如果不指定起始索引，则从开头提取。
print(players[2:])
# 同理，从第三到最后。
print(players[-3:])
# 从倒数第三到最后。

players = ['charles', 'martina', 'michael', 'florence', 'eli']
print("Here are the first three players on my team:")
for player in players[:3]:
    print(player.title())
# 遍历切片。

my_foods = ['pizza', 'falafel', 'carrot cake']
friend_foods = my_foods[:]
print("My favorite foods are:")
print(my_foods)
print("\nMy friend's favorite foods are:")
print(friend_foods)
# 使用[:]进行列表复制。

my_foods = ['pizza', 'falafel', 'carrot cake']
friend_foods = my_foods[:]
my_foods.append('cannoli')
friend_foods.append('ice cream')
print("My favorite foods are:")
print(my_foods)
print("\nMy friend's favorite foods are:")
print(friend_foods)
# 确保赋值是使用[:]进行了切片复制。如果使用A=B，会导致A与B同时改动。

dimensions = (200, 50)
print(dimensions[0])
print(dimensions[1])
# 元组：使用圆括号，即赋值。[]用来创建列表，[数值]选择位置，[1：n]选择范围。
dimensions[0] = 250
# 元组的元素是不能修改的，因此会报错。

for dimension in dimensions:
    print(dimension)
# 遍历元组。

print("Orignal dimensions:")
for dimension in dimensions:
    print(dimension)
dimensions = (400, 100)
print("\nModified dimentions:")
for dimension in dimensions:
    print(dimension)
# 不能修改元组中的元素。因此修改元组变量只能重新赋值元组。

cars = ['audi', 'bmw', 'subaru', 'toyota']
for car in cars:
    if car == "bew":
        print(car.upper())
    else:
        print(car.title())
# if 语句

cars = 'bmw'
# 赋值： 用一个等号
cars == 'bmw'
# 条件测试：两个等号

cars = ['audi', 'bmw', 'subaru', 'toyota']
for car in cars:
    if car == 'subaru':
        print("\nIs car == 'subaru'? I predict True.")
        print(car == 'subaru')
    else:
        print("\nIs car == 'audi'? I predict False.")
        print(car == 'audi')


age = 12
if age < 4:
    print("Your admission cost is $0.")
elif age < 18:
    print("Your admission cost is $5.")
else:
    print("Your admission cost is $10.")


age = 12
if age < 4:
    price = 0
elif age < 18:
    price = 5
else:
    price = 10
print("Your admission cost is $" + str(price) + ".")


requested_toppings = ['mushrooms', 'green peppers', 'extra cheese']
for requested_topping in requested_toppings:
    if requested_topping == 'green peppers':
        print("Sorry, we are out of green peppers right now.")
    else:
        print("Adding " + requested_topping + ".")
print("\nFinished making your pizza!")


requested_toppings = []
if requested_toppings:
    for requested_topping in requested_toppings:
        print("Adding " + requested_topping + ".")
    print("\nFinished making your pizza!")
else:
    print("Are you sure you want a plain pizza?")
# 测试空集。

alien_0 = {'color': 'green', 'points': 5}
print(alien_0['color'])
# 创建字典

new_points = alien_0['points']
print("You just earned " + str(new_points) + " points!")

alien_0['x_position'] = 0
alien_0['y_position'] = 25
print(alien_0)

alien_0 = {}
alien_0['color'] = 'green'
alien_0['points'] = 5
print(alien_0)

alien_0 = {'x_position': 0, 'y_position': 25, 'speed': 'medium'}
print("Original x-position: " + str(alien_0['x_position']))

if alien_0['speed'] == 'slow':
    x_increment = 1
elif alien_0['speed'] == "medium":
    x_increment = 2
else:
    x_increment = 3

alien_0['x_position'] = alien_0['x_position'] + x_increment

print("New x_positon: " + str(alien_0['x_position']))
# 用速度计算距离的代码。

alien_0 = {'color': 'green', 'points': 5}
print(alien_0)

del alien_0['points']
print(alien_0)
# 删除键-值

favorite_languages  = {
    'jen': 'python',
    'sarah': 'c',
    'edward': 'ruby',
    'phil': 'python',
    }

print("Sarah's favorite language is " +
      favorite_languages['sarah'].title() +
      ".")

user_0 = {
    'username': 'efermi',
    'first': 'enrico',
    'last': 'fermi',
}

for key, value in user_0.items():
    print("\nKey: " + key)
    print("Value: " + value)
# 遍历字典

favorite_languages

for name, language in favorite_languages.items():
    print(name.title() + "'s favorite language is " +
          language.title() + ".")
# 遍历字典例2

for name in favorite_languages.keys():
    print(name.title())
# key()： 当不需要显示值的时候，直接用这个函数显示键。不输入时，python也会默认遍历键。

friends = ['phil', 'sarah']
for name in favorite_languages:
    print(name.title())
    if name in friends:
        print(" Hi " + name.title() +
              ", I see your favorite language is " +
              favorite_languages[name].title() + "!")

if 'erin' not in favorite_languages:
    print("Erin, please take our poll!")
# 不包含元素的遍历

favorite_languages
for name in sorted(favorite_languages):
    print(name.title() + ", thank you for taking the poll.")
# 用sorted() 来按顺序遍历字典中的键。

print("The following languages have been mentioned:")
for language in favorite_languages.values():
    print(language.title())
# 遍历字典中的值。

alien_0 = {'color': 'green', 'points': 5}
alien_1 = {'color': 'yellow', 'point': 10}
alien_2 = {'color': 'red', 'point': 15}

aliens = [alien_0, alien_1, alien_2]
for alien in aliens:
    print(alien)
# 多个字典组合。

aliens = []
for alien_number in range(30):
    new_alien = {'color': 'green', 'points': 5, 'speed': 'slow'}
    aliens.append(new_alien)
for alien in aliens[:5]:
    print(alien)
print("...")
print("Total number of aliens:" + str(len(aliens)))

aliens = []
for alien_number in range(0, 30):
    new_alien = {'color': 'green', 'points': 5, 'speed': 'slow'}
    aliens.append(new_alien)

for alien in aliens[0:3]:
    if alien['color'] == 'green':
        alien['color'] = 'yellow'
        alien['speed'] = 'medium'
        alien['points'] = 10

for alien in aliens[0:5]:
    print(alien)
print("...")

for alien in aliens[0:3]:
    if alien['color'] == 'green':
        alien['color'] = 'yellow'
        alien['speed'] = 'medium'
        alien['points'] = 10
    elif alien['color'] == 'yellow':
        alien['color'] = 'red'
        alien['speed'] = 'fast'
        alien['point'] = '15'
# 选择性批量修改列表中的字典。

pizza = {
    'crust': 'thick',
    'toppings': ['mushrooms', 'extra cheese'],
}
print("You ordered a " + pizza['crust'] + "-crust pizza " + "with the flowing toppings:")
for topping in pizza['toppings']:
    print("\t" + topping)
# 在字典中储存列表例1

favorite_languages = {
    'jen': {'python', 'ruby'},
    'sarah': {'c'},
    'edward': {'ruby', 'go'},
    'phil': {'python', 'haskell'},
}
for name, languages in favorite_languages.items():
    print("\n" + name.title() + "'s favorite language are:")
    for language in languages:
        print("\t" + language.title())
# 在字典中储存列表例2

users = {
    'aeinstein': {
        'first': 'albert',
        'last': 'einsein',
        'location': 'princeton',
    },
    'mcurie': {
        'first': 'marie',
        'last': 'curie',
        'location': 'paris',
    },
}
for username, user_info in users.items():
    print("\nUsername: " + username)
    full_name = user_info['first'] + " " + user_info['last']
    location = user_info['location']
    print("\tFull name: " + full_name.title())
    print("\tLocation: " + location.title())
# 在字典中储存字典。

message = input("Tell me something, and I will repeat back to you: ")
print(message)
# 对话小游戏。print(message)将输入呈现给用户。注意要两行一起运行。

name = input("Please enter your name:")
print("Hello, " + name + "!")

prompt = "If you tell us who you are, we can personalize the messages you see."
prompt += "\nWhat is your first name? "
name = input(prompt)
print("\nHello, " + name + "!")
# += 用于续加一串字符串。

age = input("How old are you?")
age
# 用户输入的input会变成赋值。这种情况输入的是字符。不能作为数字比较。

age = input("How old are you?")
age = int(age)
age >= 18
# 使用int()进行数值型转化。

height = input("How tell are you, in inches?")
height = int(height)
if height >= 36:
    print("\nYou're tall enough to ride!")
else:
    print("\nYou'll be able to ride when you're a little older.")
# 使用Int()来进行值输入。

4 % 3
# %求模运算符，将两个数相除并返回余数。

number = input("Enter a number, and I'll tell you if it's even or odd:")
number = int(number)
if number % 2 == 0:
    print("\nThe number " + str(number) + " is even.")
else:
    print("\nThe number " + str(number) + " is odd.")
# 求模运算

current_number = 1
while current_number <= 5:
    print(current_number)
    current_number += 1
# while 循环例1

prompt = "\nTell me something, and I will repeat it back to you:"
prompt += "\nEnter 'quit' to end the program."
message = ""
while message != 'quit':
    message = input(prompt)
    if message != 'quit':
        print(message)
# while 循环例2

prompt = "\nTell me something, and I will repeat it back to you:"
prompt += "\nEnter 'quit' to end the program."

active = True
while active:
    message = input(prompt)
    if message == 'quit':
        active = False
    else:
        print(message)
# 使用了active = True 作为标志来指出程序是否处于活动状态。可以添加多个事件。例中只有一次。

prompt = "\nPlease enter the name of a city you have visited:"
prompt += "\n(Enter 'quit' when you are finished.)"

while True:
    city = input(prompt)
    if city == 'quit':
        break
    else:
        print("I'd love to go to " + city.title() + "!")
# 使用break退出循环。

current_number = 0
while current_number < 10:
    current_number += 1
    if current_number % 2 == 0:
        continue
    print(current_number)
# continue运行时，使得程序不管剩下的代码，直接回到程序开头。

x = 1
while x <=5:
    print(x)
    x += 1
# 编写代码的时候要注意避免无限循环。

unconfirmed_users = ['alice', 'brian', 'candace']
confirmed_users = []

while unconfirmed_users:
    current_user = unconfirmed_users.pop()
    print("Verifying user: " + current_user.title())
    confirmed_users.append(current_user)
print("\nThe following users have been confirmed:")

for confirmed_user in confirmed_users:
    print(confirmed_user.title())
# pop()函数用于删除最后一个元素，并返回该元素的值。
# 在for 循环中不应该修改列表。因此在遍历列表的同时对其修改要和while语句一同使用。

pets = ['dog', 'cat', 'dog', 'goldfish', 'cat', 'rabbit', 'cat']
print(pets)

while 'cat' in pets:
    pets.remove('cat')
print(pets)
# 删除包含特定值的所有列表元素。使用循环进行多次删除。

responses = {}
polling_active = True
while polling_active:
    name = input("\nWhats your name?")
    response = input("Which mountain would you like to climb someday?")
    responses[name] = response
    repeat = input("Would you like to let another person respond? (yes/ no) ")
    if repeat == 'no':
        polling_active = False
print("\n--- Poll Results ---")
for name, response in responses.items():
    print(name + " Would like to climb " + response + ".")
# 使用用户输入来填充字典。
#  responses[name] = response 用于在字典中创建 键-值。

# 第七章小结： input()； while循环中的 设置活动标志，break， continue，列表间移动元素，删除特定元素，使用while循环字典。

def greet_user(username):
    print("Hello, " + username.title() + "!")
greet_user('jesse')
# def是定义的意思。 定义函数。 username是形参，jesse具体的输入为实参。

def describe_pet(pet_name, animal_type='dog'):
    # 设置形参的默认值/
    print("\nI have a  " + animal_type + ".")
    print("My " + animal_type + "'s name is " + pet_name.title() + ".")
describe_pet('harry', 'hamster')
describe_pet(animal_type='dog', pet_name='willie')
# 关键字实参。
describe_pet('whille')
# 只有一个实参的情况下会自动关联函数中的第一个形参。

def get_formatted_name(first_name, last_name):
    full_name = first_name + ' ' + last_name
    return full_name.title()
musician = get_formatted_name('jimi', 'hendrix')
print(musician)
# return 引导函数调用行。

def get_formatted_name(first_name, last_name, middle_name=''):
    if middle_name:
        full_name = first_name + ' ' + middle_name + ' ' + last_name
    else:
        full_name = first_name + ' ' + last_name
    return full_name.title()
musician = get_formatted_name('jimi', 'hendrix')
print(musician)
musician = get_formatted_name('jimi', 'hendrix', 'lee')
print(musician)
# 使得实参变成可选择的。

def bulid_person(first_name, last_name):
    person = {'first': first_name, 'last': last_name}
    return person
musician = bulid_person('jimi', 'hendrix')
print(musician)
# return 也可以返回字典。


def bulid_person(first_name, last_name, age = ''):
    person = {'first': first_name, 'last': last_name}
    if age:
        person['age'] = age
    return person
musician = bulid_person('jimi', 'hendrix',age=27)
print(musician)
# return返回字典例2.

def get_formatted_name(first_name, last_name):
    full_name = first_name + ' ' + last_name
    return full_name.title()
while True:
    print("\nPlease tell me your name:")
    print("(enter 'q' at any time to quit)")

    f_name = input("First name:")
    if f_name == 'q':
        break
    l_name = input("Last name:")
    if l_name == 'q':
        break
    formatted_name = get_formatted_name(f_name, l_name)
    print("\nHello, " + formatted_name + "!")
# 结合使用定义和while循环。

def greet_users(names):
    for name in names:
        msg = "Hello, " + name.title() + "!"
        print(msg)
usernames = ['hannah', 'ty', 'margot']
greet_users(usernames)
# 向函数中导入列表。

unprinted_designs = ['iphone case', 'robot pendant', 'dodecahedron']
completed_models = []
while unprinted_designs:
    current_design = unprinted_designs.pop()
    print("Printing model: " + current_design)
    completed_models.append(current_design)
print("\nThe following models have been printed:")
for completed_model in completed_models:
    print(completed_model)
# 在函数中修改列表例1

def print_models(unprinted_designs, completed_models):
    while unprinted_designs:
        current_design = unprinted_designs.pop()
        print("Printing model:" + current_design)
        completed_models.append(current_design)
def show_completed_models(completed_models):
    print("\nThe following models have been printed:")
    for completed_model in completed_models:
        print(completed_model)
unprinted_designs = ['iphone case', 'robot pendant', 'dodecahedron']
completed_models = []
print_models(unprinted_designs, completed_models)
show_completed_models(completed_models)
# 在函数中修改列表例2，这里使用了两个函数定义。

print_models(unprinted_designs[:], completed_models)
# function_name(list_name[:])
# 将列表的副本传递给函数的公式，切片表示法[:]。

def make_pizza(*toppings):
    print("\nMaking a pizza with the following toppings:")
    for topping in toppings:
        print("-" + topping)
make_pizza('pepperoni')
make_pizza('mushrooms', 'green peppers', 'extra cheese')
# *建立了一个名为toppings的空元组，并能将收到的所有值都封装到组中。

def make_pizza(size, *toppings):
    print("\nMaking a " + str(size) +
          "-inch pizza with the following toppings:")
    for topping in toppings:
        print("- " + topping)
make_pizza(16,'peperoni')
make_pizza(12, 'mushrooms', 'green peppers', 'extra cheese')
# 结合使用位置实参和任意数量实参。

def build_profile(first, last, **user_info):
    profile = {}
    profile['first name'] = first
    profile['last name'] = last
    for key, value in user_info.items():
        profile[key] = value
    return profile
user_profile = build_profile('albert', 'einstein',
                             location= 'princeton',
                             field= 'physics')
print(user_profile)
# **用于创建字典。编写的内容为先创建一个名为profile的空字典。
# 再一步步把first,last，use_info变成可以容纳到新字典profile中的格式。
# 最后返回profile，完成全部的字典格式转换。
# 原书8.5最后一个例子。

# 模块的使用见文件，pizza1和making_pizza。
# 第八章小结： 编写函数，传递实参，显示输出函数和返回值，结合使用列表/字典/while/if，模块。

class Dog():
    def __init__(self, name, age):
        self.name = name
        self.age = age
    def sit(self):
        print(self.name.title() + " is now sitting.")
    def roll_over(self):
        print(self.name.title() + " rolled over!")
# 类的定义。
my_dog = Dog('willie', 6)
print("My dog's name is " + my_dog.name.title() + ".")
print("My dog is " + str(my_dog.age) + " years old.")

my_dog.name
my_dog.sit()
your_dog = Dog('lucy', 3)

class Car():
    def __init__(self, make, model, year):
        self.make = make
        self.model = model
        self.year = year
        self.odometer_reading = 0
    def get_descriptive_name(self):
        long_name = str(self.year) + ' ' + self.make + ' ' + self.model
        return long_name.title()
    def read_odometer(self):
        print("This car has " + str(self.odometer_reading) + " miles on it.")
    def update_odometer(self, mileage):
        # 增加参数。
        if mileage >= self.odometer_reading:
            # 禁止回调。
            self.odometer_reading = mileage
        else:
            print("You can't roll back an odometer!")
    def increment_odometer(self, miles):
        # 用于递增属性值。
        self.odometer_reading += miles
my_new_car = Car('audi', 'a4', 2016)
print(my_new_car.get_descriptive_name())
my_new_car.read_odometer()

my_new_car.odometer_reading = 23
my_new_car.read_odometer()
# 直接修改值。
my_new_car = Car('audi', 'a4', 2016)
my_new_car.update_odometer(23)
my_new_car.read_odometer()
# 通过方法修改属性的值。
my_used_car = Car('subaru', 'outback', 2013)
print(my_used_car.get_descriptive_name())
my_used_car.update_odometer(23500)
my_used_car.read_odometer()
my_used_car.increment_odometer(100)
my_used_car.read_odometer()
# 通过方法对属性的值进行递增。

class Car():
    def __init__(self, make, model, year):
        self.make = make
        self.model = model
        self.year = year
        self.odometer_reading = 0
    def get_descriptive_name(self):
        long_name = str(self.year) + ' ' + self.make + ' ' + self.model
        return long_name.title()
    def read_odometer(self):
        print("This car has " + str(self.odometer_reading) + " miles on it.")
    def update_odometer(self, mileage):
        if mileage >= self.odometer_reading:
            self.odometer_reading = mileage
        else:
            print("You can't roll back an odometer!")
    def increment_odometer(self, miles):
        self.odometer_reading += miles
class ElevtricCar(Car):
    def __init__(self, make, model, year):
        super().__init__(make, model, year)
        # super()用于关联父子。
        self.battery_size = 70
        #子类的新属性以及初始值。
    def describe_battery(self):
        print("This car has a " + str(self.battery_size) + "-kWh battery.")
my_tesla = ElevtricCar('tesla', 'model s', 2016)
print(my_tesla.get_descriptive_name())
my_tesla.describe_battery()

class ElevtricCar(Car):
    def __init__(self, make, model, year):
        super().__init__(make, model, year)
        self.battery_size = 70
    def describe_battery(self):
        print("This car has a " + str(self.battery_size) + "-kWh battery.")
    def fill_gas_tank():
        print("This car does not need a gas tank!")
        # 如果在子类中重新定义了一个父类中同名的方法，则运行子类的。（重写父类方法）

class Car():
    def __init__(self, make, model, year):
        self.make = make
        self.model = model
        self.year = year
        self.odometer_reading = 0
    def get_descriptive_name(self):
        long_name = str(self.year) + ' ' + self.make + ' ' + self.model
        return long_name.title()
    def read_odometer(self):
        print("This car has " + str(self.odometer_reading) + " miles on it.")
    def update_odometer(self, mileage):
        if mileage >= self.odometer_reading:
            self.odometer_reading = mileage
        else:
            print("You can't roll back an odometer!")
    def increment_odometer(self, miles):
        self.odometer_reading += miles
class Battery():
    def __init__(self, battery_size=70):
        self.battery_size = battery_size
    def describe_battery(self):
        print("This car has a " + str(self.battery_size) + "-kWh battery.")
    def get_range(self):
        if self.battery_size == 70:
            range = 240
        elif self.battery_size == 85:
            range = 270
        message = "This car can go approximately " + str(range)
        message += " miles on a full charge."
        print(message)
class ElectricCar(Car):
    def __init__(self, make, model, year):
        super().__init__(make, model, year)
        self.battery = Battery()
# 将大型类拆分成多个协同工作的小类。
my_tesla = ElectricCar('tesla', 'model s', '2016')
print(my_tesla.get_descriptive_name())
my_tesla.battery.describe_battery()
my_tesla.battery.get_range()

