python = [
    ['Q1. What is a correct syntax to output "Hello World" in Python? ',
     '1. echo "Hello World" ',
     '2. p("Hello World") ',
     '3. echo("Hello World"); ',
     '4. print("Hello World")', 4],

    ['Q2. How do you insert COMMENTS in Python code?',
     '1. /*This is a comment*/',
     '2. #This is a comment',
     '3. //This is a comment',
     '4. Nota', 2],

    ['Q3. Which one is NOT a legal variable name?',
     '1. my_var',
     '2. my-var',
     '3. Myvar',
     '4. _myvar', 2],

    ['Q4. How do you create a variable with the numeric value 5?',
     '1. x = 5',
     '2. x = int(5)',
     '3. Both the other answers are correct',
     '4. Nota', 3],

    ['Q5. What is the correct file extension for Python files?',
     '1. .pyt',
     '2. .py',
     '3. .pyth',
     '4. .pt', 2],

    ['Q6. How do you create a variable with the floating number 2.8?',
     '1. x = 2.8',
     '2. Both the other answers are correct',
     '3. x = float(2.8) ',
     '4. Nota', 2],

    ['Q7. What is the correct syntax to output the type of a variable or object in Python?',
     '1. print(typeof(x))',
     '2. print(typeOf(x))',
     '3. print(type(x))',
     '4. print(typeof x)', 3],

    ['Q8. What is a correct syntax to return the first character in a string?',
     '1. x = sub("Hello", 0, 1)',
     '2. x = "Hello"[0]',
     '3. x = "Hello".sub(0, 1)',
     '4. Nota', 2],

    ['Q9. Which method can be used to remove any whitespace from both the beginning and the end of a string?',
     '1. len()',
     '2. ptrim()',
     '3. trim()',
     '4. strip()', 4],

    ['Q10. Which method can be used to return a string in upper case letters?',
     '1. toUpperCase()',
     '2. upper()',
     '3. uppercase()',
     '4. upperCase()', 2],

    ['Q11. Which method can be used to replace parts of a string?',
     '1. repl()',
     '2. replaceString()',
     '3. replace()',
     '4. switch()', 3],

    ['Q12. Which operator can be used to compare two values?',
     '1. ><',
     '2. = ',
     '3. <>',
     '4. ==', 4],

    ['Q13. Which of these collections defines a DICTIONARY?',
     '1. ("apple", "banana", "cherry")',
     '2. {"apple", "banana", "cherry"}',
     '3. {"name": "apple", "color": "green"}',
     '4. ["apple", "banana", "cherry"]', 3],

    ['Q14. Which collection is ordered, changeable, and allows duplicate members?',
     '1. LIST',
     '2. DICTIONARY',
     '3. TUPLE',
     '4. SET', 1],

    ['Q15. Which collection does not allow duplicate members?',
     '1. None',
     '2. LIST',
     '3. TUPLE',
     '4. SET', 4]
]

levels = [1000, 2000, 5000, 10000, 20000, 40000, 80000, 160000, 320000, 640000, 1250000, 2500000, 5000000, 10000000, 7000000000]

money = 0

name = input("Enter your Full Name: ")
dob = input("Enter your DOB in DD/MM/YYYY.\nFor example, if your date of birth is 8 of August 2007, write it as 08/08/2007: ")
print(f"Welcome to Kaun Banega Arabpati.\nDear {name}, you registered successfully. Let's start!")

for i in range(0, len(python)):
    question = python[i]
    print(f"Question For Rs.{levels[i]}")
    print(question[0])
    print(f" {question[1]}             {question[2]} ")
    print(f" {question[3]}             {question[4]} ")
    reply = int(input("Enter your answer (1-4) or 0 to quit:\n"))
    if reply == 0:
        if i == 0:
            money = 0
        else:
            money = levels[i-1]
        break
    if reply == question[-1]:
        print(f"Correct answer, you have won Rs. {levels[i]}")
        if i == 3:
            money = 10000
        elif i == 9:
            money = 320000
        elif i == 14:
            money = 10000000
        elif i == 15:
            money = 7000000000
    else:
        print("Wrong answer!")
        break

if reply == 0:
    print(f"Better Luck Next Time. You won Rs.{money}")
elif i == 15:
    print(f"Congratulations {name}, DOB {dob}.\nYou answered all the questions.\nYou won our Maha Dhan Rashi.\n\n\n\nRs.{money}")
elif i >= 4 and i < 10:
    print(f"Congratulations {name}, DOB {dob}.\nYou answered stage 1 questions.\nYou won our Ararambh Dhan Rashi.\n\n\n\nRs.{money}")
elif i >= 10 and i < 15:
    print(f"Congratulations {name}, DOB {dob}.\nYou answered Stage 2 questions.\nYou won our Madhyam Dhan Rashi.\n\n\n\nRs.{money}")
elif i >= 0 and i < 4:
    print(f"Better Luck Next Time. You won Rs.{money}")

heart = "❤️"
print(f"Thanks for playing this quiz \n Made by Ishant with {heart}  in India")
