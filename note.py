#use backslash \ to negate single and double quotation mark ex- 'it\'s a sunny day'

#IN function returns in boolean and specifies weather a character is present in string or not
#MY_STR = "HELLO WORLD"
#PRINT("HELLO" IN MY_STR ) returns True

#you can only concatenate same data type like string with string not string with integer first you have to convert integer to string

# += addition and assignment operator at same time 
name = "amit" 
name += str(26)
print(name)

#process of inserting variables in strings is called string intrpolation
sting = f'my name is {name}'
print(sting)

#String slicing lets you extract a portion of a string or work with only a specific part of it. Here's the basic syntax: string[start:stop]
name = "samit"
print(name[1:5])
#it doesnot modify original string ONE MORE SYNTAX FOR STEPING string[start:stop:step]

#isme jo 1 h vo exclusive hota h means 1 wale ko add krta h and stop 5th vale ko exclude rkhta h use include ni krta and if you dont assign value of start it automaticlly refer to as 0
