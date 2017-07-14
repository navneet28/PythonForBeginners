try:
    print('10'+10)
#except TypeError/NameError(if variable not defined) as e:
except Exception as e:
    print(str(e))
print('Code continues..')
#multiple except blocks allowed
try:
    x=input('What is your name?')
    print('Name:'+x)
except TypeError as t:
    print('Enter a string for name')
    print(str(t))
digit=upper=lower=special=0
try:
    pwd=input('Enter the password(must contain a special+number+uppercase+lowercase character):\n')
    for c in pwd:
        if c.isdigit():
            digit+=1
        elif c.isupper():
            upper+=1
        elif c.islower():
            lower+=1
        else:
            special+=1
    if digit<1 or upper<1 or lower<1 or special<1:
        raise TypeError("Invalid password")
    else:
        print("Valid password")
except Exception as e:
    print(str(e))
    
