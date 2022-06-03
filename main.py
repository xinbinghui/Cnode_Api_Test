import pytest
import time
import os
from common.Logs import Log
# from common.Shell import Shell
import sys
from common.Emails import mail

if __name__ == '__main__':
    file_name = os.path.basename(sys.argv[0])
    log = Log(file_name)
    logger = log.Logger
    try:
        logger.info("开始执行脚本")
        logger.info("==========" + time.strftime('%Y-%m-%d %H:%M:%S', time.localtime()) + "==========")
        # pytest.main(['-vs','--alluredir','./report/reportallure/'])
        pytest.main()
        logger.info("脚本执行完成")
    except Exception as e:
        logger.error("脚本批量执行失败", e)
        print("脚本批量执行失败", e)
    try:
        # shell = Shell
        cmd = 'allure generate %s -o %s --clean' % ('./report/reportallure/','./report/reporthtml/')
        logger.info("开始执行报告生成")
        # shell.invoke(cmd)
        os.system(cmd)
        logger.info("报告生成完毕")
    except Exception as e:
        logger.error("报告生成失败，请重新执行", e)
        print("报告生成失败，请重新执行", e)
        raise

    # time.sleep(2)
    # mail()

# allure 报告终端打开方式
# allure open F:\Python\api_rili\report\reporthtml