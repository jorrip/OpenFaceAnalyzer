import subprocess
import os
import argparse
import sys


class cd:
    """Context manager for changing the current working directory."""
    def __init__(self, newPath):
        self.newPath = os.path.expanduser(newPath)

    def __enter__(self):
        self.savedPath = os.getcwd()
        os.chdir(self.newPath)

    def __exit__(self, etype, value, traceback):
        os.chdir(self.savedPath)


def analyze_files(openface, rootdir, outputdir, suffix = ''):
    """"Analyzes all files found in rootdir that end with suffix using OpenFace locted at openface. 
    The output is stored in outputdir."""
    list_of_files = []
    subdirs = []
    
    # walk through files and subdirectories in root
    for subdir, dirs, files in os.walk(rootdir):
        for file in files:
            # if suffix is specified: search for files with suffix
            if suffix != '':
                if file.endswith(suffix):
                    list_of_files.append(file)
                    subdirs.append(subdir)
            # else: use every file found
            else:
                list_of_files.append(file)
                subdirs.append(subdir)
                
    print("Found "  + str(len(list_of_files)) + " files to analyze.")
    print("Starting analyzing process...")

    if(len(list_of_files) > 0):
        i = 0
        for file in list_of_files:
            print("\nStarted analyzing file " + str(i+1) + "\n...")
            subprocess.run(['mkdir', os.path.join(outputdir, file)], shell=True) # create an output dir for each analyzed video
            # change current directory (needed for performing openface command)
            with cd(subdirs[i]):
                subprocess.run(openface + ' -f ' + file + ' -out_dir ' + os.path.join(outputdir, file), shell=True)
            print("Finished analyzing file " + str(i+1))
            i += 1
        print("\nAll files are analyzed! The output is found in " + outputdir)  
    else:
        print("No files to analyze.")
        

def parse_args():
    parser = argparse.ArgumentParser(description='OpenFace helper')
    parser.add_argument('-root', nargs='?', dest='root',
                        help='The root directory of the videos. This dir can either contain only videos or subdirectories with videos.',
                        required=True)
    parser.add_argument('-open', nargs='?', dest='open',
                        help='The path to FeatureExtraction.exe from OpenFace.',
                        required=True)
    parser.add_argument('-out', nargs='?', dest='output',
                        help='The directory where the output is saved.',
                        required=True)
    parser.add_argument('-suf', nargs='?', dest='suffix',
                        help='Suffix of the files to be analyzed (e.g. "face.mpg"). If no suffix is specified, all files in rootdir will be analyzed.',
                        required=False)
    return parser.parse_args()


if __name__== "__main__":
    # params parser
    args = parse_args()
    # check params
    if not os.path.isfile(args.open):
        print(args.open + " is not the path to the FeatureExtraction.exe file from OpenFace.")
        sys.exit()
    if not os.path.isdir(args.root):
        print(args.root + " is not a directory.")
        sys.exit()
    if not os.path.isdir(args.output):
        print(args.output + " is not a directory.")
        sys.exit()
    
    # analyze file
    if(args.suffix != None):
        analyze_files(args.open, args.root, args.output, args.suffix)
    else:
        analyze_files(args.open, args.root, args.output)
    
    
    
    
    
    
    
    
