from tast1 import*

def group_by_year(movies):
    group_year = [] 
    year_dic = {}
    for i in movies:
        # print (i)
        years = i["year"]
        if years not in group_year:
            group_year.append(years)
    for p in group_year:
        year_dic[p] = []
        # print (year_dic)
    for j in movies:
        year_list = j["year"]
        for s in year_dic:
            if s == year_list:
                 year_dic[s].append(j)
    return (year_dic)
movies_year = (group_by_year(Movies_details))
# pprint.pprint(movies_year)