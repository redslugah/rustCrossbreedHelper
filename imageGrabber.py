import pyautogui


def grab_image(place):
    if place == 1:
        img = pyautogui.screenshot(region=(1170, 364, 260, 30))
        img.save("rust.png")
    else:
        img = pyautogui.screenshot(region=(795, 298, 157, 23))
        img.save("rust.png")
