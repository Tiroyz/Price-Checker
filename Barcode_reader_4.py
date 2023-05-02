import cv2
from pyzbar.pyzbar import decode
  
# Make one method to decode the barcode
def BarcodeReader(image):
         
    # read the image in numpy array using cv2
    img = cv2.imread(image)
      
    # Decode the barcode image
    detectedBarcodes = decode(img)
      
    # If not detected then print the message
    if not detectedBarcodes:
        print("Barcode Not Detected or your barcode is blank/corrupted!")
    else:
       
          # Traverse through all the detected barcodes in image
        for barcode in detectedBarcodes: 
           
            # Locate the barcode position in image
            (x, y, w, h) = barcode.rect
             
            # Put the rectangle in image using
            # cv2 to highlight the barcode
            cv2.rectangle(img, (x-10, y-10),
                          (x + w+10, y + h+10),
                          (255, 0, 0), 2)
                 
    #Display the image
    # cv2.imshow("Image", img)
    # cv2.namedWindow("img", cv2.WINDOW_NORMAL)
    # cv2.waitKey(0)
    cv2.destroyAllWindows()
    if barcode.data!="":
               
            # Return the barcode data
                return barcode.data     #, barcode.type
 
# if __name__ == "__main__":
# Take the image from user
from glob import glob
barcodes = glob("image.png")
for image in barcodes:
    # image="Img.jpg"
    print(BarcodeReader(image))