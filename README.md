
# PPK-RTKlib [ PPK-RTKlib ]
**PPK-RTKlib** does the following:
1.  Using Google Colabs, Runs completely online, in the cloud, from a Google Chrome, FireFox, or Safari web browser
1. Create a unified directory structure for a GPS and SfM project,
1. Process raw GNSS dual frequency carrier phase generated by the CWW-PPK Precision GNSS system to precision trajectories.

# CORS_Lib.ipynb [ Run in Colabs ]
**COR_Lib** does the following:
1. 1. Using Google Colabs, Runs completely online, in the cloud, from a Google Chrome, FireFox, or Safari web browser
1. Library of tools to gather NOAA CORS data.  
1. Eliminates the need to manually round up CORS data using a browser, uploading, etc.

# PPK-2-PixPos  [ Run in Colabs ](https://colab.research.google.com/github/lidar532/ppkgeotag/blob/2020-1020-dev/PPK_2_PixPos.ipynb)
**PPK-2-PixPos** software is designed to do the following:
1.  Using Google Colabs, Runs, completely online, in the cloud, from a Google Chrome, FireFox, or Safari web browser
1. Photo event time Synchronization
1. Use a GNSS trajectory to process Photo Events from the CWW-PPK into precision photo positions that can be loaded loaded into Agisoft Metashape for SfM processing.

# PPK_trajectory_analysis.ipynb [ Run in Colabs ]
**PPK_trajectory_analysis** is a tool box for graphical analysis and comparison of GNSS trajectories generated using various methods and programs including RTKlib, Novatel GrafNav, and The free online Canadian Natural Resources PPP service.  The toolbox allows loading up to 7 different trajectories, and can geherate graphical plots of the data including: 
1. Plan view
1. Elevation
1. Elevation differences
1. Elevation Histograms
1. Trajectory statistics 

# Extract_exif_info.py  ( Run locally as a script in Agisoft metashape or Photoscan )
Python program to be run from within Agisoft / Metashape to extract photo EXIF information from each photo and write the information to a single EXIF file. The resulting file is required by the ppkgeotagging software to link each photo to the precision GPS position as well as the Flash Event time stamps.

# mp_genjpg.ipynb  ( Run in local Juypter Notebook )
**mp_genjpg** walks a directory containing 
[raw Sony ARW photo files](https://en.wikipedia.org/wiki/Raw_image_format#ARW), and generates a
Linux bash script which will use all CPU cores to generate jpg or other
photo files.  After gathering the list of raw photos, it divides them by the number
of CPU cores on your computer, and then generates a list for each core of input and output
file names.  A Bash script is generated that will run several copies (one per core) of GraphicsMagick 
configured to convert the raw file to jpg (or other) output format.

The program runs on a windows-10 based jupyter Python Notebook and generates
a bash script suitable for execution on a [Windows-10 WSL (Windows Subsystem for Linux)](https://docs.microsoft.com/en-us/windows/wsl/install-win10).

## Leveraged Software:
* RTKlib: An Open Source Program Package for GNSS Positioning. The RTKlib manual in pdf can be found at: www.rtklib.com. PPK-2-PixPos uses the Linux commandline version of the RTKlib postprocessor (RNX2RTKP) and other tools.
* Teqc: The Toolkit for GNSS Data.
* Exiftool.




