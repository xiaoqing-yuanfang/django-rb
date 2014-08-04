"""
This file demonstrates writing tests using the unittest module. These will pass
when you run "manage.py test".

Replace this with more appropriate tests for your application.
"""

#from django.test import TestCase
#
#
#class SimpleTest(TestCase):
#    def test_basic_addition(self):
#        """
#        Tests that 1 + 1 always equals 2.
#        """
#        self.assertEqual(1 + 1, 2)
if(__name__ == "__main__"):
    import os
    import shutil
    import time
    import filecmp
    while(True):
        file1 = "rb.sqlite3"
        file2 = "rb.sqlite3.backup"
        size1 = os.path.getsize(file1)
        size2 = os.path.getsize(file2)
        flag = filecmp.cmp(file1,file2,shallow=False)
        print(size1,size2,flag)
        time.sleep(3)
        if(flag == True):
            break
    shutil.copy(file1,"/tmp/")
    #shutil.copy(src="rb.sqlite3",dst="/tmp/")
