#!/usr/bin/env python3
from io       import StringIO
from unittest import main, TestCase
import os
import requests
from Netflix import netflix_solve

# -----------
# TestNetflix
# -----------

class TestNetflix (TestCase) :
	def test_netflix_solve(self) :
		x = 1
		y = 1
		z = netflix_solve(x,y)
		self.assertEqual(1,z)

# ----
# main
# ----

if __name__ == "__main__" :
    main()