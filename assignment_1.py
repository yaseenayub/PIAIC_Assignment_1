#Finds a given word in a given string
def find(string, valueToBeFound):
    string = string.split()
    i = 0
    while(i < len(string)):
        if(string[i] == valueToBeFound):
          return valueToBeFound
        i += 1
    return "not found"



#example calls

print(find("yaseen is my friend","friend"))

print(find("yaseen is my friend","frind"))
