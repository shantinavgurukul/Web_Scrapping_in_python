from tast1 import*
# from task2 import*

def scrap_movie_details(movie_url):
    req=requests.get(movie_url)
    soup = BeautifulSoup(req.text,"html.parser")
    title_div = soup.find("div",class_= "title_wrapper").h1
    a=title_div.get_text()
    # return (a)
    movie_name = ""
    for i in title_div:
        if "(" not in i :
            movie_name = (movie_name +i).strip()
        else:
            break
        # return movie_name
    sub_div = soup.find("div", class_= "subtext")
    runtime = sub_div.find("time").get_text().strip()
    runtime_hours = int(runtime[0])*60
    # return runtime_hours
    movie_runtime = 0
    if "min" in runtime:
        runtime_minutes = int(runtime[3:].strip("min"))
        movie_runtime = runtime_hours +runtime_minutes
    else:
        movie_runtime = runtime_hours
    # return movie_runtime
    gener = sub_div.find_all("a")
    gener.pop()
    movie_gener = [i.get_text()for i in gener]
    # return movie_gener
    summary = soup.find("div",class_= "plot_summary")
    # return summary
    movie_bio = summary.find("div",class_="summary_text").get_text().strip()
    # return movie_bio
    director = summary.find("div",class_="credit_summary_item")
    director_list = director.find_all("a")
    # return director_list
    director_movie = [i.get_text().strip() for i in director_list]
    # return director_movie
    Extra_details = soup.find("div",attrs = {"class":"article","id" : "titleDetails"})
    list_of_divs = Extra_details.find_all("div")
    for divs in list_of_divs:
       
        h4_tags = divs.find_all('h4')
        for h4 in h4_tags:
            # movie_data_dic = {}
            if 'Language:' in h4:
                movie_a_tag = divs.find_all('a')
                movie_language = [Language.get_text() for Language in movie_a_tag]
    # return movie_language  
            elif 'Country:' in h4:
                country_tag = divs.find_all('a')
                movie_country = ''.join([Country.get_text() for Country in country_tag]) 
    # return movie_country 
    movie_poster_link = soup.find("div",class_="poster").a["href"]
    movie_poster = "title/tt0048473/mediaviewer/rm2023787521/" + movie_poster_link
    # return movie_poster
    movie_detail_dic = {}
    movie_detail_dic["name"]= movie_name
    movie_detail_dic["director"] = director_movie
    movie_detail_dic["bio"] = movie_bio
    movie_detail_dic["runtime"] = movie_runtime
    movie_detail_dic["gener"] = movie_gener
    movie_detail_dic["language"] = movie_language
    movie_detail_dic["country"] = movie_country
    movie_detail_dic["poster_url_image"] = movie_poster
    return movie_detail_dic
url1 = ("https://www.imdb.com/title/tt0048473/?pf_rd_m=A2FGELUUNOQJNL&pf_rd_p=690bec67-3bd7-45a1-9ab4-4f274a72e602&pf_rd_r=RJF8Z6ET1WPM1M42SE2G&pf_rd_s=center-4&pf_rd_t=60601&pf_rd_i=india.top-rated-indian-movies&ref_=fea_india_ss_toprated_tt_1")
# pprint.pprint(scrap_movie_details(url1)) 
# scrap_movie_details(url1)
details_of_movie = scrap_movie_details(url1)
# pprint.pprint(details_of_movie)