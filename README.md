# OpenFaceAnalyzer
This file can be used to analyze multiple videos in a specified root directory using the [OpenFace](https://github.com/TadasBaltrusaitis/OpenFace) software. The output is saved in an organized manner in a specified directory.
## Prerequisites
* Windows
* Python 3
* OpenFace should be downloaded and installed according to the installation [wiki](https://github.com/TadasBaltrusaitis/OpenFace/wiki) of OpenFace
## Usage
1. Download run_open_face.py
2. Specify the root directory where all videos that should be analyzed are located using ```-root [rootdir]```. This can either be a folder containing just videos, or a folder with subdirectories containing the videos.
3. Specify where FeatureExtraction.exe from [OpenFace](https://github.com/TadasBaltrusaitis/OpenFace) is located using ```-open [path] ```
4. Specify where the output should be saved using ```-out [output directory]```
5. Use the optional parameter ```-suf [suffix]``` to specify which files will be analyzed. Example: with ```-suf face.mpg``` only files that end with face.mpg are analyzed. If this parameter is omitted all files in rootdir are analyzed.

Example:
```
python C:\Downloads\run_open_face.py -root C:\workspaces\videos -open C:\OpenFace\OpenFace_2.0.5_win_x64\FeatureExtraction.exe -out C:\OpenFace\Output -suf face.mpg
```

## Output
For every video that is analyzed a folder is created in the specified output directory containing the outputs from the OpenFace software.
