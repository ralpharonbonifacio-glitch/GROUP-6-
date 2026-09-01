# Task 1: Basic Stress and Strain Calculator

print ("STRESS AND STRAIN CALCULATOR")

force = float(input("Enter applied force (N):"))
area = float(input("Enter cross-sectional area (m^2):"))
original_length = float(input("Enter original length (m):"))
change_length = float(input("Enter change in length (m):"))

stress = force/area

strain = change_length/original_length

print("RESULTS")
print(f"Stress = {stress:.2f}Pa")
print(f"Strain = {strain:.6f}")
