import unittest
import US47


class MyTestCase(unittest.TestCase):
    global INDI

    INDI = {
        '@I1@': ['Javier /Diaz/', 'M', '27 AUG 2000', 20, True, 'N/A', ['@F1@', 'N/A']],
        '@I2@': ['Miguel /Diaz/', 'M', '9 SEP 1967', 53, True, 'N/A', ['N/A', '@F1@'], ['N/A', '@F2@'],
                 ['@F3@', 'N/A']],
        '@I3@': ['Deysi /Geronimo/', 'F', '3 JAN 1979', 41, True, 'N/A', ['N/A', '@F1@'], ['@F4@', 'N/A']],
        '@I4@': ['Xavier /Diaz/', 'M', '27 AUG 2000', 20, True, 'N/A', ['@F1@', 'N/A']],
        '@I5@': ['Cesar /Geronimo/', 'M', '23 MAY 1944', 76, True, 'N/A', ['N/A', '@F4@']],
        '@I6@': ['Daisy /Guerrero/', 'F', '25 APR 1953', 67, True, 'N/A', ['N/A', '@F4@']],
        '@I7@': ['Cesar Jr /Geronimo/', 'M', '9 SEP 1977', 43, True, 'N/A', ['@F4@', 'N/A'], ['N/A', '@F5@'],
                 ['N/A', '@F6@']],
        '@I8@': ['Cecilia /Geronimo/', 'F', '4 DEC 1982', 38, True, 'N/A', ['@F4@', 'N/A'], ['N/A', '@F7@']],
        '@I9@': ['Federico /Diaz/', 'M', '9 DEC 1936', 84, False, '11 MAR 1985', ['N/A', '@F3@']],
        '@I10@': ['Elena /Cruz/', 'F', '14 JUL 1940', 80, True, 'N/A', ['N/A', '@F3@']],
        '@I11@': ['Donny /Pena/', 'M', '20 FEB 1978', 42, True, 'N/A', ['N/A', '@F7@']],
        '@I12@': ['Daileen /Pena/', 'F', '18 JUN 2002', 18, True, 'N/A', ['@F7@', 'N/A']],
        '@I13@': ['Derek /Pena/', 'M', '4 OCT 2004', 16, True, 'N/A', ['@F7@', 'N/A']],
        '@I14@': ['Dariel /Pena/', 'M', '17 JUN 2009', 11, True, 'N/A', ['@F7@', 'N/A']],
        '@I15@': ['Miguel Adonis /Diaz/', 'M', '20 MAR 1997', 23, True, 'N/A', ['@F2@', 'N/A']],
        '@I16@': ['Stephanie /Gonzalez/', 'F', '13 JUN 1980', 40, True, 'N/A', ['N/A', '@F5@']],
        '@I17@': ['Maria /Santos/', 'F', '12 OCT 1969', 51, False, '18 OCT 1998', ['N/A', '@F2@']],
        '@I18@': ['Gabriela /Geronimo/', 'F', '12 AUG 2007', 13, False, '3 DEC 2014', ['@F5@', 'N/A']],
        '@I19@': ['Ana /Castro/', 'F', '9 OCT 1979', 41, True, 'N/A', ['N/A', '@F6@']],
        '@I20@': ['Ginelly /Geronimo/', 'F', '3 JUN 2018', 2, True, 'N/A', ['@F6@', 'N/A']],
        '@I21@': ['Iris /Diaz/', 'F', '16 SEP 1976', 44, True, 'N/A', ['@F3@', 'N/A'], ['N/A', '@F8@']],
        '@I22@': ['Luis /Severino/', 'M', '30 JUN 1970', 50, True, 'N/A', ['N/A', '@F8@']],
        '@I23@': ['Karen /Severino/', 'F', '13 JUL 2002', 18, True, 'N/A', ['@F8@', 'N/A']],
        '@I24@': ['Karol /Severino/', 'F', '10 NOV 2004', 16, True, 'N/A', ['@F8@', 'N/A']],
        '@I25@': ['Katy /Severino/', 'F', '24 JAN 2008', 12, True, 'N/A', ['@F8@', 'N/A']],
        '@I26@': ['Mercedes /Diaz/', 'F', '30 SEP 1970', 50, True, 'N/A', ['@F3@', 'N/A'], ['N/A', '@F9@']],
        '@I27@': ['Carlos /Alayon/', 'M', '13 OCT 1965', 55, True, 'N/A', ['N/A', '@F9@']],
        '@I28@': ['Emilkar /Alayon/', 'M', '30 SEP 1985', 35, True, 'N/A', ['@F9@', 'N/A']],
        '@I29@': ['Fredrick /Alayon/', 'M', '21 DEC 1990', 30, True, 'N/A', ['@F9@', 'N/A']],
        '@I30@': ['Emil /Alayon/', 'M', '23 JAN 2001', 19, True, 'N/A', ['@F9@', 'N/A']]
    }

    def test_correct_print(self):
        self.assertTrue(US47.print_under_6(INDI))


if __name__ == '__main__':
    unittest.main()
