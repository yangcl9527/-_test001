import unittest
from test import Test001
import HTMLTestRunner


suite = unittest.TestLoader().loadTestsFromTestCase(Test001)


fp = file("report/my_report.html", "wb")
runner = HTMLTestRunner.HTMLTestRunner(
    stream=fp,
    title="test",
    description="huodongapi"
)


runner.run(suite)