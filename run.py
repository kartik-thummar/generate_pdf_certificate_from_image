import os
import cv2
import img2pdf
from PIL import Image

list_of_names = []

names_path = "names/name-data.txt"
imgs_path = "generated/"
pdfs_path = "generated_pdfs/"
reference_certificate_img = "samples/sample1.png"


def delete_old_data():
   for i,img in enumerate(os.listdir(imgs_path)):
      os.remove(f"{imgs_path}{img}")
      print(f"{i+1}. {img} image deleted")
   print("\n\n")
   
   for i, pdf in enumerate(os.listdir(pdfs_path)):
      os.remove(f"{pdfs_path}{pdf}")
      print(f"{i+1}. {img} pdf deleted")
   print("\n\n")
   
def clear_names():
   with open(names_path,'w') as f:
      f.write(' ')
      print("All names are removed")


def names():
   with open(names_path) as f:
      for line in f:
         list_of_names.append(line.strip())
   print(list_of_names)

def generate_certificates():

   for index, name in enumerate(list_of_names):
      certificate_template_image = cv2.imread(reference_certificate_img)
      cv2.putText(certificate_template_image, name.strip(), (550,750), cv2.FONT_HERSHEY_SCRIPT_SIMPLEX, 4, (0, 0, 250), 5, cv2.LINE_AA)
      cv2.imwrite("generated/{}.jpg".format(name.strip()), certificate_template_image)
      print("Processing {} / {}".format(index + 1,len(list_of_names)))
      
def image2pdf():

   dires = os.listdir(imgs_path)

   for image_name in dires:

      image = Image.open(f'{imgs_path}{image_name}')
      pdf_bytes = img2pdf.convert(image.filename)
      pdf_name = f"{pdfs_path}{image_name.split('.')[0]}.pdf"
      with open(pdf_name,'wb') as f:
         f.write(pdf_bytes)
      print(f"{imgs_path}{pdf_name} generated")

def main():
   # delete_old_data()
   # clear_names()
   names()
   generate_certificates()
   image2pdf()

if __name__ == '__main__':
   main()
