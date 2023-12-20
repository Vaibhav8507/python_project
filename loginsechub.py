import pyautogui
import time
from PIL import ImageChops
import pytesseract
from PIL import Image
import cv2
print("hello world")
time.sleep(10)
x, y = pyautogui.position()
print(f"Mouse cursor position: X = {x}, Y = {y}")

# pyautogui.hotkey('win', 's')
# pyautogui.write('Google Chrome')
# pyautogui.press('enter')
# time.sleep(9)
# # pyautogui.click(1287, 1040)
#
# pyautogui.click(252, 99)
# time.sleep(2)
# pyautogui.write("10.20.202.211/auth/authenticate")
# pyautogui.press("enter")
# time.sleep(3)
# pyautogui.click(121, 805)
# time.sleep(3)
# pyautogui.moveTo(148, 862)
# pyautogui.click(button='left')
#
# time.sleep(15)
#
# x, y = pyautogui.locateCenterOnScreen("D:/execute.png",confidence=0.9)
# pyautogui.moveTo(x, y, 1)
# pyautogui.click()
#
# screenshot = pyautogui.screenshot()
# screenshot.save('image10.png')
# time.sleep(5)
# pytesseract.pytesseract.tesseract_cmd = r'C:/Users/VNarule/AppData/Local/Programs/Tesseract-OCR/tesseract.exe'
# screenshot = Image.open('image10.png')
#
# toaster_text = pytesseract.image_to_string(screenshot)
# print("toastertext:",toaster_text)



# refrence_image = Image.open('D:/error_msg.png')
# difference = ImageChops.difference(refrence_image,saved)
# img_location = pyautogui.locateOnScreen('alert1.png')
# rms_difference = ImageChops.sqrt(ImageChops.mean(ImageChops.square(difference)))
# print(rms_difference)
# threshold = 10
# if rms_difference < threshold:
#     print("image match")
#
# else:
#     print("img not found")












# x,y = pyautogui.locateCenterOnScreen("D:/error_msg.png",confidence=0.9)
# pyautogui.moveTo(x, y, 1)
# pyautogui.click()
# time.sleep(5)




