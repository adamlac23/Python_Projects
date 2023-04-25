name = str(input("Hi, what's your name?\t"))
print('Hello', name)

weight = int(input('Enter your weight in pounds: '))

height = int(input('Enter your height in inches: '))

BMI = (weight * 703) / (height * height)
print('Your BMI is:', BMI)

if BMI > 0:
    if (BMI < 18.5):
        print(name +', you are underweight.')
    elif (BMI < 24.9):
        print(name +', your BMI is normal.')
    elif (BMI < 29.9):
        print(name +', you are overweight.')
    elif (BMI < 34.9):
        print(name +', you are obese.')
    elif (BMI < 39.9):
        print(name +', you are severely obese.')
    elif (BMI > 40):
        print(name +', you are morbildy obese.')