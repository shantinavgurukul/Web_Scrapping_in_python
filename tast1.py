from bs4 import BeautifulSoup
import requests
import pprint
url=("https://www.imdb.com/india/top-rated-indian-movies/")
req=requests.get(url)
# print(req)
a=req.text 
# print(a)
soup=BeautifulSoup(req.text,"html.parser")
# print(soup)  
def scrap_top_list():
    main_div=soup.find("div",class_="lister")
    # return main_div
    tbody=main_div.find("tbody",class_="lister-list")
    # return tbody
    trs=tbody.find_all("tr")
    # return trs

    movie_ranks=[]
    movie_name=[]
    year_of_realease=[]
    movie_urls=[]
    movie_ratings=[]

    for tr in trs:
        # return tr# details = {"position":"","name":"","year":"","rating":"","url":""}

        position=tr.find("td", class_="titleColumn").get_text().strip()
        # return position
        rank=""
        for i in position:
            if "." not in  i:
                rank=rank+i
            else:
                break
        movie_ranks.append(rank)
    # return movie_ranks# details = {"position":"","name":"","year":"","rating":"","url":""}

        title=tr.find("td",class_="titleColumn").a.get_text()
        # return title
        movie_name.append(title)
        # return movie_name
        year = tr.find("td",class_="titleColumn").span.get_text()
        # return year
        year_of_realease.append(year)
    # return year_of_realease
        imdb_rating=tr.find("td",class_="ratingColumn imdbRating").strong.get_text()
        # return imdb_rating
        movie_ratings.append(imdb_rating)
        # return movie_ratings
        link = tr.find("td",class_="titleColumn").a["href"]
        # return link
        movie_link = "https://www.imdb.com"+link
        # return movie_link
        movie_urls.append(movie_link)
    # return movie_urls

    Top_movie=[]
    # details = {}
    for s in range(0,len(movie_ranks)):
        details = {}
        details["position"] = movie_ranks[s]
        details["name"] = movie_name[s]
        year_of_realease[s]=year_of_realease[s][1:5]
        details["year"] = int(year_of_realease[s])
        details["rating"] = float(movie_ratings[s])
        details["url"] = movie_urls[s]
        Top_movie.append(details)
    return Top_movie
# pprint.pprint(scrap_top_list())  

Movies_details = scrap_top_list()
# pprint.pprint(Movies_details)