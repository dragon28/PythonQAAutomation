import subprocess
import datetime
import shutil

if __name__ == '__main__':
    
    date_time = datetime.datetime.now().strftime("%Y_%m_%d_%H_%M_%S")
    
    output_log_file = "logs/output_log_" + date_time +".log"
    error_log_file = "logs/error_log_" + date_time +".log"
    
    single_html_report = "reports/report.html"
    allure_single_html_report  = "allure-report/index.html"
    
    # pytest_result = subprocess.run(['python', '-m', 'pytest', '--driver', 'Chrome','tests/pytest-selenium/test_otp_page.py'], capture_output=True, text=True)
    pytest_result = subprocess.run(['python', '-m', 'pytest', '--driver', 'Chrome'], capture_output=True, text=True)
    
    if pytest_result.stdout:
        
        print(pytest_result.stdout)
        
        pytest_output_log = open(output_log_file, 'w')
        pytest_output_log.write(pytest_result.stdout)
        pytest_output_log.close()
        shutil.copyfile(single_html_report, "reports/report_" + date_time + ".html")
    
    
    if pytest_result.stderr:
        
        print(pytest_result.stderr)
        
        pytest_result_log = open(error_log_file, 'w')
        pytest_result_log.write(pytest_result.stderr)
        pytest_result_log.close()


    allure_result = subprocess.run(['allure', 'generate', '--single-file', 'allure-results', '--clean'], capture_output=True, text=True)
    
    
    if allure_result.stdout:
        
        print(allure_result.stdout)
        
        allure_output_log = open(output_log_file, 'a')
        allure_output_log.write(allure_result.stdout)
        allure_output_log.close()
        shutil.copyfile(allure_single_html_report, "reports/allure_report_" + date_time + ".html")
    
    
    if allure_result.stderr:
        
        print(allure_result.stderr)
        
        allure_result_log = open(error_log_file, 'a')
        allure_result_log.write(allure_result.stderr)
        allure_result_log.close()