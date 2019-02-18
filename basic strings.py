#find count of vowels in a string
def vowels(string):
    lst=['a','e','i','o','u']
    count=0
    for i in string:
        if i in lst:
           count+=1
    return count
#print(vowels("Hamza Hoda"))

#reverse a string
def reverse(string):
    newString=''
    length=len(string)-1
    while length>=0:
        newString = newString+string[length]
        length = length-1
    return newString
#print(reverse("Hoda"))
