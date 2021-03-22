import unittest
from csvReader import CsvReader, ClassFactory
from pprint import pprint

class MyTestCase(unittest.TestCase):
    def setUp(self) -> None:
        self.csv_reader = CsvReader('Tests/Data/testJobs.csv')

    def test_return_as_objects(self):
        staff = self.csv_reader.return_data_as_class('job')
        self.assertIsInstance(staff, list)
        test_class = ClassFactory('job', self.csv_reader.data[0])

        for job in staff:
            self.assertEqual(job.__name__, test_class.__name__)
            # pprint(vars(staff))

if __name__ == '__main__':
    unittest.main()