import os
import zipfile
import shutil

def main():
    downloads = "C:\\Users\\jaxru\\Downloads"
    send_to_slideshow = False
    toPath = downloads+ "\\tempextract"
    slideshow_path = "C:\\Users\\jaxru\\Downloads\\slideshow\\"

    output_folder = input("output folder (if empty, send to slideshow)")
    if output_folder=="":
        send_to_slideshow=True
    else:
        toPath = downloads + "\\"+ output_folder

    for i in os.listdir(downloads):
        if i.find("iCloud Photos")!=-1:
            file = downloads+"\\"+i
            with zipfile.ZipFile(file, 'r') as zip_ref:
                zip_ref.extractall(toPath)
            os.remove(file)
    ewpath =toPath+"\\iCloud Photos\\"
    for i in os.listdir(ewpath):
        print(i)
        if i.find(".jpg") !=-1 or i.find(".JPG")!=-1:
            os.rename(ewpath+i, toPath+"\\"+i)
    shutil.rmtree(ewpath)
    if send_to_slideshow:
        for i in os.listdir(toPath):
            os.rename(toPath+"\\"+i,slideshow_path+i)
        shutil.rmtree(toPath)





    return


main()
