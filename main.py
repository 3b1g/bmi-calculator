# Constant Variables
MINI_VALUE = 18.5
MAXI_VALUE = 24.9




# Getting Proper Height and Mass from the person

while True:
    try:
        height = float(input('Enter Your Height in Meters: '))
        mass = float(input('Enter Your Mass in Kilograms: '))

        # Check if height and weight are greater than zero
        if height <= 0 or mass <= 0:
            print('Height and Mass must be greater than zero.')
        else:
            break
    except ValueError:
        print('Please enter valid numeric values for Height and Mass.')
    except KeyboardInterrupt:
        # Handle Ctrl+C gracefully
        print('Operation canceled.')
        exit(1)    
    

# Defining a BMI Calculator function
def bmi_calc(height, mass):
    bmi = mass / height ** 2
    return bmi

bmi = bmi_calc(height, mass)

# Condition statements to check BMI category
if bmi < MINI_VALUE:
    category = 'Underweight'
elif MINI_VALUE <= bmi <= MAXI_VALUE:
    category = 'Normal Weight'
else:
    category = 'Overweight'

# Display BMI and category
print(f'Your BMI is: {bmi:.2f}')
print(f'You are in the "{category}" category.')