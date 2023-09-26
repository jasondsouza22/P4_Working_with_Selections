import arcpy
import os

gdb_path = r"D:\Second Year\Sem 3\Programming_for_GIS_III\P4_Working_with_Selections\ProProject_Selections\ProProject_Selections.gdb"
restaurant_fc_name = "Wilson_Restaurants"
hist_fc_name = "Wilson_Histdist"

restaurant_fc_path = os.path.join(gdb_path, restaurant_fc_name)
hist_fc_name_path = os.path.join(gdb_path,hist_fc_name)

# Converting a feature class to feature layer
arcpy.management.MakeFeatureLayer(restaurant_fc_path, "restaurant_lyr")
arcpy.management.MakeFeatureLayer(hist_fc_name_path, "hist_dist_lyr")

pre_count = arcpy.GetCount_management("restaurant_lyr")
print(" Count of the restaurants before applying selection is ",pre_count)

arcpy.management.SelectLayerByLocation("restaurant_lyr","WITHIN_A_DISTANCE", "hist_dist_lyr", "500 feet")

post_count = arcpy.GetCount_management("restaurant_lyr")
print("Count of restaurants within 500 feet of historic dist", post_count)

output_restaurant_histdist = "Restaurant_within_500feet"
output_restaurant_histdist_path = os.path.join(gdb_path,output_restaurant_histdist)

arcpy.management.CopyFeatures("restaurant_lyr" , output_restaurant_histdist_path)

print("Process Completed")