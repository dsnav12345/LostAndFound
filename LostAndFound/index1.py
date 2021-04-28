from colordescriptor import ColorDescriptor
import argparse
import glob
import cv2
def indexpy(dataset,index):
    print('hello')
    cd=ColorDescriptor((8,12,3))
    output=open(index,"w")
    for imagePath in glob.glob(dataset+"/*.jpg"):
        imageId=imagePath[imagePath.rfind("/")+1:]
        image=cv2.imread(imagePath)
        features=cd.describe(image)
        features=[str(f) for f in features]
        output.write("%s,%s\n" % (imageId,",".join(features)))
    output.close()
