import win32file
import glob
import win32con

def togglefileattribute(filename, fileattribute, value):
    bitvector = win32file.GetFileAttributes(filename)
    if value:
        bitvector |= fileattribute
    else:
        bitvector &= ~fileattribute
    win32file.SetFileAttributes(filename, bitvector)

for filename in glob.iglob(".\\**/*" , recursive = True):
    togglefileattribute(filename, win32con.FILE_ATTRIBUTE_ARCHIVE, False)
    print(f"Processed {filename}")