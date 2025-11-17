# Syed Haroon Haider


print("                                                              PART1")

name = input("enter your name:")

#stripping the name

new_name = name.strip()
print(f"your name is {new_name}")
print(f"cleaned name is {new_name}")

#uppering the case of name

upper = new_name.upper()
print(f"Name in UPPER is {upper}")

#lowering the case of new name
new_name = "HAROON HAIDER"
lower = new_name.lower()
print(f"Name in lower is {lower}")

#name analysis
if "jhon" in new_name:
    print("your name contains jhon")
else:
    print("your name does not contain Jhon")
#printing the first 3 characters of name
name1 = "Haroon Haider!"
first_three = name1[:3]
print(f"the first three characters are {first_three}")

#printing the last three characters
last_three = name1[10:13]
print(f"the last 3 characters are {last_three}")


#name with underscore
name2 = "Haroon Haider"
name3 = name2.replace(" ", "_")
print(f"name with underscore {name3}")
print("parts of your name:")
name4 = name2.split(" ")
print(name4)

print("                                                   PART2")

#entering the age from user input
age = input("enter your age:")
print(f"your age is {age}")

#entering the height
height = int(input("enter your height in cms:"))
height_in_cms = height / 100
print(f"your height is {height} ({height_in_cms})")

#enter the fav quote
quote = "A pessimist sees the difficulty in every opportunity. An optimist sees the opportunity in every difficulty."
print(f"enter your favourite quote: {quote}")
print(f"your quote with single quotes is '{quote}'")
length = len(quote)
print(f"the length of your quote is {length}")


print("                                   ............FINAL SUMMARY...........")
print(f"Full name        :{name2}")
print(f"Age              :{age}")
print(f"Height           :{height}({height_in_cms})")
print(f"Favourite quote  :{quote}")




