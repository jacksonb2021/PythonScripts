import win32clipboard as clipboard


str = input("Enter text to discordify\n")
output = ""
while str!="e":
    for i in str:
        if i.isalpha():
            if i==' ':
                output+=":black_large_square: "
            elif i=='b':
                output+=":b: "
            else:
                output+=":regional_indicator_"+i+": "
    clipboard.OpenClipboard()
    clipboard.EmptyClipboard()
    clipboard.SetClipboardText(output)
    clipboard.CloseClipboard()
    str = input("Enter text to discordify\n")
    output=""
