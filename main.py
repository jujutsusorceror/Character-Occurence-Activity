text = input("Enter the text:")
c = input("Enter the character:")

i = 0
count = 0

while i <len(text):
    if text[i] == c: 
        count += 1
    i += 1
        
print(f"{c} has appeared {count} number of times.")