from collections import Counter
def most_frequent(string="Mississippi"):
    print("Please enter a string" '\n' ,string)
most_frequent()    
#letter counter in decreasing order   
string = "Mississippi"
string_length = Counter(string)

print(string_length)
    