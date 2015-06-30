#!/usr/bin/env python3
from io       import StringIO
from unittest import main, TestCase

from Netflix import rep_int_check, netflix_calc, netflix_solve

# -----------
# TestNetflix
# -----------

class TestNetflix (TestCase) :

	def test_rep_int_check_1(self) :
		s = '2043:\n'
		self.assertEqual(False, rep_int_check(s))

	def test_rep_int_check_2(self) :
		s = '2043\n'
		self.assertEqual(True, rep_int_check(s))

	def test_rep_int_check_3(self) :
		s = '12366\n'
		self.assertEqual(True, rep_int_check(s))

	def test_netflix_calc_1(self) :
		i = 1.0
		j = 1.0
		self.assertEqual(1.0, netflix_calc(i,j))

	def test_netflix_calc_2(self) :
		i = 2.0
		j = 5.0
		self.assertEqual(3.4099999999999997, netflix_calc(i,j))

	def test_netflix_calc_3(self) :
		i = 1.5
		j = 1.0
		self.assertEqual(1.2650000000000001, netflix_calc(i,j))

	def test_netflix_solve_1(self) :
		r = StringIO("2043:\n1417435\n2312054\n462685\n")
		w = StringIO()
		netflix_solve(r,w)
		self.assertEqual(w.getvalue(), "2043:\n3.9\n3.7\n3.9\nRMSE: 1.66\n")

	def test_netflix_solve_2(self) :
		r = StringIO("2043:\n1417435\n2312054\n462685\n")
		w = StringIO()
		netflix_solve(r,w)
		self.assertEqual(w.getvalue(), "2043:\n3.9\n3.7\n3.9\nRMSE: 1.66\n")

	def test_netflix_solve_3(self) :
		r = StringIO("2043:\n1417435\n2312054\n462685\n")
		w = StringIO()
		netflix_solve(r,w)
		self.assertEqual(w.getvalue(), "2043:\n3.9\n3.7\n3.9\nRMSE: 1.66\n")

# ----
# main
# ----

if __name__ == "__main__" :
    main()