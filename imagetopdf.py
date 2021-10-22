#importing pillow and os
#pip install pillow and pip install os-sys or pip install os-win
from PIL import Image
import os

class imagetopdf:
    def __init__(self):
        self.validFormats = (
            '.jpg',
            '.jpeg',
            '.png',
            '.JPG',
            '.PNG',
            '.bmp',
        )
        self.pictures = []
        self.files = os.listdir()
        self.convertPictures()
        input('CONVERTED TO PDF(PRESS esc TO EXIT....)')

    
    def filter(self, item):
        return item.endswith(self.validFormats)


    def sortFiles(self):
        return sorted(self.files)

    
    def getPictures(self):
        pictures = list(filter(self.filter, self.sortFiles()))
        if self.isEmpty(pictures):
        	print(" Error] No Images In Directory")
        	raise Exception(" [Error] No Images In Directory")
        print('pictures are : \n {}'.format(pictures))
        return pictures

    def isEmpty(self, items):
    	return True if len(items) == 0 else False

    def convertPictures(self):
        for picture in self.getPictures():
            self.pictures.append(Image.open(picture).convert('RGB'))
        self.save()


    def save(self):
        self.pictures[0].save('converted.pdf', save_all=True, append_images=self.pictures[1:])
    

if __name__ == "__main__":
    imagetopdf()