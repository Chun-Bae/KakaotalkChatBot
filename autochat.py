import pyautogui
import time
import clipboard
import pyperclip

def read_message(): # 메시지를 읽어오는 함수
    x,y = 1420,745 #복사할 메시지 좌표
    pyautogui.moveTo(x,y)
    pyautogui.doubleClick()    
    pyautogui.hotkey('ctrl', 'c')
    data = clipboard.paste()
    return data

def send_message(c,w): # 메시지를 전송하는 함수
    pyautogui.moveTo(w) #화면 캡쳐한 곳 가운데로 이동
    pyautogui.click() #한번 클릭
    pyautogui.write(c)
    pyautogui.write(['enter'])

while True:
    pyautogui.screenshot('white.png',region =(1345, 740, 377,120)) #보내는 곳
    write = pyautogui.locateCenterOnScreen('white.PNG') # 입력창 사진으로 좌표구하는건데 이것도 그냥 좌표로 바꾸는 게 편할듯??
    data = read_message()
    print(data)
    if data == "!도움말":
        content = "![dlfma]dmf dlqfurgktlaus xmrwlddmf throgoemflqslek."
        send_message(content,write)

    
    pyperclip.copy(' ')
