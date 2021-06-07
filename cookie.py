import pyautogui, time
count = 0
while True:
	count+=1;
	if count > 1:
		currentMouseX, currentMouseY = pyautogui.position()
		if currentMouseY != 359:
			break
	pyautogui.click(x=277, y=359)
	time.sleep(0.000000001)

print(f'Cookies cliked: {count}')