import glob
import os

for item in glob.glob("/home/eduard.mainou/hmdb51/flow/tvl1_flow/v/**/*.jpg"):
    
    os.rename(item, item.replace("flow_x_","flow_y_")) 

