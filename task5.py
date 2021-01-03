from task4 import*
from tast1 import*
def get_movie_list_details(movies):
    movie_list = []
    for i in movies[:10]:
        Url = scrap_movie_details(i['url'])
        movie_list.append(Url)
    return (movie_list)
# pprint.pprint(get_movie_list_details(Movies_details))
Get_Details_Movies = get_movie_list_details(Movies_details)
# pprint.pprint(Get_Details_Movies)

















