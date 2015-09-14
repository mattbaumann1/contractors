#!/usr/bin/python3
# test_main.py authored by Matt Baumann for COMP 412 Loyola University

import main
import unittest
import os

class MainTests(unittest.TestCase):
    
    ##http://stackoverflow.com/questions/82831/check-whether-a-file-exists-using-python
    def testContractorsIsFile(self):
        assert os.path.isfile('./contractors.csv') and os.access('./contractors.csv', os.R_OK)
    def testLobbyistsIsFile(self):
        assert os.path.isfile('./lobbyist.csv') and os.access('./lobbyist.csv', os.R_OK)
    
if __name__ == "__main__": unittest.main()
