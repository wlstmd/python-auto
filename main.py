import pyautogui
import time

# 나의 모니터 화면 크기 출력
print(pyautogui.size())

# 마우스 위치 출력
time.sleep(2)
print(pyautogui.position())

# 마우스 이동
pyautogui.moveTo(1256, 57)

# 마우스 이동 + 천천히 이동
pyautogui.moveTo(600, 57, 0.5)

# # 마우스 클릭
pyautogui.click()

# 마우스 오른쪽 클릭
pyautogui.click(button='right')

# 마우스 더블 클릭
pyautogui.doubleClick()

# 마우스 더블 클릭 + 시간 지정
pyautogui.click(clicks=3, interval=1)  # 3번클릭 + 1초마다 클릭

# 마우스 드래그
pyautogui.moveTo(683, 99, 2)
pyautogui.dragTo(557, 97, 2, button='left')

# 마우스 정보 알아 내기
pyautogui.mouseInfo()