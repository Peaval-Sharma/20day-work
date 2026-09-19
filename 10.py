a={}
n=int(input("Enter the quantity of contact numbers: "))
for i in range(n):
    name=input(f"Enter name of person {i+1}: ")
    number=int(input(f"Enter the number of person{i+1}: "))
    a[name]=number
    # Displaying the contact numbers
print("Contact Numbers:")
for name, number in a.items():
    print(f"{name}: {number}")
    # Searching a contact number
search=input("\nEnter the name of the person to search: ")
if search in a:
    print(f"{search}: {a[search]}")
else:
    print("Person not found.")
    #logic to remmove a contact number
remove=input("\nEnter the name of the person to remove: ")
if remove in a:
    del a[remove]
    print(f"{remove} has been removed from the contact list.")
else:
    print("Person not found.")
    #logic to update a contact number
update=input("\nEnter the name of the person to update: ")
if update in a:
    new_number=int(input(f"Enter the new number for {update}: "))
    a[update]=new_number
    print(f"{update}'s number has been updated to {new_number}.")
    print("Updated Contact Numbers:")
    print("thank you for using the contact management system.")