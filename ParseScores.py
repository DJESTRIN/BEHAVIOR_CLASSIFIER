# -*- coding: utf-8 -*-
""" A general script for parsing data from Deeplabcut and video score'd data """
""" Libraries """
import numpy as np
import pandas as pd
import os, glob

""" Parse behavior class """
class ParseBehavior():
    def __init__(csv_file_name, tracking_file_name):
        self.csv_file_name = csv_file_name
        self.tracking_file_name = tracking_file_name
        self.scoring_start, self.scoring_stop = self.read_scores()
        self.tracking_data = self.read_tracking()
        self.merged_dataframe = self.merge_dataframes()
    
    def read_scores(self):
        # read scoring data into a dataframe
        
        return scoring_start, scoring_stop
    
    def read_tracking(self):
        # Bring in the tracking coordinate data from the select video
        # clip data onset and offset by scoring start and stop 
        
        return tracking_data
        
    def merge_dataframes(self):
        # Take scoring and tracking data and put into single dataframe. 
        
        return merged_dataframe

    def ground_truth_video(self):
        # Generate video based on the merged dataframe 
        
        return
    
""" Create multi-animal CSDS class maCSDS() which inherits the above class """
class multi_CSDS(ParseBehavior):
    def __init__():
        self.updated_dataframe = self.update_dataframe()
        self.video()
    
    def proximity(self):
        
        return proximity
    
    def velocity(self):
        return velocity
    
    def acceleration(self):
        return acceleration
    
    def angular_velocity(self):
        return angular_velocity
        
    def update_dataframe(self):
        return updated_dataframe
    
    def video():
        return
            
def Match_files(video_file_name):

    return scored_filename       
    

if __name__ == "main": 
    """ Get videos file names from direcotry of choice """
    os.chdir("") #Video file directory
    videos = glob.glob('*.mp4')
    dataset = pd.DataFrame()
    
    """ Loop through videos => generate training dataset """
    for video_filename in videos:
        scored_filename = Match_files(video)
        parsed_video = multi_CSDS(video_filename, scored_filename)
        dataset = dataset.append(parsed_video.updated_dataframe)

    """ Save dataset as csv file """









""" Put data in large table
    Dependent variable: (1) Freezing, (2) Running, (3) Jumping, (3) Dominating, (4) Pursuing, (5) Investigating, (6) Nothing
    Mouse (1) Distance from CD
 """