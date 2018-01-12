if True:
    print("Answer");print("true")
else:
    print("anser")
    print("false")

days=['Monday','Tuesday',
'Wednesday','Thursday']

for i in days:
    print(i)

num = 2 #raw_input("Enter a number  :")
while(num<5):
    num+=1
    print("====output with index===")
    for idx in range(len(days)):
        print(days[idx])
