def greeting(name):
  print("Hello, " + name)

#2
import mymodule

mymodule.greeting("Jonathan")

#3
person1 = {
  "name": "John",
  "age": 36,
  "country": "Norway"
}

#4
import mymodule

a = mymodule.person1["age"]
print(a)

#5
import mymodule as mx

a = mx.person1["age"]
print(a)

#6
import platform

x = platform.system()
print(x)

#7
def greeting(name):
  print("Hello, " + name)

person1 = {
  "name": "John",
  "age": 36,
  "country": "Norway"
}

#8
from mymodule import person1

print (person1["age"])