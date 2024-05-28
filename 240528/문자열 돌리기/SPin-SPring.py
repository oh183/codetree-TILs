# get input
string = str(input())

# loop through the string and print 
for _ in range(len(string) + 1):
    print(string)

    # manipulate the string
    endpoint = len(string) - 1 
    string = string[endpoint] + string[0:endpoint]