import pyautogui
import subprocess
import time
import math

def execute_mspaint():
    print("Execute mspaint - Launching Paint...")
    subprocess.Popen('mspaint.exe')    
    # Wait sufficiently for Paint to open and become active
    time.sleep(2)
    # Maximize the Paint window
    pyautogui.keyDown('alt')
    pyautogui.press(' ')
    pyautogui.press('x')
    pyautogui.keyUp('alt')
    time.sleep(1)

def draw_heart():    
    # Set the starting position for drawing (near the center of the screen)
    screen_width, screen_height = pyautogui.size()
    center_x = screen_width // 2
    center_y = screen_height // 2 - 50

    # Heart drawing algorithm (Parametric Equation of a Heart)
    scale = 10 # Scale factor to enlarge the heart shape

    print("Starting to draw the heart. Please do not move the mouse!")
    # Move to the first coordinate (start drawing)
    first_step = True
    
    # Calculate coordinates by changing t from 0 to 2*pi
    for t in [i * 0.1 for i in range(0, 63)]:
        # Heart shape mathematical formula
        x = 16 * math.sin(t)**3
        y = -(13 * math.cos(t) - 5 * math.cos(2*t) - 2 * math.cos(3*t) - math.cos(4*t))
        
        # Convert to actual screen coordinates
        target_x = center_x + x * scale
        target_y = center_y + y * scale
        
        if first_step:
            pyautogui.moveTo(target_x, target_y)
            pyautogui.mouseDown() # Press left mouse button
            first_step = False
        else:
            # Set duration to draw the heart slowly
            pyautogui.dragTo(target_x, target_y, duration=0.02)

    pyautogui.mouseUp() # Finish drawing


def draw_filled_heart():   
    origin_x, origin_y = pyautogui.position()
    origin_y += 120
    scale = 90         # Size adjustment
    k = 100            # Density (maximum value among 0~100 mentioned by the user)
    step = 0.01        # Precision (smaller is smoother)
    
    first_move = True
    
    # Repeat x range from -sqrt(3) to sqrt(3)
    x_val = -math.sqrt(3)
    while x_val <= math.sqrt(3):
        # y = x^(2/3) + 0.9 * sin(kx) * sqrt(3-x^2)
        term1 = pow(abs(x_val), 2/3)
        term2 = 0.9 * math.sin(k * x_val) * math.sqrt(3 - x_val**2)
        y_val = -(term1 + term2) 
        
        draw_x = origin_x + (x_val * scale)
        draw_y = origin_y + (y_val * scale)

        if first_move:
            pyautogui.moveTo(draw_x, draw_y)
            pyautogui.mouseDown()
            first_move = False
        else:
            pyautogui.dragTo(draw_x, draw_y, duration=0)
        
        x_val += step

    pyautogui.mouseUp()
    print("Heart drawing completed!")


if __name__ == "__main__":
    try:
        execute_mspaint()
        draw_heart()
        draw_filled_heart()
    except Exception as e:
        print(f"Error occurred: {e}")