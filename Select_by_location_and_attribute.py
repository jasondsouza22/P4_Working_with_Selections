import arcpy
import os

gdb_path = r"D:\Second Year\Sem 3\Programming_for_GIS_III\P4_Working_with_Selections\ProProject_Selections\ProProject_Selections.gdb"
restaurant_fc_name = "Wilson_Restaurants"
hist_fc_name = "Wilson_Histdist"
crime96_fc_name = "Wilson_Crimes96"

restaurant_fc_path = os.path.join(gdb_path, restaurant_fc_name)
hist_fc_path = os.path.join(gdb_path,hist_fc_name)
crime96_fc_path = os.path.join(gdb_path, crime96_fc_name)

# Converting a feature class to feature layer
arcpy.management.MakeFeatureLayer(restaurant_fc_path, "restaurant_lyr")
arcpy.management.MakeFeatureLayer(hist_fc_path, "hist_dist_lyr")
arcpy.management.MakeFeatureLayer(crime96_fc_path, "crime96_lyr")

arcpy.management.SelectLayerByAttribute("restaurant_lyr", "NEW_SELECTION", "ALCOHOL = 1")
count = arcpy.GetCount_management("restaurant_lyr")
print("The count of restaurants that serve alcohol is {}".format(count[0]))

arcpy.management.SelectLayerByLocation("restaurant_lyr", "WITHIN_A_DISTANCE", "hist_dist_lyr", "1000 feet", "SUBSET_SELECTION")
restaurant_1000_feet = arcpy.GetCount_management("restaurant_lyr")
print("The count of restaurant within 1000 feet is {}".format(restaurant_1000_feet[0]))

arcpy.management.SelectLayerByLocation("crime96_lyr", "WITHIN_A_DISTANCE", "restaurant_lyr", "500 feet", "SUBSET_SELECTION")
crimes_500_feet = arcpy.GetCount_management("crime96_lyr")
print("The count of crimes within 500 feet is {}".format(crimes_500_feet[0]))

arcpy.management.SelectLayerByAttribute("crime96_lyr", "SUBSET_SELECTION", "ALCOHOL > 0")
count = arcpy.GetCount_management("crime96_lyr")
print("The count of crimes is {}".format(count[0]))

print("Process Completed")
