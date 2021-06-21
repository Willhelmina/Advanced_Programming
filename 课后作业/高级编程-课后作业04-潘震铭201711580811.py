
import calendar
from datetime import date
print(calendar.calendar(2021))





str = '               '
print(len(str))



days = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31] #
weekdays = ['Mo', 'Tu', 'We', 'Th', 'Fr', 'Sa', 'Su'] 
months = ['January', 'February', 'March', 'April', 'May', 'June', 'July', 'August', 'September', 'October', 'November', 'December']

lst_j = [4, 3, 3, 4]

print(2021)
print()

for x in range(0, 4): 
    lst= [1, 1, 1]
    j = lst_j[x]
    if x==0:
        print("     {:^10}                {:^10}                {:^10}".format(months[0], months[1], months[2]))
    if x==1:
        print("     {:^10}                {:^10}                {:^10}".format(months[3], months[4], months[5]))
    if x==2:
        print("     {:^10}                {:^10}                {:^10}".format(months[6], months[7], months[8]))
    if x==3:
        print("     {:^10}                {:^10}                {:^10}".format(months[9], months[10], months[11]))
    print("Mo Tu We Th Fr Sa Su      Mo Tu We Th Fr Sa Su      Mo Tu We Th Fr Sa Su")
    for i in range(0, 6):
        if i == 0:
            for q in range(0, 3): 
                m = x*3 + q 
                print(" "*3*j, end = "")
                for w in range(1, 8):
                    print("{:>2} ".format(w), end="")   
                    j+=1
                    if j == 7:
                        print(" "*5, end = "")
                        j = (days[m]-w)%7
                        m += 1
                        lst[q] = w
                        break
                                             
        else:
            for q in range(0, 3): 
                m = x*3 + q
                for w in range(1, 8):
                    if w+lst[q] <= days[m]:
                        print("{:>2} ".format(w+lst[q]), end="")   
                    else:
                        print("{:>2} ".format(" "), end="")
                print(" "*5, end = "")
                lst[q] = w+lst[q]         
        print()
    print()

