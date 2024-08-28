
github_user_name = "emeyers"
package_name = "YData"


import urllib.request
import requests
import os


def download_data(file_name):
    """A function to download YData data"""
    return download_class_file(file_name, "data")
    

def download_image(file_name):
    """A function to download YData images"""            
    return download_class_file(file_name, "images")


def download_homework(homework_number):
    """A function to download homework""" 
    file_name = "homework_" + str(homework_number).zfill(2) + ".ipynb"
    return download_class_file(file_name, "homework")


def download_class_code(class_number, with_answers = False):
    """A function to download class code""" 
    file_name = "class_" + str(class_number).zfill(2) 
    
    if with_answers:
        file_name = file_name + "_answers"
     
    file_name = file_name + ".ipynb"

    download_class_file(file_name, "class_code")


def download_practice_code(practice_number, with_answers = False):
    """A function to download code from the practice sessions""" 
    file_name = "practice_" + str(practice_number).zfill(2) 
        
    if with_answers:
        file_name = file_name + "_answers"
     
    file_name = file_name + ".ipynb"

    download_class_file(file_name, "practice_code")


def download_slides(class_number):
    """A function to download the class slides""" 
    file_name = "class_" + str(class_number).zfill(2) + "_slides.pdf"
    return download_class_file(file_name, "slides")



    

def get_basepath(): 
    """A helper function that returns the base URL for downloading files from the YData GitHub repository."""
    
    base_path = "https://raw.githubusercontent.com/" + github_user_name + "/" + package_name + "/main/ClassMaterial/"
    
    return base_path




def get_github_file_names(): 
    """A helper function that returns a dictionary listing all the files on the YData GitHub repository."""
 
    # download info on all the files that are on the YData GitHub site
    url = "https://api.github.com/repos/" + github_user_name + "/" + package_name + "/git/trees/main?recursive=1"
    r = requests.get(url = url)
    github_files = r.json()

    
    # Create a dictionary that list all the files in that are in the different class directories
    class_files = {}
    
    for i in range(len(github_files["tree"])):

        curr_file_name = github_files["tree"][i]["path"]
        
        if curr_file_name.startswith("ClassMaterial/"):
            curr_file_pieces = curr_file_name.split("/")
            
            if len(curr_file_pieces) == 3:
                class_files[curr_file_pieces[1]] = class_files.get(curr_file_pieces[1], []) + [curr_file_pieces[2]]
            
    return class_files





def download_class_file(file_name, file_type):
    """A helper function that can download any class_code, data, homework, images, or slides on the YData GitHub repository."""

    
    # check that file_type is one of:  class_code, data, homework, images, slides
    if file_type not in ["class_code", "data", "homework", "images", "slides", "project"]:
        raise Exception('The file_type argument must be a string set to either: "class_code", "data", "homework", "images", "slides", "project"')


    full_file_name = get_basepath() + "/" + file_type + "/" + file_name
    
    
    # check whether the file exists on the GitHub YData website
    github_file_names = get_github_file_names()
    if file_name not in github_file_names[file_type]:
        raise Exception("The file you are requesting " + file_name + " does not exist on the YData GitHub site. The " + file_type +" files that exist are: " + ' '.join(github_file_names[file_type]))
        
        
    # Only download the file if it doesn't already exist on one's computer
    # Could make this an assertion error, but better to just print a message for now
    if os.path.exists(file_name):
        print("The file `" + file_name + "` already exists.")
        print("If you would like to download a new copy of the file, please rename the existing copy of the file.")
    else:
        urllib.request.urlretrieve(full_file_name, file_name)




