'''
Created on 27-Sep-2018

@author: sarveshshrivastava
'''
import sys, os, math
from datetime import  datetime
from functools import lru_cache


class DiskSpaceUtility(object):
    ''' 
    **To run this utility just pass an absolute path of a directory or filesystem through command-line argument 
    or it will take project root directory as an input** i.e. 
    
                    python disk_space_utility.py <absolute_path_to_filesystem>
    
    This utility class contains Python script to display the disk space used by files and directories on 
    a filesystem much like the UNIX utility 'du' does. It would display:

                     *Display the total disk space used by a directory tree within a filesystem;
                     *Display subtotals for each and every file and directory in the directory tree;
                     *Support two output formats when printing the values: normal (the number of bytes, e.g. 992496) and 
                      human readable (e.g., 970M). 
    
                i.e.   Bytes   |Readable Size|   Last Modified   |Absolute Path
                     __________|_____________|___________________|_______________________
                       .....        .....           .....          .....           
                     __________|_____________|___________________|_______________________
                           5434       5.43 KB 2018-08-21 13:44:00 /home/desktop/downloads
                     _________|_____________|___________________|_______________________
                        48322|     47.19 KB|Total disk space used by the directory tree
    
    '''

    du_result_map = {}

    def __init__(self):
        '''
        Default Constructor
        '''
        
        
###############################################################################################################
#    Method Definition : Method takes bytes as an input and returns the size in human readable format.        #
###############################################################################################################      
    def convert_from_bytes_to_readable_unit(self, size_in_bytes):
        '''
        Method Definition : Method takes bytes as an input and returns the size in human readable format.
        '''
        
        if type(size_in_bytes) is str:
            raise TypeError("Argument must be an int or float type.")
        
        elif size_in_bytes<0:
            raise ValueError("Argument must possess a positive value.")
        
        try:
            if size_in_bytes == 0:
                return 0
        
            elif size_in_bytes == 1:
                return "1.0 Byte"
        
            size_unit = ["Bytes", "KB", "MB", "GB", "TB", "PB", "EB", "ZB"]
        
            size_unit_index = int(math.floor(math.log(size_in_bytes, 1024)))
        
            base_value = math.pow(1024, size_unit_index)
        
            redable_value = round(size_in_bytes / base_value, 2)
        
            return "{} {}".format(redable_value, size_unit[size_unit_index])
        
        except Exception as e:
            raise e            
 
 
###############################################################################################################
#    Method Definition : Method takes an absolute path of a directory and add size, last modified date-time   #
#    and absolute path of each and every child file in a cache dictionary.                                    #
###############################################################################################################        
    @lru_cache(maxsize=5000)
    def get_dir_size(self, subdir_path):
        '''
        Method Definition : Method takes an absolute path of a directory and add size, last modified date-time
        and absolute path of each and every child file in a cache dictionary.
        '''
        total_size = 0
        
        if not os.path.exists(subdir_path):
            raise FileNotFoundError("The system cannot find the path specified: {}".format(subdir_path))
        
        try:
            for item in os.listdir(subdir_path):
                itempath = os.path.join(subdir_path, item)
                if os.path.isfile(itempath):
                    f_size = os.stat(itempath).st_size
                    l_mod = datetime.fromtimestamp(round(os.stat(itempath).st_mtime))
                    self.du_result_map[itempath] = (f_size, self.convert_from_bytes_to_readable_unit(f_size), str(l_mod))
              
                    total_size += f_size
                
                elif itempath in self.du_result_map:
                    total_size += self.du_result_map[itempath][0] 
                elif os.path.isdir(itempath):
                    total_size += self.get_dir_size(itempath)
          
            return total_size
   
        except Exception as e:
            raise e
   
   
   
###############################################################################################################
#    Method Definition : Method takes an absolute path of a directory and add size, last modified date-time   #
#    and absolute path of each and every child directory and first-child files in a cache dictionary.          #
###############################################################################################################              
    def get_directory_tree(self, rootdir_path): 
        '''
        Method Definition : Method takes an absolute path of a directory and add size, last modified date-time
        and absolute path of each and every child directory and first-child files in a cache dictionary.
        '''
        
        self.du_result_map.clear()
        
        if not os.path.exists(rootdir_path):
            raise FileNotFoundError("The system cannot find the path specified: {}".format(rootdir_path))
        
        try:
            for file in os.listdir(rootdir_path):
                itempath = os.path.join(rootdir_path, file)
                if os.path.isfile(itempath):
                    f_size = os.stat(itempath).st_size
                
                    l_mod = datetime.fromtimestamp(round(os.stat(itempath).st_mtime))
                    self.du_result_map[itempath] = (f_size, self.convert_from_bytes_to_readable_unit(f_size), str(l_mod))
   
            for root, dirs, files in os.walk(rootdir_path, topdown=False):

                for dir_name in dirs:
                    itempath = os.path.join(root, dir_name)
                    if not itempath in self.du_result_map:
                        byte_size = self.get_dir_size(os.path.join(root, dir_name))
                  
                        self.du_result_map[itempath] = (byte_size, self.convert_from_bytes_to_readable_unit(byte_size), 'directory')
            
            return self.du_result_map

        except Exception as e:
            raise e


###############################################################################################################
#     Method Definition : Method takes a du_result dictionary as an input and returns total disk              #
#     space used by the directory tree.                                                                       #
###############################################################################################################      
    def total_disk_space_used(self, du_result):
        '''
        Method Definition : Method takes a du_result dictionary as an input and returns total disk space used by the directory tree.
        '''
        if not type(du_result) is dict:
            raise TypeError("'du_result' type must be a dict only, found: {}".format(type(du_result)))
        
        return sum((lambda result:[result[key][0] for key in result if result[key][2] != 'directory' ])(du_result))



###############################################################################################################
#  Method Definition : This method is core method to be called. Method takes absolute path of a directory and #
#  display the disk space used by files and directories on a file-system much like the UNIX utility 'du' does #
###############################################################################################################     
    def du_command_output(self, rootdir_path):
        '''
        Method Definition : This method is core method to be called. Method takes absolute path of a directory and 
        display the disk space used by files and directories on a file-system much like the UNIX utility 'du' does.
        '''
        if not os.path.exists(rootdir_path):
            raise FileNotFoundError("The system cannot find the path specified: {}".format(rootdir_path))
        
        result_tree = self.get_directory_tree(rootdir_path)
        disk_space = self.total_disk_space_used(result_tree)
        
        print("{:^10}|{:^13}|{:^19}|{}".format("Bytes", "Readable Size", "Last Modified", "Absolute Path"))
        print("{:_<10}|{:_<13}|{:_<19}|{:_<100}".format("_", "_", "_", "_"))
        for key, val in result_tree.items():
             
            print("{:>10}|{:>13}|{:>19}|{}".format(val[0], val[1], val[2], key))
     
        print("{:_<10}|{:_<13}|{:_<19}|{:_<100}".format("_", "_", "_", "_"))
        print("{:>10}|{:>13}|{:>19}".format(disk_space, self.convert_from_bytes_to_readable_unit(disk_space), "Total disk space used by the directory tree"))
        
        return True
   
   
    
if __name__ == "__main__":
    
###############################################################################################################
#     Checking if sys.argv has been passed through the command-line argument or not, otherwise assigning      #
#     test_data dir path inside project directory to the 'rootdir_path' variable.                             #
###############################################################################################################     
      
    if len(sys.argv) > 1:
        dir_path = sys.argv[1]
    else:
        dir_path = os.path.join(os.path.dirname(os.path.dirname(os.path.abspath(__file__))),"test_data")
       
    DiskSpaceUtility().du_command_output(dir_path)