def display_list(items):
    print("list contents  :",items)
def display_tuple(items):
    print("tuple contents :",items)
def display_dictionary(items):
    print("dictionay contents  :",items)
n=int(input("enter no of integars:"))
numbers=[int(input(f"enter elemant{i+1}:"))for i in range(n)]
value=int(input("enter value to insert"))
position=int(input("enter position(0-based):"))
if 0<=position<=len(numbers):
    numbers.insert(position,value)
else:
    print("invalid position:")
value=int(input("enter elemant to delete:"))
if value in numbers:
    numbers.remove(value)
else:
    print("elemant not foiund:")
numbers.sort()
print("sorted list  :",numbers)
numbers.reverse()
print("reversed list  :",numbers)
names=tuple(input("enter student name seperated by space:").split())
print("tuples:",names)
search_name=input("enter name to count:")
print("count:",names.count(search_name))
index_name = input("enter name to find index:")
if index_name in names:
 print("Index:", names.index(index_name))
else:
 print("Name not found")
students = {"4MT26CS001": "Ananya", "4MT26CS002": "Rahul"}
new_usn = input("Enter new USN: ")
new_name = input("Enter new student name: ")
students[new_usn] = new_name
update_usn = input("Enter USN to update: ")
if update_usn in students:
 students[update_usn] = input("Enter updated name: ")
else:
    print("usn not found")
delete_usn = input("Enter USN to delete: ")
if delete_usn in students:
 del students[delete_usn]
else:
 print("USN not found")
print("Keys :", list(students.keys()))
print("Values:", list(students.values()))
display_list(numbers)
display_tuple(names)
display_dictionary(students)