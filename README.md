# ml_scripts
Data preparation scripts for machine learning training

#How to run:
* **Part 1**
 * python part_1.py
 * It will generate a text file that contains a list of available paired file names contained in a number of folders. The csv file is used to do the associations.
 *  If SHOW_FIGURE is set to 1, a figure will display the binary masks.

* **Part 2**
 * python part_2.py
 * It will open the text file generated in part 1, and it will actually load the training data into numpy arrays.
 * It will then extract randomized batches of data for training
 * Set DISPLAY_BATCHES to 1 to display (print) the extracted data batches.

 
