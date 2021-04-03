# Lazor-Project

## This is a project used to generate solutions to various levels of the popular iOS and Android App, Lazors. Stuck on a difficult level? Looking to beat the App? You’ve come to the right place.
#### Authors: Keynon Bell, Lidya Gebremeskel, Linda Procell
### This code will read in a *.bff file to obtain information such as the original board configuration, lazer paths, target point positions, and movable blocks. 

## INSTALLATION
### Download the defeatLazorBoard.py file

## OPERATING INSTRUCTIONS
### 
In order to run the code successfully, save a *.bff file alongside the defeatLazorBoard.py code in this repository. Enter the command defeatLazorBoard(‘filename’) where filename is the name of the board in quest, such as ‘mad_1.bff’. This will interpret and solve the board for you.
When complete, the code will save a *.png file with the name ‘filename_solution.png’, showing the winning block configuration. To see an example of the file format, please refer to the example files included in this repository. file ‘mad_1.bff’ has a complete explanation of the *.bff file design. For smaller boards, this process should not last more than 20-30 seconds. For larger and more complex boards, please expect a slight delay in solution retrieval. 
The *.png output file can be read using the following key: Reflective blocks are white, Opaque blocks are grey, Refract blocks are light yellow, and other unmovable blocks are brown. The lazor paths are red and target points are blue. While rudimentary, this image output shows you where to place your blocks so you can get through even the hardest levels with minimal effort. 
Good Luck! 
###

## FILE MANIFEST 
###  Python Code:
* defeatLazorBoard.py
### Levels:
* mad_1.bff
* mad_4.bff
* mad_7.bff
* numbered_6.bff
* tiny_5.bff
* yarn_5.bff
* dark_1.bff
### Prompt/handout 
* Lazor_Project_Handout_Spring_2021.pdf
### Example solutions:
* dark_1_completed.png
* mad_1_completed.png
* mad_4_completed.png
* mad_7_completed.png
* numbered_6_completed.png
* tiny_5_completed.png
* yarn_5_completed.png


## TROUBLESHOOTING
### 
This code is designed to read in *.bff files ONLY. if you enter some other filetype, the code will throw an error. Make sure the filename you enter corresponds to an actual *.bff board.
Another potential pitfall is an unsolvable board. Unsolvable boards will also throw an error, so if you are designing your own testing board, please follow the input format shown in the files ‘mad_1.bff’ or ‘mad_7.bff’ in this repository.
###
