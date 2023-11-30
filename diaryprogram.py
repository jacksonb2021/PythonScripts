from datetime import datetime


def make_dictionary():
    file = open("data.txt", 'r')
    lines = file.readlines()
    count = 0
    dictionary = dict()
    new = []
    for i in lines:
        line = i.strip('\n')
        if line != '':
            new.append(line)
    while count < len(new):
        date = new[count]
        text = new[count + 1].strip('\n')
        dictionary[date] = text
        count += 2
    dictionary = sort_dates(dictionary)
    return dictionary

def sort_dates(date_dict):
    sorted_dates = sorted(date_dict.items(), key=lambda x: datetime.strptime(x[0], "%m/%d/%Y"))
    sorted_dict = {key: value for key, value in sorted_dates}
    return sorted_dict

def read(dictionary):
    months = ['January', 'February', 'March', 'April', 'May', 'June', 'July', 'August', 'September',
              'October', 'November', 'December']
    for date,text in dictionary.items():
        datearr = date.split("/")
        monthstr = months[int(datearr[0])-1]
        print(f"Date: {monthstr + ' ' +datearr[1] +', '+ datearr[2]}")
        while len(text) > 100:
            idx = text[:100].rfind(' ')  # find the index of the last space character within the first 100 characters
            if idx == -1:  # no space character found, so break the line at the 100th character
                idx = 100
            print(text[:idx])
            text = text[ idx + 1:]

        print(text)
        print()



def write():
    file=open('data.txt', 'a')
    date=datetime.now()
    file.write('\n\n')
    file.write(date.strftime('%m/%d/%Y')+'\n')
    stuff=input("Whats new today?\n")
    file.write(stuff)
    print()
    file.close()

def append():
    file=open("data.txt", 'a')
    stuff=input("What else do you want to add?\n")
    file.write(stuff)
    print()
    file.close()

def lookup():
    date=input("Enter date MM/DD/YYYY\n")
    print()
    dictionary=make_dictionary()
    try:
        print(f"Date: {date}")
        text=dictionary[date]
    except KeyError:
        print("No value exists for this date")
        return
    while len(text) > 100:
        print(text[:100])
        text = text[100:]
    print(text)

def insert(dictionary):
    date = input("Enter date MM/DD/YYYY\n")
    text = input("Enter entry")
    dictionary[date] = text
    overwrite(dictionary)

def overwrite(dictionary):
    file = open("data.txt", "w")
    str=""
    for key,val in dictionary:
        str += f"{key}\n{val}\n"
    str.strip("\n")
    file.write(str)
    print()
    file.close()

def yesterday():
    file=open('data.txt', 'a')
    date=datetime.now()
    file.write('\n\n')

    date = date.strftime('%m/%d/%Y')
    day = date.split("/")
    newdate = f'{day[0]}/{int(day[1])-1}/{day[2]}'
    file.write(newdate+'\n')
    stuff=input("Whats new yesterday?\n")
    file.write(stuff)
    print()
    file.close()



def main():
    str = "r for read, w for write, l for lookup, a for append, y for yesterday, q for quit\n"
    whatdo=input(str)
    file=open("data.txt")
    file.close()
    dictionary=make_dictionary()
    while whatdo != 'q':
        dictionary = make_dictionary()
        if whatdo == "r":
            print()
            read(dictionary)
        elif whatdo == 'w':
            print()
            write()
            dictionary = make_dictionary()
        elif whatdo == 'l':
            print()
            lookup()
        elif whatdo == 'a':
            print()
            append()
            dictionary = make_dictionary()
        elif whatdo == 'y':
            print()
            yesterday()
            dictionary = make_dictionary()
        else:
            print("\nplz enter some real shit")

        print()
        whatdo = input(str)

    print("goodbye")



main()