#Code for Question 1
import statistics
ages = [19, 22, 19, 24, 20, 25, 26, 24, 25, 24]
ages = sorted(ages)
print("The ages list after sorted",ages)
print("The min age in the list is:",min(ages))
print("The max age in the list is:",max(ages))
ages.append(min(ages))
ages.append(max(ages))
print("After adding min and max ages to the list",ages)
print("The sorted ages list after adding min and max ages",sorted(ages))
print("Median of ages",statistics.median(sorted(ages)))
avg = sum(ages)/len(ages)
print("The average is:",avg)
r = range(max(ages)-min(ages))
print("The range is:",r)
print("\n")
#code for Question 2
dog = {}
print("An empty dictionary called dog is created",dog,type(dog))
dog = {'color' : 'white', 'breed' : 'pug', 'legs' : 'short', 'age' : 'twoyears'}
print(dog)

student = {'first_name' : 'Nikhil', 'last_name' : 'Gunda', 'gender' : 'M', 'age' : 23, 'martial status' : 'Not Married',
           'skills' : ['Python','Java'],'Country' : 'India', 'City' : 'Kurnool', 'Address' : 'H:NO 87/209,Madhavi Nagar,B-camp,Kurnool'}
print(student)
print(len(student))
print(student['skills'])
print(type(student['skills']))
student['skills'].append('HTML')
print(student)
print(student.keys())
print(student.values())
print("\n")
#code for Question 3

Sisters = ("Taruni","Udaya","Swarna")
brothers = ("Maruthi","Raju")

print("A tuple is created for sisters",type(Sisters))
print("A tuple is created for Brothers",type(brothers))
print(Sisters)
print(brothers)

Siblings = Sisters + brothers

print("Siblings are:",Siblings)

print("How many siblings do you have?",len(Siblings))

family = list(Siblings)
family.append('Murali')
family.append('Lakshmi')

Family_members = tuple(family)

print("My family members are:",Family_members)
print("\n")
#code for Question 4

it_companies = {'Facebook', 'Google', 'Microsoft', 'Apple', 'IBM', 'Oracle', 'Amazon'}
A = {19, 22, 24, 20, 25, 26}
B = {19, 22, 20, 25, 26, 24, 28, 27}

age = [22, 19, 24, 25, 26, 24, 25, 24]

print("The length of the set is:",len(it_companies))
it_companies.add('Twitter')
print("After adding a value to the set",it_companies)

companies = ['Cognizant','Tata']

it_companies.update(companies)

print("After inserting multiple it companies at once to the set",it_companies)

it_companies.remove('Tata')

print("After removing a company 'Tata' from the it_companies",it_companies)

C = A.union(B)
print("Union of set A and B is",C)

D = A.intersection(B)

print("Intersection of set A and B is",D)

z = A.issubset(B)

print("Is A subset of B?",z)

x=A.isdisjoint(B)
print("Are A and B disjoint sets?",x)

y = A.symmetric_difference(B)

print("What is the symmetric difference between A and B",y)

A.update(B)
print("Join A with B",A)

B.update(A)

print("Join B with A",B)



it_companies.clear()
A.clear()
B.clear()
print("After Deleting the sets completely",A,B,it_companies)

print("Length of the list age",len(age))

myage = set(age)

print("Length of the set age",len(myage))
print("\n")
#code for Question 5

Radius = float(input("Enter the Radius:"))
print("Radius:",Radius)

Area_of_circle = 3.14*Radius*Radius

print("Area of the Circle: ",Area_of_circle)

circum_of_circle = 2*3.14*Radius

print("Circumference of the Circle",circum_of_circle)
print("\n")
#code for Question 6

sentence = "I am a teacher and I love to inspire and teach people"

words = sentence.split()

myset = set(words)

print(words)
print("Unique words",myset)
print("Count of unique words",len(myset))
print("\n")
#code for Question 7

sen1 = "Name\t\tAge\tCountry\tCity"
sen2 = "Asabeneh\t250\tFinland\tHelsinki"

print(sen1)
print(sen2)
print("\n")
#code for Question 8

radius = 10
area = 3.14 * radius ** 2

sentence = "The area of a circle with radius {} is {} meters square."
print(sentence.format(radius,area))
print("\n")
#code for Question 9

lbs = []
wgs = []
n = int(input("Enter the number of students "))

print("\n")
for i in range(0, n):
    print("Enter weight of student", i+1)
    item = float(input())
    lbs.append(item)
print("The weights of students in lbs are ", lbs)

for j in lbs:
    j = float(j/2.205)
    wgs.append(j)
print("The weights of students in kilograms", wgs)