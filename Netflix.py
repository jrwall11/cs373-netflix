#!/usr/bin/env python3
import json
import os
from pprint import pprint
from math import sqrt

global simple_user_cache
global simple_movie_cache
global expected_results
global movie_year_cache
global customer_decade_cache
if "TRAVIS_CACHE" in os.environ :
	cache_path = os.environ["TRAVIS_CACHE"]
else :
	cache_path = "/u/ebanner/netflix-tests"
with open(cache_path+'/ezo55-Average_Viewer_Rating_Cache.json') as url :
	simple_user_cache = json.load(url)
with open(cache_path+'/BRG564-Average_Movie_Rating_Cache.json') as url2 :
	simple_movie_cache = json.load(url2)
with open(cache_path+'/drc2582-customer_decade_dict.json') as url4 :
	customer_decade_cache = json.load(url4)
with open(cache_path+'/mw23845-movie_years.json') as url5 :
	movie_year_cache = json.load(url5)
with open(cache_path+'/pam2599-probe_solutions.json') as url3 :
	expected_results = json.load(url3)

#
#              rep_int_check
#
# My rep_int_check function checks if the string
# can be represented as an integer. This helps
# when taking in my RunNetflix.in file bc I can
# extract the movie simply bc it has a : at the
# end of the number. This makes it easy to 
# differentiate b/w Movies & Customers
#

def rep_int_check(str) :
	try :
		int(str)
		return True
	except :
		return False

#
#              netflix_calc
#
# I implemented a lazy solution that involves
# simple mathematics to provide myself with
# a solution. I give priority to the lower
# average b/w the Customer and the Movie
#

def netflix_calc(i, j) :
	return 0.47 * j + 0.53 * i


#
#               netflix_solve
#
# In my netflix_solve method I take in my
# RunNetflix.in file to produce the RunNetflix.out
# I keep count of my total customer ratings 
# and the square of the difference b/w the
# actual result and my guess result I get. Then I
# conclude by taking the root of the mean of the
# sum of my calculations and produce the RMSE.
#

def netflix_solve(r, w) :
	global simple_user_cache
	global simple_movie_cache
	global expected_results
	global movie_year_cache
	global customer_decade_cache
	current_movie_rating = 0
	current_user_rating = 0
	actual_user_rating = 0
	user_rating_guess = 0
	rmse_count = 0
	rmse_total = 0
	current_movie_year = 0
	for s in r :
		if rep_int_check(s) is False :
			v = s[:-2]
			current_movie_rating = int(v)
			current_movie_rating = simple_movie_cache.get(str(v))
			current_movie_year = movie_year_cache.get(str(v))
			w.write(str(s))
		else :
			q = int(s)
			#print(str(q))
			current_user_path = customer_decade_cache.get(str(q))
			current_movie_decade = int(current_movie_year) % 10
			current_movie_year -= current_movie_decade
			current_user_year = current_user_path.get(str(current_movie_year))
			current_user_rating = current_user_year.get('total')/current_user_year.get('count')
			if current_user_rating == 0 :
				current_user_rating = simple_user_cache.get(str(q))
			user_rating_guess = netflix_calc(current_user_rating,current_movie_rating)
			w.write(str(round(user_rating_guess,1))+'\n')
			actual_user_rating = expected_results.get(str(v)).get(str(q))
			rmse_count += 1
			rmse_total += (float(user_rating_guess) - float(actual_user_rating))**2
	rmse_ans = sqrt((rmse_total/rmse_count))
	real_rmse = round(rmse_ans, 2)
	w.write('RMSE: '+str(real_rmse)+'\n')