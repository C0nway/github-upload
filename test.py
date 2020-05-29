import os
import win32api


def test(dirs):
    if os.path.isfile(dirs):
        with open(dirs,"rb+") as f:
            fdata = f.read()
            
    else:
        print ("Not file!")


if __name__ == '__main__':
    test(r"F:\Python\test")