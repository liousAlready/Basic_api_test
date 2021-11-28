import unittest
import HTMLTestReportCN
from common.localconfig_utlis import local_config


def get_all_cases_suite():
    discover = unittest.defaultTestLoader.discover(
        start_dir="./testcases",
        pattern="*_cases.py",
        top_level_dir="./testcases"
    )
    all_suite = unittest.TestSuite()
    all_suite.addTest(discover)
    return all_suite


report_dir = HTMLTestReportCN.ReportDirectory(local_config.REPORT_PATH + "/")
report_dir.create_dir("API_TEST")
# dir_path = HTMLTestReportCN.GlobalMsg.get_value("dir_path")
report_path = HTMLTestReportCN.GlobalMsg.get_value("report_path")
fp = open(report_path, "wb")
runner = HTMLTestReportCN.HTMLTestRunner(stream=fp,
                                         tester="new",
                                         title="api_tests",
                                         description="学习")
runner.run(get_all_cases_suite())
fp.close()