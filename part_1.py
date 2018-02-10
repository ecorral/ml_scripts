# Copyright 2018 Eduardo R. Corral-Soto. All Rights Reserved.
#
# ==============================================================================
"""## Part 1. Generate a list of corresponding dcm and contour files.

This python script implements the following functionality:
1. It uses data from a csv file to correctly associate ground-truth and label files 
stored in diffent folders.
2. It finds matching ground-truth and label files based on a unique number contained
in their file names
3. It outputs a text file that contains a list of paired ground-truth and label file
names to be used for training.
"""

import dicom
from dicom.errors import InvalidDicomError
import numpy as np
from PIL import Image, ImageDraw
from parsing import *
import matplotlib.pyplot as plt
import matplotlib
import csv
import glob
import re

regex = re.compile(r'\d+')
mri_width = 256
mri_height = 256
SHOW_FIGURE = 0 # 0 = 'No', 1 = 'Yes'

dcm_base_folder = 'final_data/dicoms/'
contr_base_folder = 'final_data/contourfiles/'

csv_filename='final_data/link.csv'
output_list_file_name = 'filename_pairs_list.txt'

namepairs_file = open(output_list_file_name,'w') 

if SHOW_FIGURE:
  fig = plt.figure(figsize=(4,4))
    
with open(csv_filename, 'r') as f:

  reader = csv.reader(f)

  # For each row in csv file...
  for row in reader:        
        	
    if row[0] != 'patient_id':  #skip this row
                
      # Make a list of matched file names
      matched_filenames_list = []
      Nmatches = 0

      dcm_folder_name = dcm_base_folder + row[0] + '/*' 
      ctr_folder_name = contr_base_folder + row[1] + '/i-contours' + '/*' 

      for name in glob.glob(dcm_folder_name): 
        #print name		
        [int(dcm_file_number) for dcm_file_number in regex.findall(name)]
        dcm_file_number = int(dcm_file_number)
        #print(dcm_file_number) 

	for name2 in glob.glob(ctr_folder_name): 
          #print name2
          [int(ctr_file_number) for ctr_file_number in regex.findall(name2)]
          ctr_file_number = int(ctr_file_number)
          #print(int(ctr_file_number)) 

          # If the numbers match... 
          if dcm_file_number == ctr_file_number:
            matched_filenames_list.append( name + ' ' + name2)
            Nmatches = Nmatches + 1
            namepairs_file.write( name + ' ' + name2 + '\n')  

            #Parse data from matched files
            dcm_dict = parse_dicom_file(name)
            contour_points = parse_contour_file(name2)
            mask = poly_to_mask(contour_points, mri_width, mri_height)
               
            if SHOW_FIGURE:         
              plt.imshow(mask, cmap="gray")
              fig.suptitle('Binary mask', fontsize=14)
              plt.pause(0.1)
    
namepairs_file.close()             




