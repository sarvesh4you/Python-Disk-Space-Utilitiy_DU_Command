# Python_disk_space_utility

#### System Requirement:

* Python 3.4
* Any IDE i.e. PyDev, PyCharm (optional).

#### Framework and Package Structure:
  -Unittest Based Framework
  
  ***It comprises two main folders:-***
  1) main
  2) test
  3) test_data
  4) test_reports
  5) help_snapshots
  
  
1)***Python-Disk-Space-Utilitiy\src\main*** contains 1 module.

  ``` disk_space_utility.py ``` 
  ***This module contains the Python script to display the disk space used by files and directories on a file-system much like the UNIX utility 'du' does.***  
 
 
2)***Python-Disk-Space-Utilitiy\src\test*** contains 2 modules.

  ``` test_disk_space_utility.py ``` 
  ***Contains unit tests for 'disk_space_utility.py'.*** 
  
  ``` HTMLTestRunner.py ```
  ***Contains code for generating clear HTML reports after executing unit tests.***
  
 
3)***Python-Disk-Space-Utilitiy\src\test_data*** contains test dirs and files. 
     ``` test_data ``` 
  ***Contains test data (dirs and files) which are being used in unittest.***  
  
  
4)***Python-Disk-Space-Utilitiy\src\test_report*** contains html test reports. 
     ``` Sample_fail_TestReport.html ``` 
	 ``` Sample_pass_TestReport.html ``` 
	 ***Contains HTML test reports generated through HTMLTestRunner.py.***    
	 
5)***Python-Disk-Space-Utilitiy\src\help_snapshots*** contains html test reports. 
     ``` output_1.JPG ``` 
	 ``` output_2.JPG ``` 
	 ``` report_1.JPG ``` 
	 ``` report_2.JPG ``` 
	 ``` report_3.JPG ``` 
	 ``` utility_class.JPG ``` 
	 ``` unittest_for_utility_class.JPG ``` 
	 ``` project_directory_structure.JPG ``` 
	 
	 ***Contains JPG help snapshots that will help to explore and understand the utility.***  	 

	 
#### Execution Steps:
***Please follow the instructions to execute the tests on local:***


#### To Run 'disk_space_utility.py' Utility:

1. By Using cmd/terminal:

   - To Execute use command: 
        python disk_space_utility.py <absolute_path_to_filesystem>
		
	```(after navigating to the main module)```
    ``` if you don't give any system argument for dir path, it will use project root path by default``` 

	
2. By Using IDE i.e. PyDev:
   
   - To Execute follow steps:
   
     ```Set dir path in command-line argument ```
     ```Right click on disk_space_utility.py```
     ``` Run As Python Run``` 
     ``` if you don't set any system argument for dir path, it will use project root path by default``` 
	 
	 
#### To Run Unittest for 'disk_space_utility.py':

1. By Using cmd/terminal:
   - To Execute through unittest (It will not generator the html test reports under 'test_report' folder)
	```(after navigating to the test module) python -m unittest test_disk_space_utility.py```
	
   - To Execute through HTMLTestRunner (It will generator the html test reports under 'test_report' folder)
    ``` (after navigating to the test module) python test_disk_space_utility.py``` 

	
2. By Using IDE i.e. PyDev:
   - To Execute through unittest (It will not generator the html test reports under 'test_report' folder)
	``` Run As Python unit-test```
	
   - To Execute through HTMLTestRunner (It will generator the html test reports under 'test_report' folder)
    ``` Run As Python Run``` 


#### Functionality Of Utility:	

***disk_space_utility.py*** 

```
The utility we would like you to create is a Python script to display the disk space used by files and directories on a filesystem much like the UNIX utility 'du' does. It would need to:

    display the total disk space used by a directory tree within a filesystem;
    display subtotals for each and every file and directory in the directory tree;
    support two output formats when printing the values: normal (the number of bytes, e.g. 992496) and human readable (e.g., 970M). 
```


#### Let me know if you have any questions/suggestions/issues related to this utility:
``` sarvesh4you@gmail.com```
``` +91-8800672630```
