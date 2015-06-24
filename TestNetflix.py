#!/usr/bin/env python3
from io       import StringIO
from unittest import main, TestCase

from Netflix import rep_int_check, netflix_calc, netflix_solve

# -----------
# TestNetflix
# -----------

class TestNetflix (TestCase) :

	def test_netflix_solve(self) :
		r = StringIO("2043:\n1417435\n2312054\n462685\n")
		w = StringIO()
		netflix_solve(r,w)
		self.assertEqual(w.getvalue(), "2043:\n3.5984323624831602\n4.230650186640531\n3.787491657406052\n1.9\n")

# ----
# main
# ----

if __name__ == "__main__" :
    main()