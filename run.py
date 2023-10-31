# Collect User Information
def get_user_info():
    name = input("Enter your name: ")
    email = input("Enter your email address: ")
    weight = float(input("Enter your weight in kg: "))
    height_cm = float(input("Enter your height in cm: "))
    return name, email, weight, height_cm

# Calculate BMI
def calculate_bmi(weight, height_cm):
    height_m = height_cm / 100
    
    bmi = weight / (height_m ** 2) 
    return bmi

# Determine BMI category  
def get_bmi_category(bmi):
    if bmi < 18.5:
        return "underweight"
    elif 18.6 <= bmi <= 24.9:
        return "normal"
    elif 25 <= bmi <= 29.9:
        return "overweight"
    else:
        return "obese"            

# Function to gather additional health information
def gather_health_info():
    health_info = {}
    
    print("Additional Health Information:")
    print("==============================")
    
    # Physical Activity
    print("1. How often do you engage in physical activity or exercise?")
    print("   a) Daily")
    print("   b) A few times a week")
    print("   c) Rarely")
    answer = input("Enter your answer (a, b, or c): ").strip().lower()
    health_info["physical_activity"] = answer
    
    # Diet and Nutrition
    print("2. How would you describe your daily diet?")
    print("   a) Balanced")
    print("   b) Vegetarian")
    print("   c) High-protein")
    answer = input("Enter your answer (a, b, or c): ").strip().lower()
    health_info["diet_description"] = answer
    
    print("3. How many servings of fruits and vegetables do you consume in a day?")
    print("   a) 3 or more servings")
    print("   b) 1-2 servings")
    print("   c) Less than 1 serving")
    answer = input("Enter your answer (a, b, or c): ").strip().lower()
    health_info["fruits_vegetables_servings"] = answer
    
    print("4. Do you have any dietary restrictions or food allergies?")
    print("   a) No")
    print("   b) Yes, dietary restrictions")
    print("   c) Yes, food allergies")
    answer = input("Enter your answer (a, b, or c): ").strip().lower()
    health_info["diet_restrictions"] = answer
    
    print("5. How often do you eat fast food?")
    print("   a) Once a month or less")
    print("   b) Once or twice a week")
    print("   c) Daily or very often")
    answer = input("Enter your answer (a, b, or c): ").strip().lower()
    health_info["fast_food_frequency"] = answer
    
    print("6. How often do you drink soft drinks?")
    print("   a) Never or almost never")
    print("   b) Sometimes like once or twice a week")
    print("   c) Daily or very often")
    answer = input("Enter your answer (a, b, or c): ").strip().lower()
    health_info["soft_drinks_frequency"] = answer
    
    # Gathered information
    return health_info

# Collect user information (as before)
name, email, weight, height_cm = get_user_info()
bmi = calculate_bmi(weight, height_cm)
bmi_category = get_bmi_category(bmi)

# Display BMI category
print(f'Hello, {name}, your BMI is {bmi:.2f} and your BMI category is {bmi_category}')

# Ask lifestyle questions and provide recommendations (as before)
ask_lifestyle_questions(bmi_category)

# Gather additional health information
health_info = gather_health_info()

# Display gathered health information
print("\nGathered Health Information:")
for key, value in health_info.items():
    print(f"{key}: {value}")
