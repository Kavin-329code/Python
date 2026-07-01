print("Welcome SmartFit Digital Fitness \n")
your_name = input("Please enter your name: \n")# "n" is used to create a new line to make code clear

print(f"Hello, {your_name}! Welcome to Smartfit. Let's get started with your fitness journey. \n")
print ("please enter your age for couch to create a better exercise for you: \n")
age = int(input ("Age: ")) # we use int() to make sure only number are entered for age and not strings
has_medical_condition = input("Do you have any medical conditions? (yes/no): ").lower()

if has_medical_condition not in ["yes", "no"]: #it checks if what user entered is in the list if not it will print the statement below.
    print("Invalid input. Please enter 'yes' or 'no'.")


print ("SmartFit offers two types of membership: Basic and Premium. \n")


print(f"Great! {your_name} You are {age} years old and has {has_medical_condition} medical conditions. We will create a personalized exercise plan for you that fits your needs and health. \n")


membership = input("Please select your  membership choice type (Basic/Premium): ").lower()

#Evaluating membership of which user wants
# 1. Basic

if membership == "basic":
    personal_training = input("Would you like to include personal training sessions? (yes/no): ").lower()

    if personal_training == "yes": #nested condition since it is inside if statement
        print("Basic plan with personal training: $45 per month.")
    else:
        print("Basic plan without personal training: $30 per month.") # Basic plan without personal training

        print ("Consider upgrading to Premium for more benefits!") #print's this statement whenever a user selects basic training without personal training


# 2. Premium

elif membership == "premium":
    print("Premium plan: $60 per month.")
    if age < 30: # a nested condition since it is inside elif 
        print("You qualify for a youth discount! 10% off your plan.")

    if membership == "premium" and has_medical_condition== "yes":
        print("We recommend a free consultation before starting.")

#now here we evaluste the age of the user to determine which fitness program they are eligible for.

if age < 18:
    print ( "You are eligible for the Teen Fitness Program.")

    

elif age >= 18 and age < 40: #use of logical operator to check if age is between 18 and 40
    print ("You are eligible for the Regular Fitness Program.")


else:
    print ("You are eligible for the Senior Wellness Program.")


#here we evaluate medical conditions of our user for deetermining what next step for each individual

    
if age >= 40 and has_medical_condition == "yes": #both conditions must be true 
    print("Medical clearance required before joining.")

elif age < 40 or has_medical_condition == "no": #if one of the conditions is true, the user can proceed with registration
    print("You can proceed with registration.")


# The above program checks medical conditions  of users not just at age 40 but also above it and below it.