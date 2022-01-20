import cv2
import random
import dropbox
import time

value = random.randint(0,100000)
start_time = time.time()

def take_snapshot():
    #initalize cv2
    videoCaptureObject = cv2.VideoCapture(0)
    result = True

    while(result):
        #reading the frame while the camera is on
        ret, frame = videoCaptureObject.read()
        print(ret)
        #save image to any storage device
        img_name = "picture" + str(value) +".Jpg"
        cv2.imwrite(img_name, frame)
        start_time = time.time
        result = False
        
    return img_name

    #releases the camera
    videoCaptureObject.release()
    #closes all the windows that might be open while this process
    cv2.destroyAllWindows()

def upload_File(img_name):
    access_token = 'VnT7xQhrGwkAAAAAAAAAAYzDNcYf9y3e9t7BkahVPdNur2m5jNfOlAuEdjr4VWKd'
    file = img_name

    
    file_from = file
   
    file_to = "/new folder/" + (img_name)
    dbx = dropbox.Dropbox(access_token)
    with open(file_from, 'rb') as f:
        dbx.files_upload(f.read(), file_to, mode = dropbox.files.WriteMode.overwrite)
        print("File uploaded sucessfully")



def main():
    while (True):
        take_snapshot()
        if ((time.time()-start_time)>=1):
            name=take_snapshot()
            upload_File(name)

main()
