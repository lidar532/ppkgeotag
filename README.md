# mp_genjpg.ipynb
**mp_genjpg** walks a directory containing 
[raw Sony ARW photo files](https://en.wikipedia.org/wiki/Raw_image_format#ARW), and generates a
Linux bash script which will use all CPU cores to generate jpg or other
photo files.  After gathering the list of raw photos, it divides them by the number
of CPU cores on your computer, and then generates a list for each core of input and output
file names.  A Bash script is generated that will run several copies (one per core) of GraphicsMagick 
configured to convert the raw file to jpg (or other) output format.

The program runs on a windows-10 based jupyter Python Notebook and generates
a bash script suitable for execution on a [Windows-10 WSL (Windows Subsystem for Linux)](https://docs.microsoft.com/en-us/windows/wsl/install-win10).

# PPK-2-PixPos
**PPK-2-PixPos** software is designed to do the following:
1. Run completely online from a Google Chrome, FireFox, or Safari web browser
1. Process raw GNSS dual frequency carrier phase generated by the CWW-PPK Precision GNSS system to precision trajectories.
1. Create a unified directory structure for a GPS and SfM project,
1. Analyse and compare
    * GNSS trajectories,
    * Photo event time Synchronization
1. Use a GNSS trajectory to process Photo Events from the CWW-PPK into precision photo positions that can be loaded loaded into Agisoft Metashape for SfM processing.

## Leveraged Software:
* RTKlib: An Open Source Program Package for GNSS Positioning. The RTKlib manual in pdf can be found at: www.rtklib.com. PPK-2-PixPos uses the Linux commandline version of the RTKlib postprocessor (RNX2RTKP) and other tools.
* Teqc: The Toolkit for GNSS Data.


# ppkgeotag.ipynb
Generates a high precision PPK based GNSS photo location file suitable for reading by Agisoft Photoscan / Metashape and other SfM software. This notebook runs best on Google Colabs.

# PPK_trajectory_analysis.ipynb
Tool box for graphical analysis and comparison of GNSS trajectories generated using various methods and programs including RTKlib, Novatel GrafNav, and The free online Canadian Natural Resources PPP service.  The toolbox allows loading up to 7 different trajectories, and can geherate graphical plots of the data including: 
1. Plan view
1. Elevation
1. Elevation differences
1. Elevation Histograms
1. Trajectory statistics 

This notebook runs best on Google Colabs.

# Test_PPK_lib.ipynb
Python notebook with cells pre-loaded with several test case datasets.  This notebook is intented for developers to test and enhance the ppkgeotag library.  This notebook runs well on Google Colabs or locally in Juypter Notebooks.

# Extract_exif_info.py
Python program to be run from within Agisoft / Metashape to extract photo EXIF information from each photo and write the information to a single EXIF file. The resulting file is required by the ppkgeotagging software to link each photo to the precision GPS position as well as the Flash Event time stamps.
