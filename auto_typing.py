import pyautogui
import time

def run_taja():
    # Win + R (Open Run dialog)
    pyautogui.hotkey('win', 'r')

    # Wait for the Run dialog to appear
    time.sleep(0.5)

    # Enter URL
    url = "https://tt.hancomtaja.com/ko?pr=LW"
    pyautogui.write(url, interval=0.05)

    # Press Enter to launch the default browser
    pyautogui.press('enter')
    time.sleep(6)

def press_typing():
    text = [
        "dornrrk 1wjf",
        "ehdgoanfrhk qorentksdl",
        "akfmrh ekfgehfhr",
        "gksmsladl qhdngktk",
        "dnflskfk akstp",
        "anrndghk tkacjsfl",
        "ghkfu rkdtks",
        "eogks tkfka eogksdmfh",
        "rlfdl qhwjsgktp"
    ]

    for line in text:
        pyautogui.write(line, interval=0.1)
        pyautogui.press("space")

if __name__ == "__main__":
    run_taja()
    press_typing()


def run_notepad():
    # Win + R (Open Run dialog)
    pyautogui.hotkey('win', 'r')

    # Wait for the Run dialog to appear
    time.sleep(0.5)

    # Enter notepad command
    pyautogui.write("notepad", interval=0.05)

    # Press Enter to launch Notepad
    pyautogui.press('enter')
    time.sleep(1)
