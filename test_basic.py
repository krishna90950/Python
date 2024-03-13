"""
naming convention
1. module/file : test_filename.py or filename_test.py
2. classes : Testclassname
3. functions/methods : test_function()

execution : through terminal
pytest test_filename.py

-v = verbosity : (detailed information about test execution)
-s = scripting (print all the print statements)

to generate the report
pip install pytest-html
pytest test_filename.py -vs --html="reportname.html"
"""

class TestDemo:

    def test_spam(self):
        print("in spam")

    def test_assert(self):
        assert 2 == 3, "2 is not equal to 3"


    def test_greet(self):
        print("hello")

