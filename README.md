# WooCommerceAutomation
To automate Woo Commerce Application follow the below steps:
1. Install Python (3.10.1)
2. Install selenium libraries using command Python **-m pip install -U Selenium**  
3. Install pycharm and after opening it, install selenium package. Also pycharm-html for generating reports and pycharm-xdist for parallel test execution
    The automation script is written in POM model (Pages, TestCases, Config files and conftest.py file)
5. To run the script, open the terminal in current project and run the command:
  -> **pytest Tests**
  To make output more verbose -> **pytest Tests -v**
  To run test cases in parallel (mention number od threads to run) -> **pytest Tests -n 6**
  To generate html report -> **pytest Tests --html=./wooCommerce.html**
  <img width="941" alt="image" src="https://github.com/anu-baby97/WooCommerceAutomation/assets/69788070/7c51a556-5a82-4f69-a238-f362732f9f37">
