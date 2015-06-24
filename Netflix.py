#!/usr/bin/env python3
import json
import os
from pprint import pprint
from math import sqrt

global simple_user_cache
global simple_movie_cache
global expected_results
if "TRAVIS_CACHE" in os.environ :
	cache_path = os.environ["TRAVIS_CACHE"]
else :
	cache_path = "/u/ebanner/netflix-tests"
with open(cache_path+'/ezo55-Average_Viewer_Rating_Cache.json') as url :
	simple_user_cache = json.load(url)
with open(cache_path+'/BRG564-Average_Movie_Rating_Cache.json') as url2 :
	simple_movie_cache = json.load(url2)
with open(cache_path+'/pam2599-probe_solutions.json') as url3 :
	expected_results = json.load(url3)

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

def netflix_calc(i, j) :
	return (2 * i + j) / 3 

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
	global expected_results
	current_movie_rating = 0
	current_user_rating = 0
	actual_user_rating = 0
	user_rating_guess = 0
	rmse_count = 0
	rmse_total = 0
	for s in r :
		if rep_int_check(s) is False :
			v = s[:-2]
			current_movie_rating = int(v)
			current_movie_rating = simple_movie_cache.get(str(v))
			w.write(str(s))
		else :
			q = int(s)
			current_user_rating = simple_user_cache.get(str(q))
			user_rating_guess = netflix_calc(current_user_rating,current_movie_rating)
			w.write(str(user_rating_guess)+'\n')
			actual_user_rating = expected_results.get(str(v)).get(str(q))
			rmse_count += 1
			rmse_total += (float(user_rating_guess) - float(actual_user_rating))**2
	rmse_ans = sqrt((rmse_total/rmse_count))
	real_rmse = round(rmse_ans, 2)
	w.write(str(real_rmse)+'\n')