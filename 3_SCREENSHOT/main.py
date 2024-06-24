import pyscreenshot
import playsound
import time

for i in range(10,1,-1):
    print(f"Screen Shot Will be take in {i} second")
    time.sleep(1)
image = pyscreenshot.grab()
playsound.playsound('3_SCREENSHOT\Beep.mp3')
# image.show()
image_name = input("What is the Image Name?\n")
image_name = "".join([image_name,".png"])
image.save(image_name)