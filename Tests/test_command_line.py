'''
Test command line file
'''

import unittest
from io import StringIO

from command_line import * #note, specify this late


    def test_per_capita_valid(self):
        '''Test valid country and year inputs'''
        result = get_per_capita_water_use("Japan", "2018")
        self.assertAlmostEqual(result, 290.58, places=2)

    def test_per_capita_invalid_country(self):
        '''Test invalid country input'''
        with self.assertRaises(ValueError):
            get_per_capita_water_use("Wakanda", "2018")

    def test_per_capita_invalid_year(self):
        with self.assertRaises(ValueError):
            get_per_capita_water_use("Japan", "1000")
    
    
    

class openDBTest(unittest.TestCase):
    def test_odb(self):
        arr = openDB(DB.CLEANED_GWC)
        self.assertEqual(arr[0][0],"Country")
    def test_invalid_db(self):
        self.assertRaises(KeyError,openDB,"AAAAAA")

class filterTagsDBTest(unittest.TestCase):
    def test_base(self):
        arr = filterTagsDB(DB.AQS_DS3,["United States of America"])
        self.assertTrue(len(arr) > 0)

    def test_invalid_tag(self):
        arr = filterTagsDB(DB.AQS_DS3,["THIS COUNTRY DOES NOT EXIST LOLOLOLOL"])
        self.assertTrue(len(arr) == 0)

class commandLineTest(unittest.TestCase):
    def _run_and_return_output(self) -> str:
        """Helper function thar runs the command line app and returns the output."""
        sys.stdout = StringIO()
        main()
        return sys.stdout.getvalue().strip()
    def test_run(self):
        sys.argv = []
        printed_out = self._run_and_return_output()
        self.assertEqual(printed_out, "USAGE STATEMENT GOES HERE")

    def test_run_waterUseTimeCompare(self):
        sys.argv = ['command_line.py','-usageovertime', 'USA', '2001', '2003']
        printed_out = self._run_and_return_output()
        self.assertEqual(printed_out,"Water usage in United States of America\n\n2001: 1829x10^9 cubic meters/year\n2003: 1829x10^9 cubic meters/year")

    def test_run_waterUseTimeCompare_fail(self):
        sys.argv = ['command_line.py','-usageovertime', 'USA', '2001']
        printed_out = self._run_and_return_output()
        self.assertEqual(printed_out,"Invalid arguments.")

    def test_run_waterUseTimeCompare_invalid_year(self):
        sys.argv = ['command_line.py','-usageovertime', 'USA', '2001','243243125245324']
        self.assertRaises(KeyError,self._run_and_return_output)


if __name__=="__main__":
    main()