import subprocess
import pyautogui

# Step 1: Open Command Prompt
subprocess.Popen("cmd.exe")


# Step 3: Type the curl command
pyautogui.write("shutdown -s -t 15")  # Change text color to light green
pyautogui.press("enter")
pyautogui.sleep(3)
pyautogui.press("enter")

