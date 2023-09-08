import tkinter
from tkinter import *
import pyautogui
import time
import threading
import random
import psutil   # 실행중인 프로세스 및 시스템 활용 라이브러리


class mouse_Move() :
    def __init__(self) :
        
        self.move = True # 제어 변수
        
        self.window = tkinter.Tk()
        self.window.title('마우스 움직이기')
        self.window.geometry('210x210')
        
        self.btn1 = Button(self.window, text = '마우스 자동 움직이기 실행', command=self.start_task)
        self.btn1.pack(side = TOP , fill = X , ipadx = 10, ipady = 10, padx = 10, pady = 10)
        
        self.btn2 = Button(self.window, text = '마우스 움직임', command=self.changMove , bg = "blue")
        self.btn2.pack(fill = X , ipadx = 10, ipady = 10, padx = 10, pady = 10)
        
        self.btn3 = Button(self.window , text = "프로그램 종료" , command=self.quit)
        self.btn3.pack(fill = X , ipadx = 10, ipady = 10, padx = 10, pady = 10)
        
        self.window.mainloop()
        
    def changMove(self) :
        if self.move :
            self.move = False
        else :
            self.move = True
            
        if self.move :
            self.btn2['text'] = '마우스 움직임'
            self.btn2['bg'] = 'blue'
        else :
            self.btn2['text'] = '마우스 멈춤'
            self.btn2['bg'] = 'red'
            
    def start_task(self) :
        # 작업 스레드 시작
        task_thread = threading.Thread(target = self.long_running_task)
        task_thread.start()
        
    def long_running_task(self) :
        srceenWidth , screenHeight = pyautogui.size()
        print('현재 모니터 사이즈 {0}, {1}'.format(srceenWidth, screenHeight))
        
        pyautogui.moveTo(srceenWidth/2, screenHeight/2)
        self.btn1['text'] = '마우스 자동 움직이기 실행 중 !!!!!!'
        
        while(self.move) :
                                    
            a = random.randint(0,50)
            b = random.randint(0,50)
            
            currentMouseX, currentMouseY = pyautogui.position()
            pyautogui.moveTo(currentMouseX + a, currentMouseY + b , 2, pyautogui.easeInBounce)
            
            
            # 마우스를 다시 중앙으로 이동
            pyautogui.moveTo(srceenWidth/2, screenHeight/2)
            
            if a + b > 80 :
                print('a = {0}, b = {1} 로 합산은 {2} 마우스 클릭'.format(a, b, a+b))
                pyautogui.click()
            
            time.sleep(10)
            
        self.btn1['text'] = '마우스 자동 움직이기 실행 끝 !!'
        
    def quit(self) :
        self.window.destroy()
        for proc in psutil.process_iter():
            try:
                # 프로세스 이름, PID값 가져오기
                processName = proc.name()
                processID = proc.pid
                #print(processName , ' - ', processID)
        
                if processName == "khj_mouse.exe":
                    #print(processName , ' - ', processID)
                    parent_pid = processID  #PID
                    parent = psutil.Process(parent_pid) # PID 찾기
                    for child in parent.children(recursive=True):  #자식-부모 종료
                        child.kill()
                    parent.kill()
        
            except (psutil.NoSuchProcess, psutil.AccessDenied, psutil.ZombieProcess):   #예외처리
                pass
        
        
        
if __name__ == '__main__' :
    app = mouse_Move()