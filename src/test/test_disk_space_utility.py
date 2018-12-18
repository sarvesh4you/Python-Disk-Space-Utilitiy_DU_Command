'''
Created on 28-Sep-2018

@author: sarveshshrivastava
'''
import os, logging, sys, unittest


sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from main import disk_space_utility
import HTMLTestRunner

reports_path = os.path.join(os.path.dirname(os.path.dirname(os.path.abspath(__file__))), "test_report")
testdata_dir_path = os.path.join(os.path.dirname(os.path.dirname(os.path.abspath(__file__))), "test_data")
cv_and_cover_letter_dir_path = os.path.join(testdata_dir_path, "cv_and_cover_letter")

log = logging.getLogger("LogMessage: ")
test_obj = None

class Test(unittest.TestCase):
        
    def setUp(self):
        global test_obj
        test_obj = disk_space_utility.DiskSpaceUtility()
   
   
###############################################################################################################
#   Test Description : Verify method 'convert_from_bytes_to_readable_unit(self, size_in_bytes)' is            #
#   taking bytes and successfully converting it in human readable format.                                     #
###############################################################################################################  
    def test_01_validate_convert_from_bytes_to_readable_unit(self):
        '''
        Test Description : Verify method 'convert_from_bytes_to_readable_unit(self, size_in_bytes)' is taking bytes and successfully
        converting it in human readable format.
        '''
        self.assertEqual(test_obj.convert_from_bytes_to_readable_unit(1074000000), "1.0 GB", msg="")
        self.assertEqual(test_obj.convert_from_bytes_to_readable_unit(251465), "245.57 KB", msg="")
        log.debug("Test 'validate_convert_from_bytes_to_readable_uni' : Passed")
     
        
###############################################################################################################
#   Test Description : Verify method 'convert_from_bytes_to_readable_unit(self, size_in_bytes)' is            #
#   successfully handling exceptions.                                                                         #
###############################################################################################################  
    def test_02_check_exceptions_in_convert_from_bytes_to_readable_unit(self):
        '''
        Test Description : Verify method 'convert_from_bytes_to_readable_unit(self, size_in_bytes)' is successfully
        handling exceptions.
        '''
        with self.assertRaises(TypeError):
            test_obj.convert_from_bytes_to_readable_unit("string")
        with self.assertRaises(ValueError):
            test_obj.convert_from_bytes_to_readable_unit(-2)
        log.debug("Test 'check_exceptions_in_convert_from_bytes_to_readable_unit' : Passed")
        
        
###################################################################################################################
#   Test Description : Verify method 'get_directory_tree(self, rootdir_path)' is taking directory                 #
#   path and successfully returning all dirs and files inside it. Also verify the count of dirs                   #
#   and files inside it.                                                                                          #
###################################################################################################################      
    def test_03_validate_number_count_of_dir_and_files_in_a_filesystem(self):
        '''
        Test Description : Verify method 'get_directory_tree(self, rootdir_path)' is taking directory path and successfully
        returning all dirs and files inside it. Also verify the count of dirs and files inside it.
        '''
        self.assertEqual(len(test_obj.get_directory_tree(testdata_dir_path)), 38, msg="No. count of dir and files mismatching in filesystem :{} ".format(testdata_dir_path))
        self.assertEqual(len(test_obj.get_directory_tree(cv_and_cover_letter_dir_path)), 2, msg="No. count of dir and files mismatching in filesystem :{}".format(cv_and_cover_letter_dir_path))
        log.debug("Test 'validate_number_count_of_dir_and_files_in_a_filesystem' : Passed")
    
    
###################################################################################################################
#   Test Description : Verify method 'get_directory_tree(self, rootdir_path)' is successfully                     #
#   handling exceptions.                                                                                          #
###################################################################################################################  
    def test_04_check_exceptions_in_number_count_of_dir_and_files_in_a_filesystem(self):
        '''
        Test Description : Verify method 'get_directory_tree(self, rootdir_path)' is successfully
        handling exceptions.
        '''
        with self.assertRaises(FileNotFoundError):
            test_obj.get_directory_tree("/home/desktop/no_file")
        log.debug("Test 'check_exceptions_in_number_count_of_dir_and_files_in_a_filesystem' : Passed")
       
       
###################################################################################################################
#   Test Description : Verify method 'total_disk_space_used(self, du_result)' successfully                        #
#   returning total disk space used by filesystem.                                                                #
###################################################################################################################     
    def test_05_validate_total_size_of_dir_and_files_in_a_filesystem(self):
        '''
        Test Description : Verify method 'total_disk_space_used(self, du_result)' successfully
        returning total disk space used by filesystem.
        '''
        self.assertEqual(test_obj.total_disk_space_used(test_obj.get_directory_tree(testdata_dir_path)), 403464, msg="Total size of dir and files mismatching in filesystem :{} ".format(testdata_dir_path))
        self.assertEqual(test_obj.total_disk_space_used(test_obj.get_directory_tree(cv_and_cover_letter_dir_path)), 251465, msg="Total Size of dir and files mismatching in filesystem :{} ".format(cv_and_cover_letter_dir_path))    
        log.debug("Test 'validate_total_size_of_dir_and_files_in_a_filesystem' : Passed")
    
    
###################################################################################################################
#    Test Description : Verify method 'total_disk_space_used(self, du_result)' is successfully                    #
#    handling exceptions.                                                                                         #
###################################################################################################################  
    def test_06_check_exceptions_in_total_size_of_dir_and_files_in_a_filesystem(self):
        '''
        Test Description : Verify method 'total_disk_space_used(self, du_result)' is successfully
        handling exceptions.
        '''
        with self.assertRaises(FileNotFoundError):
            test_obj.total_disk_space_used(test_obj.get_directory_tree("/home/desktop/no_file"))
        log.debug("Test 'check_exception_in_total_size_of_dir_and_files_in_a_filesystem' : Passed")
        
        
####################################################################################################################
#   Test Description : Verify method 'du_command_output(self, rootdir_path)' is successfully                       #
#   returning true after listing all the dirs and files ina filesystem.                                            #
####################################################################################################################    
    def test_07_validate_du_command_output_in_a_filesystem(self):
        '''
        Test Description : Verify method 'du_command_output(self, rootdir_path)' is successfully
        returning true after listing all the dirs and files ina filesystem.
        '''
        self.assertTrue(test_obj.du_command_output(cv_and_cover_letter_dir_path), msg="Total Size of dir and files mismatching in filesystem :{} ".format(cv_and_cover_letter_dir_path))    
        log.debug("Test 'validate_du_command_output_in_a_filesystem' : Passed")


####################################################################################################################
#   Test Description : Verify method 'du_command_output(self, rootdir_path)' is successfully                       #
#   handling exceptions.                                                                                           #
####################################################################################################################  
    def test_08_check_exceptions_in_du_command_output_in_a_filesystem(self):
        '''
        Test Description : Verify method 'du_command_output(self, rootdir_path)' is successfully
        handling exceptions.
        '''
        with self.assertRaises(FileNotFoundError):
            test_obj.du_command_output("/home/desktop/no_file")
        log.debug("Test 'check_exceptions_in_du_command_output_in_a_filesystem' : Passed") 
        
        
        
    def tearDown(self):
        global test_obj
        del test_obj
        
        
        
if __name__ == "__main__":
    
####################################################################################################################
#            Using 'HTMLTestRunner' module to generate clear detailed HTML reports of unittest                     #
####################################################################################################################     

    logging.basicConfig(stream=sys.stderr)
    logging.getLogger("LogMessage: ").setLevel(logging.DEBUG)
    suite = unittest.TestLoader().loadTestsFromTestCase(Test)
  
    outfile = open(reports_path + "\\TestReport_" + os.path.basename(__file__).split(".")[0] + ".html", "w")
    runner = HTMLTestRunner.HTMLTestRunner(
                stream=outfile,
                title='Test Report : Unittest for ARM Python Disk Utility',
                description='Testing \'disk_space_utility.py\' utility'
                )
  
    runner.run(suite)
    outfile.close()
