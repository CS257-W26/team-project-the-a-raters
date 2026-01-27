"""
Test command line file
"""

import unittest
import sys
from io import StringIO

from command_line import open_database  # note, specify this late
from command_line import DB
from command_line import filter_tags_database
from command_line import get_per_capita_water_use
from command_line import main
from command_line import get_usage_percentage
from command_line import usage_proportion


# Running the line above is giving me an error.


class OpenDataBaseTest(unittest.TestCase):
    """Tests open_database func"""
    def test_odb(self):
        """Tests the basic OpenDatabase function"""
        arr = open_database(DB.CLEANED_GWC)
        self.assertEqual(arr[0][0], "Country")

    def test_invalid_db(self):
        """Tests ODB with invalid DB"""
        self.assertRaises(KeyError, open_database, "AAAAAA")


class FilterTagsDataBaseTest(unittest.TestCase):
    """Tests filter_tags_database"""
    def test_base(self):
        """Tests filter DB"""
        arr = filter_tags_database(DB.AQS_DS3, ["United States of America"])
        self.assertTrue(len(arr) > 0)

    def test_invalid_tag(self):
        """Tests filter DB with invalid args"""
        arr = filter_tags_database(DB.AQS_DS3, ["THIS COUNTRY DOES NOT EXIST LOLOLOLOL"])
        self.assertTrue(len(arr) == 0)


class CommandLineTest(unittest.TestCase):
    """Tests command line running"""
    def _run_and_return_output(self) -> str:
        """Helper function thar runs the command line app and returns the output."""
        sys.stdout = StringIO()
        main()
        return sys.stdout.getvalue().strip()

    def test_run(self):
        """Basic test run"""
        sys.argv = []
        printed_out = self._run_and_return_output()
        self.assertEqual(printed_out, "Usage: python3 command_line.py -usageproportion --country --year")

    def test_run_water_use_time_compare(self): #THIS IS AN ACCEPTANCE TEST FOR #3
        """Tests water use compare"""
        sys.argv = ["command_line.py", "-usageovertime", "USA", "2001", "2003"]
        printed_out = self._run_and_return_output()
        self.assertEqual(
            printed_out,
            "Water usage in United States of America \n\n2001: 1829x10^9 cubic meters/year\n2003: 1829x10^9 cubic meters/year\nDifference:\n0x10^9 cubic meters/year",
        )

    def test_run_water_use_time_compare_fail(self):
        """Tests invalid water use compare"""
        sys.argv = ["command_line.py", "-usageovertime", "USA", "2001"]
        printed_out = self._run_and_return_output()
        self.assertEqual(printed_out, "Invalid arguments.")

    def test_run_water_use_time_compare_invalid_year(self):
        """Tests invalid water use compare with bad year"""
        sys.argv = [
            "command_line.py",
            "-usageovertime",
            "USA",
            "2001",
            "243243125245324",
        ]
        self.assertRaises(KeyError, self._run_and_return_output)
    def test_per_capita_command(self): #THIS IS AN ACCEPTANCE TEST FOR #1
        """Test percapita command"""
        sys.argv = ["command_line.py", "-percapita", "Argentina", "2024"]
        printed_out = self._run_and_return_output()
        self.assertEqual(
            printed_out,
            "Argentina's Water Usage per Capita:                     364.38 Liters per day",
        )


class PerCapitaWaterUseTest(unittest.TestCase):

    """Tests percapita water use"""
    def test_per_capita_valid(self): #THIS IS AN ACCEPTANCE TEST FOR #2
        """Test valid country and year inputs"""
        result = get_per_capita_water_use("Japan", "2018")
        self.assertAlmostEqual(result, 290.58, places=2)

    def test_per_capita_invalid_country(self):
        """Test invalid country input"""
        with self.assertRaises(ValueError):
            get_per_capita_water_use("Wakanda", "2018")

    def test_per_capita_invalid_year(self):
        """Test invalid year input"""
        with self.assertRaises(ValueError):
            get_per_capita_water_use("uk", "1000")



class UsagePercentageTest(unittest.TestCase):
    """Tests usage percentage"""
    def test_percentage_valid(self):
        """Test valid country/year/type input"""
        result = get_usage_percentage("Argentina", "2023", "Agricultural")
        self.assertAlmostEqual(result, 40.842, places=2)

    def test_percentage_invalid_country(self):
        """Test invalid country input"""
        with self.assertRaises(ValueError):
            get_usage_percentage("Wakanda", "2023", "Agricultural")

    def test_percentage_invalid_year(self):
        """Test invalid year input"""
        with self.assertRaises(ValueError):
            get_usage_percentage("Argentina", "3023", "Agricultural")

    def test_percentage_invalid_usage_type(self):
        """Test invalid usage type input"""
        with self.assertRaises(ValueError):
            get_usage_percentage("Argentina", "2023", "Extrajudicial")


class UsageProportionTest(unittest.TestCase):
    """Tests usage proportions"""
    def _run_and_return_output(self) -> str:
        """Helper function thar runs the command line app and returns the output."""
        sys.stdout = StringIO()
        main()
        return sys.stdout.getvalue().strip()

    def test_proportion_valid(self): #THIS IS AN ACCEPTANCE TEST FOR #1
        """Test valid country/year/type input"""
        sys.argv = ["command_line.py", "-usageproportion", "Argentina", "2024"]
        printed_out = self._run_and_return_output()
        self.assertEqual(
            printed_out,
            "Water usage in Argentina in 2024\n\nAgricultural: 51.2 %\nIndustrial: 34.14 %\nHousehold: 23.52 %\nNone",
        )

    def test_proportion_invalid_country(self):
        """Test invalid country input"""
        with self.assertRaises(ValueError):
            usage_proportion("Wakanda", "2023")

    def test_proportion_invalid_year(self):
        """Test invalid year input"""
        with self.assertRaises(ValueError):
            usage_proportion("Argentina", "3023")

    def test_proportion_no_year(self):
        """Test missing year input"""
        sys.argv = ["command_line.py", "-usageproportion", "Argentina"]
        printed_out = self._run_and_return_output()
        self.assertEqual(printed_out,"Usage: python3 command_line.py -usageproportion --country --year")



if __name__ == "__main__":
    main()
