'''
Test command line file
'''

import unittest
from io import StringIO

from command_line import * #note, specify this late
#Running the line above is giving me an error.

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
        self.assertEqual(printed_out,"Water usage in United States of America \n\n2001: 1829x10^9 cubic meters/year\n2003: 1829x10^9 cubic meters/year\nDifference:\n0x10^9 cubic meters/year")

    def test_run_waterUseTimeCompare_fail(self):
        sys.argv = ['command_line.py','-usageovertime', 'USA', '2001']
        printed_out = self._run_and_return_output()
        self.assertEqual(printed_out,"Invalid arguments.")

    def test_run_waterUseTimeCompare_invalid_year(self):
        sys.argv = ['command_line.py','-usageovertime', 'USA', '2001','243243125245324']
        self.assertRaises(KeyError,self._run_and_return_output)

class perCapitaWaterUseTest(unittest.TestCase):
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

class usagePercentageTest(unittest.TestCase):
    def test_percentage_valid(self):
        '''Test valid country/year/type input'''
        result = get_usage_percentage("Argentina", "2023", "Agricultural")
        self.assertAlmostEqual(result, 40.842, places=2)

    def test_percentage_invalid_country(self):
        '''Test invalid country input'''
        with self.assertRaises(ValueError):
            get_usage_percentage("Wakanda", "2023", "Agricultural")

    def test_percentage_invalid_year(self):
        '''Test invalid year input'''
        with self.assertRaises(ValueError):
            get_usage_percentage("Argentina", "3023", "Agricultural")

    def test_percentage_invalid_usage_type(self):
        '''Test invalid usage type input'''
        with self.assertRaises(ValueError):
            get_usage_percentage("Argentina", "2023", "Extrajudicial")

class usageProportionTest(unittest.TestCase):
    def _run_and_return_output(self) -> str:
        """Helper function thar runs the command line app and returns the output."""
        sys.stdout = StringIO()
        main()
        return sys.stdout.getvalue().strip()
    
    def test_proportion_valid(self):
        '''Test valid country/year/type input'''
        sys.argv = ['command_line.py','-usageproportion', 'Argentina', '2024']
        printed_out = self._run_and_return_output()
        self.assertEqual(printed_out,"Water usage in Argentina in 2024\n\nAgricultural:  51.20142857\nIndsutrial:  34.14285714\nHousehold:  23.52285714\nNone")
    
    def test_proportion_invalid_country(self):
        with self.assertRaises(ValueError):
            usageProportion("Wakanda", "2023")

    def test_proportion_invalid_year(self):
        with self.assertRaises(ValueError):
            usageProportion("Argentina", "3023")
    
    def test_proportion_no_year(self):
        sys.argv = ['command_line.py','-usageproportion', 'Argentina']
        with self.assertRaises(ValueError):
            usageProportion("Argentina", "")



if __name__=="__main__":
    main()