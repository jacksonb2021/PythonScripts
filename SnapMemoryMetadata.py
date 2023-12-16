import os
# from PIL.ExifTags import TAGS
import string
from time import strptime

from exif import Image
import random
import piexif
from datetime import datetime


def assign_metadata_to_photo(photo_path, year, month, date):
    # Load the EXIF data from the photo
    exif_dict = piexif.load(photo_path)

    # Convert the year, month, and date to string format
    year_str = str(year)
    month_str = str(month).zfill(2)
    date_str = str(date).zfill(2)

    # Assign the metadata values to the EXIF data
    exif_dict["Exif"][piexif.ExifIFD.DateTimeOriginal] = f"{year_str}:{month_str}:{date_str} 00:00:00"

    # Convert the EXIF data back to binary format
    exif_bytes = piexif.dump(exif_dict)

    # Save the updated EXIF data to the photo
    piexif.insert(exif_bytes, photo_path)


def main():
    path = input("input path of your photos extracted from the snapchat datadump")
    if path == "":
        path = os.path.dirname(os.path.realpath(__file__))

    years = os.listdir(path)
    for year in years:
        if len(year.split(' ')) !=1:
            continue
        temppath = path+'\\'+year
        for file in os.listdir(temppath):
            filepath = temppath + "\\" + file
            # im = Image.open()
            # TODO: only works with photos so far
            if file.split(".")[1]!="jpg":
                continue

            filename = file.split('-')
            # letters = string.ascii_lowercase
            # newname = ''.join(random.choice(letters) for i in range(5))
            month = filename[0]
            if len(filename) == 2:
                newstr = filename[1].split('.')
                day = newstr[0]
            elif len(filename) == 3:
                day = filename[1]
            print(f'filename= {filename} and day = {day} and month = {month}')
            month_num = datetime.strptime(month, '%B').month
            formattedmonth = f"{month_num:02}"
            print(f'{month_num},{formattedmonth}')
            # print(formattedmonth)
            formattedday = f"{day:02}"
            assign_metadata_to_photo(filepath, year, month_num, day)
        # print(formattedday)
        # exif_dict = piexif.load(mainpath+"\\"+file)
        # #$newmonth = strptime(month)
        # #parsedate = datetime.strptime(file[0:16], "%Y-%m-%d-%H-%M-%S")
        # newExifDate = f"{year}:{formattedmonth}:{formattedday} 12:00:00"
        #
        #
        # exif_dict['Exif'][piexif.ExifIFD.DateTimeOriginal] = newExifDate
        # exif_dict['Exif'][piexif.ExifIFD.DateTimeDigitized] = newExifDate
        # exif_bytes = piexif.dump(exif_dict)
        # piexif.insert(exif_bytes, mainpath+"\\"+file)


    # with open(mainpath+"\\"+file,'rb') as img_file:
    # 	hmm = Image(img_file)
    # hmm.set("datetime", f'{year}:{month}:{day} 12:00:00')
    #
    # with open(f'{modifiedpath}\\{file}','wb') as \
    # 		new_image_file:
    # 	new_image_file.write(hmm.get_file())


main()
