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

	def test_netflix_solve_1(self) :
		r = StringIO("2043:\n1417435\n2312054\n462685\n")
		w = StringIO()
		netflix_solve(r,w)
		self.assertEqual(w.getvalue(), "2043:\n3.6\n4.23\n3.79\nRMSE: 1.9\n")

# ----
# main
# ----

if __name__ == "__main__" :
    main()