
def calculate_bmi(weight, height):
    bmi = weight / (height ** 2)
    return bmi

def bmi_category(bmi):
    if bmi < 18.5:
        return "Underweight", "Increase nutritious food intake."
    elif 18.5 <= bmi < 24.9:
        return "Normal", "Maintain healthy lifestyle."
    elif 25 <= bmi < 29.9:
        return "Overweight", "Follow diet and exercise regularly."
    else:
        return "Obese", "Consult a doctor and monitor diet."
print("---- Patient BMI Health Monitoring ----")
name = input("Enter Patient Name: ")
age = int(input("Enter Age: "))
height = float(input("Enter Height (in meters): "))
weight = float(input("Enter Weight (in kg): "))

bmi = calculate_bmi(weight, height)
category, advice = bmi_category(bmi)

print("\n----- Health Report -----")
print(f"Patient Name: {name}")
print(f"Age: {age}")
print(f"BMI Value: {bmi:.2f}")
print(f"Health Category: {category}")
print(f"Suggested Advice: {advice}")
