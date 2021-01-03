from tast1 import*
from task2 import*

def group_by_decade(movies):
    
    list1=[]
    for i in movies:
        # return i
        print(i["year"])
        mod = i["year"] % 10
        # print(mod)
        decade = i["year"]-mod
        # print(decade)
        if decade not in list1:
            list1.append(decade)
    # return list1
    list1.sort()
    # return list1
    # print(list1)
    moviedec={}
    for j in list1:
        moviedec[j]=[]
    # return moviedec
    # print(moviedec)
    for x in moviedec:
        dec10 = x+9
        # print(i["year"])
        # print(dec10)
    # return dec10
        for y in movies:
            # print(y["year"])
            if y["year"] <= dec10 and y["year"] >= x:
                print(y["year"])
                # for v in movies[y]:
                moviedec[x].append(y)
    return moviedec
# pprint.pprint(group_by_decade(Movies_details))

Year_Dec10=(group_by_decade(Movies_details))
# pprint.pprint(Year_Dec10)


