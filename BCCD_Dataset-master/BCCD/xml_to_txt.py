import os
import sys
import xml.etree.ElementTree as ET
import glob

def xml_to_txt(indir,outdir):

    os.chdir(indir)
    annotations = os.listdir('.')
    annotations = glob.glob(str(annotations)+'*.xml')
    print(annotations)
    for i, file in enumerate(annotations):

        file_save = file.split('.')[0]+'.txt'
        # file_txt=os.path.join(outdir,file_save)
        file_txt = outdir+"\\"+file_save
        # print(file_save)
        f_w = open(file_txt, 'w+')

        # actual parsing
        in_file = open(file)
        tree=ET.parse(in_file)
        root = tree.getroot()
        filename = root.find('filename').text  #這裡是xml的根，獲取filename那一欄
        for obj in root.iter('object'):
                current = list()
                name = obj.find('name').text   #這裡獲取多個框的名字，底下是獲取每個框的位置

                xmlbox = obj.find('bndbox')
                xn = xmlbox.find('xmin').text   
                xx = xmlbox.find('xmax').text
                yn = xmlbox.find('ymin').text
                yx = xmlbox.find('ymax').text
                #print xn
                f_w.write(filename +' '+xn+' '+yn+' '+xx+' '+yx+' ')
                f_w.write(name+'\n')

indir='D:\\dataset\\Deep Learning HW\\BCCD_Dataset-master\\BCCD\\Annotations'   #xml目錄
outdir='D:\\dataset\\Deep Learning HW\\BCCD_Dataset-master\\BCCD\\Annotations_txt'  #txt目錄

xml_to_txt(indir,outdir)