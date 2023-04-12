To run the test case, you will need to install several dependencies including 
Python
Pycharm 
Selenium 
Requests 
Pillow
ImageHash

After installation, you will need to navigate to the

 board_support_items.py file in the features/support directory and change the folder location to your local hard drive against testdata

Then, you can navigate to board_ui.py in the features directory and run the test by right-clicking selecting 'run' or by clicking the run button.

In addition, there are several configurations files located in the 

features/configurations directory, including board_creation_conf.py which contains the API for creating a board and board_share_conf.py which contains the API for sharing a board. 

The board_support_items.py file located in the features/support directory contains support configurations while the locators.py file has all the locators. 

The board_ui.py file located in the features/forms directory contains the end-to-end test, and the features/testdate directory is where the code will create screenshots of images.

Finally, the features/tests directory contains the BDD file.

