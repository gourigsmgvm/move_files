import os
import shutil


filelist = os.listdir("E:/GOURI/pictures")

print(filelist)

for filename in filelist:
    name, extension = os.path.splitext(filename)
    print(extension)


    source = "E:/GOURI/pictures/" + filename
    dest = "E:/GOURI/pictures/pngs/" + filename

    if extension in ['.png', '.jpg', '.jpeg', '.jfif', '.webp']:
        shutil.move(source, dest)

    else:
        continue



