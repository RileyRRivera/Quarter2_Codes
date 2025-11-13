students=int(input("Enter number of students:"))
sub=int(input("Enter number of subjects:"))
CA=0
print()
for x in range(1, students+1):
    print("Student", x)
    average=0
    Sum=0
    for y in range(1, sub+1):
        grade=int(input(f"Enter score {y}:"))
        Sum+=grade
        average=Sum/sub
    print(f"Average for Student {students} = {average}")
    CA+=average
    print()
CA=CA/students
print(f"Class Average = {CA}")
