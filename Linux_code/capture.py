import pygame
import os
import pygame.camera
import time
import pysftp as sftp

filename = "Rpi_" + time.strftime("%m%d%y%H%M%S") + ".jpg"
localpath = "/home/tushaar/Desktop/minor_project/images/" + filename
remotepath = "/home/pi/Desktop/minor_project/images/" + filename

pygame.camera.init()
cam = pygame.camera.Camera("/dev/video0", (640, 640))
cam.start()
image = cam.get_image()
pygame.image.save(image, localpath)

try:
    conn = sftp.Connection(host='10.42.0.178', username='pi', password='raspberry')
    conn.put(localpath, remotepath)
    conn.close()
except Exception, e:
    print str(e)
