#CODE ALONG: Create a minion class with several attributes - some that are the same 
#for every minion, and some that are different. 
#Create an instance of the class (an object!) and print it to the console.
#The above is the work we did in class, just copy paste it for reference.





#If time permits, continue adding attributes after the whole class portion is done.
#Otherwise, remember you must at least finish the mild task below.


#YOUR TASK: Complete the following to the best of your ability. Thank you to
#			Ms. Shuman for her example tasks!
#MILD 🌶

#1. Create a class called Student that has two attributes: a name, and a grade.
class Student:
    def __init__(self, name, grade):
        self.name = name
        self.grade = grade


# Now create instances of three different students (student1, student2, and student3).
student1 = Student("Alli", 9)
student2 = Student("Berry", 10)
student3 = Student("Carl", 11)


#Confirm that the class works by printing out the first student's name.
print(student1.name)



# MEDIUM 🌶🌶

#2. Create a class called School that has three attributes: a name, a type, and
#	a size (number of students).
class School:
    def __init__(self, name, sType, sSize):
        self.name = name
        self.type = sType
        self.size = sSize


#Create instances of three individual schools.
school1 = School("Stuyvsant", "Public", 2000)
school2 = School("Syosset", "Private", 1000)
school3 = School("BMCC", "Community", 4000)


#Confirm that the class works by printing out the name and size of the third school.
print(school3.name + " and " + str(school3.size))


###
#3. Create a class called House that has four attributes: an address, a number
#	of bathrooms, a price, and a number of bedrooms.
class House:
    def __init__(self, address, bathroom, price, bedroom):
        self.address = address
        self.bathroom = bathroom
        self.price = price
        self.bedroom = bedroom


#Create instances of at least three individual houses.
house1 = House("9 East 71st Street, Manhattan, New York City", 6, "20000000", 7)
house2 = House("Some address", 12, "1", 10)
house3 = House("Another random address", 1, "9999999999", 0)


#Confirm that the class works by printing out the address and size of the second house.
print(house2.address + " and " + str(house2.bathroom))


#SPICY 🌶🌶🌶

#4. Put your three students in a list called my_students, your houses in a list
#	for houses, and your schools in a list for schools.
my_students = [student1, student2, student3]
houses = [houses1, houses2, houses3]
schools = [school1, school2, school3]


#Iterate (this means use a loop!) over the student list, printing out "_____ is in
#grade __." For each of the students.
for student in my_students:
    print("")


#Iterate over the houses list and print out a description for each one. Do the same
#for your schools lists.



###
#5. Modify your student class above to include a savings_account value for each
#	student. Change your initializers so that the code still runs. 



#Write some code that compares a student and a house, and determines whether or not
#the student can afford to buy the house. 