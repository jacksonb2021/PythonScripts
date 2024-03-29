import os
import zipfile
import shutil

def main():
    downloads = "C:\\Users\\jaxru\\Downloads"
    send_to_slideshow = False
    toPath = downloads+ "\\tempextract"
    slideshow_path = "C:\\Users\\jaxru\\Downloads\\slideshow\\"
    pre_existing = []

    output_folder = input("output folder (if empty, send to slideshow)")
    if output_folder=="":
        send_to_slideshow=True
    else:
        toPath = downloads + "\\"+ output_folder

    for i in os.listdir(downloads):
        if i.find("iCloud Photos")!=-1:
            file = downloads+"\\"+i
            if os.path.isdir(file):
                pre_existing.append(file)
                continue
            with zipfile.ZipFile(file, 'r') as zip_ref:
                zip_ref.extractall(toPath)
            os.remove(file)
    ewpath =toPath+"\\iCloud Photos\\"
    try:
        for i in os.listdir(ewpath):
            print(i)
            if i.find(".jpg") !=-1 or i.find(".JPG")!=-1 or i.find(".JPEG")!=-1 or i.find(".jpeg")!=-1:
                os.rename(ewpath+i, toPath+"\\"+i)
        shutil.rmtree(ewpath)
    except:
        pass

    if send_to_slideshow:
        for i in os.listdir(toPath):
            try:
                os.rename(toPath+"\\"+i,slideshow_path+i)
            except FileExistsError:
                iterator = 0;
                while True:
                    try:
                        os.rename(toPath+"\\"+i,slideshow_path+"("+str(iterator)+")"+i)
                        break
                    except:
                        iterator+=1
                        pass
        shutil.rmtree(toPath)





    return


main()
