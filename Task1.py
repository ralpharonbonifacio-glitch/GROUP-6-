# Task 1 and 2: Basic Stress and Strain Calculator

print ("STRESS AND STRAIN CALCULATOR")

calculation_history = []
materials_used = set()

units = ("N", "m^2", "m", "Pa")

while True:
  print("\nSelect Material:")
  print("1. Steel")
  print("2. Aluminum")
  print("3. Custom Material")
        
  while True:
    material_choice = input("Enter Choice (1-3): ")

    if material_choice == "1":
      material = "Steel"
      youngs_modulus = 200e9
      yield_strength = 250e6
      break

    elif material_choice == "2":
      material = "Aluminum"
      youngs_modulus = 69e9
      yield_strength = 276e6
      break

    elif material_choice == "3":
      material = input("Enter custom material name: ")

      try:
        youngs_modulus = float(input("Enter Young's Modulus: "))
        yield_strength= float(input("Enter Yield Strength: "))

      except ValueError:
        print("Invalid Material Properties")
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
  safety_factor = yield_strength / stress

  if stress <=yield_strength:
    safety_result = "SAFE"
  else:
    safety_result = "UNSAFE"
  
  test_record = {
    "material": material,
    "force": force,
    "area": area,
    "original_length": original_length,
    "change_length": change_length,
    "stress": stress,
    "strain": strain,
    "youngs_modulus": youngs_modulus,
    "safety_result": safety_result
  }

  calculation_history.append(test_record)
  materials_used.add(material)
  print("="*10)
  print("\nRESULTS")
  print(f"Stress = {stress:.2f}Pa")
  print(f"Strain = {strain:.6f}")
  print(f"Young's Modulus:  {youngs_modulus:.2e} Pa")
  print(f"Factor of Safety: {safety_factor:.2f}")
  print(f"Safety Result: {safety_result}")

  while True:
    print("\nWhat would you like to do?")
    print("1. New Calculation")
    print("2. View History")
    print("3. View Session Summary")
    print("4. Exit")

    next_choice = input("Enter choice (1-4):")

    if next_choice == "1":
      break
    
    elif next_choice == "2":
      print("\n CALCULATION HISTORY")
      
      for number, test in enumerate(calculation_history, start=1):
        print(f"\nTest {number}")
        print(f"Material: {test['material']}")
        print(f"Force: {test['force']}{units[0]}")
        print(f"Area: {test['area']}{units[1]}")
        print(f"Original length:  {test['original_length']}{units[2]}")
        print(f"Change in Length: {test['change_length']}{units[2]}")
        print(f"Stress: {test['stress']:.2f} {units[3]}")
        print(f"Strain: {test['strain']:.6f}")
        print(f"Young's Modulus: {test['youngs_modulus']:.2e} Pa")
        print(f"Safety Results: {test['safety_result']}")
    elif next_choice =="3":
      print("SESSION SUMMARY")
      total_tests = len(calculation_history)
      stresses = []
      for test in calculation_history:
        stresses.append(test["stress"])
      average_stress = sum(stresses)/ len(stresses)
      maximum_stress = max(stresses)
      minimum_stress = min(stresses)

      print(f"Total tests: {total_tests}")
      print(f"Unique materials used: {len(materials_used)}")
      print(f"Average stress: {average_stress:.2f} Pa")
      print(f"Maximum stress: {maximum_stress:.2f} Pa")
      print(f"Minimum stress: {minimum_stress:.2f} Pa")

    elif next_choice == "4":
      print("\nPROGRAM TERMINATED")
      exit()
      
    else:
      print("INvalid Choice. Please enter 1-4 only.")
