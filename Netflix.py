#!/usr/bin/env python3
import urllib
import json
import requests
from urllib.request import urlopen
import os
import pickle
from pprint import pprint

global simple_user_cache
global simple_movie_cache
with open('/u/ebanner/netflix-tests/ezo55-Average_Viewer_Rating_Cache.json') as url :
	simple_user_cache = json.load(url)
with open('/u/ebanner/netflix-tests/BRG564-Average_Movie_Rating_Cache.json') as url2 :
	simple_movie_cache = json.load(url2)

#
# rep_int_check
#

def rep_int_check(str) :
	try :
		int(str)
		return True
	except :
		return False

#
# netflix_calc
#

#def netflix_calc(i, j) :

#
# netflix_rmse
#

#def netflix_rmse(x, y) :

#
# netflix_print
#

#def netflix_print(w, q, r, s) :

#
# netflix_solve
#

def netflix_solve(r, w) :
	global simple_user_cache
	global simple_movie_cache
	current_movie_rating = 0
	current_user_rating = 0
	for s in r :
		if rep_int_check(s) is False :
			v = s[:-2]
			current_movie_rating = int(v)
			#print(v)
			current_movie_rating = simple_movie_cache.get(str(v))
			#print(current_movie_rating)
		else :
			q = int(s)
			#print(q)
			current_user_rating = simple_user_cache.get(str(q))
			#print(current_user_rating)
	w.write("1\n")