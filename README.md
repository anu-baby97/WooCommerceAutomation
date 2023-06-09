# WooCommerceAutomation
To automate Woo Commerce Application follow the below steps:
1. Install Python (3.10.1) 
2. Setting path for python in environment variables:            
    i)  Open _Environment Variable_ window from Control Panel.     
    ii) Under _System variables_ select _Path_.         
    iii) Click on _Edit_. Then click _New_.         
    iv) Enter the path of Python install directory.         
    v) Click on OK buttons. The path for python is set.         
3. Install selenium libraries using command **Python -m pip install -U Selenium**
4. Install Pycharm IDE and install following python packages:           
    i)   _pytest_ package               
    ii)  _selenium_ package             
    iii) _pytest-html_ for generating reports           
    iv) _pytest-xdist_ for parallel test execution               
    v)  _pytest-order_ for ordering the test cases                          
    The automation script is written in POM model (_Pages, TestCases, Config files_ and _conftest.py_ file)
5. To run the script,                           
   i) Clone the project from git                
   ii) Open the terminal in current project and run the command: -> **pytest Tests**                                       
      a) To make output more verbose -> **pytest Tests -v**                     
      b) To run test cases in parallel (mention number of threads to run) -> **pytest Tests -n 6**                      
      c) To generate html report -> **pytest Tests --html=./wooCommerceReport.html**                          
     
     
     **Generated Report**:
     
     <img width="941" alt="image" src="https://github.com/anu-baby97/WooCommerceAutomation/assets/69788070/7c51a556-5a82-4f69-a238-f362732f9f37">
