# By Ritik Mehra

import pyautogui as pt
import keyboard
from pynput.mouse import Controller, Button
from time import sleep

# You must have pin your whatsapp in your Taskbar
# This bot opens everything through Cursor Navigation


mouse = Controller()

sleep(2)

position1 = pt.locateOnScreen("Whatsapp-Bot\Watsapp_logo.png", confidence=0.6)
x = position1[0]
y = position1[1]


class whatsapp():

    def open_whatsapp():

        try:
            global x, y

            # Add Whatsapp_logo.png file directory manually if not working
            position = pt.locateOnScreen(
                "Images\Message_box.PNG", confidence=0.6)
            x = position[0]
            y = position[1]
            pt.moveTo(x+30, y+20, duration=0.05)
            mouse.click(Button.left, 1)
        except Exception as e:
            print('Exception (open_whatsapp): ', e)

    def goto_search_button():
        try:
            global x, y

            # Add Search.png file directory manually if not working

            position = pt.locateOnScreen(
                "Images\Search.png", confidence=0.6)
            x = position[0]
            y = position[1]

            pt.moveTo(x+10, y+10, duration=0.05)
            mouse.click(Button.left, 1)
            sleep(1)

            # write your friends name or group name in place of Script Testing

            keyboard.write("Script Testing")  # <--------here

            pt.press("enter")
        except Exception as e:
            print('Exception (goto_search_button): ', e)

    def send_message():
        try:
            global x, y

        # Add Message_box.png file directory manually if not working

            position = pt.locateOnScreen(
                "Images\Message_box.png", confidence=0.6)
            x = position[0]
            y = position[1]

            pt.moveTo(x+10, y+10)
            mouse.click(Button.left, 1)
            keyboard.write("Sending Message using python script!!!!")
            pt.press("enter")
        except Exception as e:
            print('Exception (send_message): ', e)


ob = whatsapp

ob.open_whatsapp()
sleep(10)
ob.goto_search_button()
sleep(3)
ob.send_message()
