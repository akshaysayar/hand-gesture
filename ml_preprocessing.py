cols=[]
for i in range(1,43):
    cols.append("col-"+str(i))
cols.append("target")

cols

p=open("/home/akshay/data/personal/Python_projects/Hand_gesture/data/badiya.csv")
lns = p.readlines()
len(lns)
final = []
final.append(cols)
for i in lns:
    #print(i)
    s=i.split(",")
    s=s[:42]
    print(len(s))
    l=[]
    for i in range(0,42,2):
        print(i)
        print(int(s[i])-int(s[0]))
        print(i+1)
        print(int(s[i+1])-int(s[1]))
        l.append(int(s[i])-int(s[0]))
        l.append(int(s[i+1])-int(s[1]))
    l.append("badiya")
    final.append(l)
final[1]
len(final)

p=open("/home/akshay/data/personal/Python_projects/Hand_gesture/data/yo.csv")
lns = p.readlines()
len(lns)
final_yo = []
#final_yo.append(cols)
for i in lns:
    #print(i)
    s=i.split(",")
    s=s[:42]
    print(len(s))
    l=[]
    for i in range(0,42,2):
        print(i)
        print(int(s[i])-int(s[0]))
        print(i+1)
        print(int(s[i+1])-int(s[1]))
        l.append(int(s[i])-int(s[0]))
        l.append(int(s[i+1])-int(s[1]))
    l.append("yo")
    final_yo.append(l)
final_yo[0]
len(final_yo)



# import csv
# with open(r'/home/akshay/data/personal/Python_projects/Hand_gesture/data/final.csv', 'w') as f:
      
#     # using csv.writer method from CSV package
#     write = csv.writer(f)
      
#     write.writerows(final)
#     write.writerows(final_yo)



p=open("/home/akshay/data/personal/Python_projects/Hand_gesture/data/katti.csv")
lns = p.readlines()
len(lns)
final_katti = []
#final_yo.append(cols)
for i in lns:
    #print(i)
    s=i.split(",")
    s=s[:42]
    print(len(s))
    l=[]
    for i in range(0,42,2):
        print(i)
        print(int(s[i])-int(s[0]))
        print(i+1)
        print(int(s[i+1])-int(s[1]))
        l.append(int(s[i])-int(s[0]))
        l.append(int(s[i+1])-int(s[1]))
    l.append("katti")
    final_katti.append(l)
final_katti[0]
len(final_katti)

p=open("/home/akshay/data/personal/Python_projects/Hand_gesture/data/thumbsup.csv")
lns = p.readlines()
len(lns)
final_thumbsup = []
#final_yo.append(cols)
for i in lns:
    #print(i)
    s=i.split(",")
    s=s[:42]
    print(len(s))
    l=[]
    for i in range(0,42,2):
        print(i)
        print(int(s[i])-int(s[0]))
        print(i+1)
        print(int(s[i+1])-int(s[1]))
        l.append(int(s[i])-int(s[0]))
        l.append(int(s[i+1])-int(s[1]))
    l.append("all the best")
    final_thumbsup.append(l)
final_thumbsup[0]
len(final_thumbsup)

# import csv
# with open(r'/home/akshay/data/personal/Python_projects/Hand_gesture/data/final_2.csv', 'w') as f:
      
#     # using csv.writer method from CSV package
#     write = csv.writer(f)
      
#     write.writerows(final)
#     write.writerows(final_yo)
#     write.writerows(final_katti)


import csv
with open(r'/home/akshay/data/personal/Python_projects/Hand_gesture/data/final_3.csv', 'w') as f:
      
    # using csv.writer method from CSV package
    write = csv.writer(f)
      
    write.writerows(final)
    write.writerows(final_yo)
    write.writerows(final_katti)
    write.writerows(final_thumbsup)