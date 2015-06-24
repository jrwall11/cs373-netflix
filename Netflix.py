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
	if i % 1 == 0 :
		return i
	else :
		if i < 2 :
			return i
		else :
			if i > 4 :
				return (i + j)/2
			else :
				if i > j :
					return (2*j + i)/3
				else :
					return (2*i + j)/3


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
			w.write(str(round(user_rating_guess,1))+'\n')
			actual_user_rating = expected_results.get(str(v)).get(str(q))
			rmse_count += 1
			rmse_total += (round(float(user_rating_guess),1) - float(actual_user_rating))**2
			#temp = sqrt((rmse_total/rmse_count))
			#print('RMSETEMP: '+str(round(temp,2))+'\n')
	rmse_ans = sqrt((rmse_total/rmse_count))
	real_rmse = round(rmse_ans, 2)
	w.write('RMSE: '+str(real_rmse)+'\n')