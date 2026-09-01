# Task 1 and 2: Basic Stress and Strain Calculator

print ("STRESS AND STRAIN CALCULATOR")

while True:
  print("\nSelect Material:")
  print("1. Steel")
  print("2. Aluminum")
  print("3. Custom Material")
        
  while True:
    material_choice = input("Enter Choice (1-3): ")

    if material_choice == "1":
      material = "Steel"
      break

    elif material_choice == "2":
      material = "Aluminum"
      break

    elif material_choice == "3":
      material = input("Enter custom material name: ")
      break

    else:
      print("Invalid choice. Please enter 1, 2, or 3.")
      
  while True:
    try:
      force = float(input("\nEnter applied force (N): "))

      if force < 0:
        print("Error: Force cannot be negative.")
      else:
        break

    except ValueError:
      print("Error: Please enter a valid number.")

  while True:
    try:
      area = float(input("Enter cross-sectional area (m^2): "))

      if area <= 0:
        print("Error: Area must be greater than 0.")
      else:
        break

    except ValueError:
      print("Error: Please enter a valid number.")

  while True:
    try:
      original_length = float(input("Enter original length (m): "))

      if original_length <= 0:
        print("Error: Original length must be greater than 0.")
      else:
        break

    except ValueError:
      print("Error: Please enter a valid number.")

  while True:
    try:
      change_length = float(input("Enter change in length (m):"))

      if change_length < 0:
        print("Error: Change in length cannot be negative.")
      else:
        break

    except ValueError:
      print("Error: Please enter a valid number.")
    

  stress = force/area
  strain = change_length/original_length

  print("\nRESULTS")
  print(f"Stress = {stress:.2f}Pa")
  print(f"Strain = {strain:.6f}")

  while True:
    again = input("\nDo you want to perform another calculation? (y/n): ").lower()

    if again == "y":
      break

    elif again == "n":
      print("Program Terminated!")
      break

    else:
      print("Invalid choice! Please enter 'y' or 'n'.")

  if again == "n":
    break
