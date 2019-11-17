# ppkgeotag.ipynb
Generates a high precision PPK based GNSS photo location file suitable for reading by Agisoft Photoscan / Metashape and other SfM software. This notebook runs best on Google Colabs.

# PPK_trajectory_analysis..ipynb
Tool box for graphical analysis and comparison of GNSS trajectories generated using various methods and programs including RTKlib, Novatel GrafNav, and The free online Canadian Natural Resources PPP service.  The toolbox allows loading up to 7 different trajectories, and can geherate graphical plots of the data including: 
1. Plan view
1. Elevation
1. Elevation differences
1. Elevation Histograms
1. Trajectory statistics 

This notebook runs best on Google Colabs.

# Test_PPK_lib..ipynb
Python notebook with cells pre-loaded with several test case datasets.  This notebook is intented for developers to test and enhance the ppkgeotag library.  This notebook runs well on Google Colabs or locally in Juypter Notebooks.

# Extract_exif_info.py
Python program to be run from within Agisoft / Metashape to extract photo EXIF information from each photo and write the information to a single EXIF file. The resulting file is required by the ppkgeotagging software to link each photo to the precision GPS position as well as the Flash Event time stamps.
