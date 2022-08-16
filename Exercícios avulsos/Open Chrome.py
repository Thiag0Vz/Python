r = input ("Do you want to open Google Chrome and research for news? y/n ")

if r == 'y':


        import subprocess
        subprocess.Popen('C:\Program Files (x86)\Google\Chrome\Application\chrome.exe')

        import pyautogui
        pyautogui.hotkey('alt','space')
        pyautogui.hotkey('x')

        pyautogui.typewrite ('Notícias')

        pyautogui.hotkey('enter')

        pyautogui.click (185, 783, duration=0.5)

if r == 'n':
    print ("Ok")
    exit()

