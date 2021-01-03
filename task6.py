from task4 import*
from tast1 import*

def analyse_movies_language(movies):
    analys_dis={}
	for dis in movies:
		for language in	dis['local_details']['language']:
			if language in analys_dis:
				analys_dis[language]+=1
			else:
				analys_dis[language]=1
	return analys_dis

pprint.pprint(analyse_movies_language(details_of_movie))