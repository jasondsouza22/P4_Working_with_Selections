# Commonly used terms when working with selections

# Feature class: A table containing an attribute field that stores geometry that defines shape of a feature
# Feature layer: An in-memory representation of the data in the feature class

# Table: A storage container for rows that contain fields to store data
# TableView: An in-memory representation of that data in a table

import arcpy
import os

gdb_path = r"D:\Second Year\Sem 3\Programming_for_GIS_III\P4_Working_with_Selections\ProProject_Selections\ProProject_Selections.gdb"
restaurant_fc_name = "Wilson_Restaurants"

restaurant_fc_path = os.path.join(gdb_path, restaurant_fc_name)

#Coverting Feature class to Feature Layer
arcpy.management.MakeFeatureLayer(restaurant_fc_path, "restaurant_lyr")

# Getting count of all the features before applying selections
pre_count = arcpy.GetCount_management("restaurant_lyr")
print("The count of all restaurants before applying selections is {}".format(pre_count[0]))


arcpy.management.SelectLayerByAttribute("restaurant_lyr", "NEW_SELECTION", "ALCOHOL = 1")

post_count = arcpy.GetCount_management("restaurant_lyr")
print("The count of restaurants that serve alcohol is {}".format(post_count[0]))

output_alcohol_restaurants = "Wilson_Restaurants_Alcohol"
output_alcohol_restaurants_path = os.path.join(gdb_path, output_alcohol_restaurants)

arcpy.management.CopyFeatures("restaurant_lyr", output_alcohol_restaurants_path)

print("Process Completed")























