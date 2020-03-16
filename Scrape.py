import pyautogui
import time
import pyperclip
import os

offenderBlock_X = 526
offenderBlock_Y = [320,385,445,528,580,648,705,550,608,670]

page_X = [426,432,439,447,452,461,468,475,482,491,514]


def testpoint():

    time.sleep(3)
    print(pyautogui.position())

    return
def scroll():
    pyautogui.scroll(-10)

    return



def swapPage(page):
    y = 280

    pyautogui.moveTo(page,280)
    pyautogui.click()
    time.sleep(9)


    return


def Scrape():

    for j in range(len(page_X)):
        swapPage(page_X[j])
        for i in range(len(offenderBlock_Y)):
            time.sleep(3)
            if i > 6:
                scroll()
                time.sleep(3)
            pyautogui.moveTo(offenderBlock_X,offenderBlock_Y[i])
            time.sleep(3)
            DownloadOffender()


    return

def parseText(text):



    fw = open("tempfile.txt","w+")

    fw.write(text)

    fw.close()

    with open("tempfile.txt","r")as f:
        content = f.readlines()
        file_name =""

        level = 11
        fname = 15
        mname = 16
        lname = 17
        #everything is 1 off because file lines dont start at 0


        for i,line in enumerate(content):
            try:
                if i == 9 and line.split()[0] == 'Yes':
                    print(line)
                    level = level+1
                    fname = fname+1
                    mname = mname+1
                    lname = lname+1


                elif i == level:
                    #print(level)
                    #print(line.strip().split())
                    file_name = file_name + line.strip().split()[2] +"-"

                elif i == fname:
                    #print(fname)
                    #print(line.strip().split())

                    file_name = file_name + line.strip().split()[2] +"-"

                elif i == mname:
                    #print(mname)
                    #print(line.strip().split())

                    file_name = file_name + line.strip().split()[2] +"-"

                elif i ==lname:
                    #print(lname)
                    #print(line.strip().split())

                    file_name = file_name + line.strip().split()[2] +"-"
            except IndexError:
                pass
    f.close()

    return file_name








def DownloadOffender():
    pyautogui.click()
    time.sleep(15)#Based on network speed changed this

    pyautogui.hotkey('ctrl','a')

    pyautogui.hotkey('ctrl','c')

    a = pyperclip.paste()

    file_name = parseText(a)

    pyautogui.moveTo(502, 315)
    pyautogui.rightClick()
    time.sleep(.5)
    pyautogui.moveTo(551, 362)
    pyautogui.click()
    time.sleep(2)
    pyautogui.hotkey('ctrl', 'a')
    pyautogui.press('backspace')
    pyperclip.copy(file_name + ".png")#place holder is here
    pyautogui.hotkey('ctrl', 'v')
    time.sleep(.5)
    pyautogui.press('enter')

    time.sleep(.5)

    #pyautogui.hotkey('alt','left')
    pyautogui.moveTo(516,267)
    pyautogui.click()
    time.sleep(15)#Based on network speed changed this
    return

time.sleep(3)
#Scrape()
#DownloadOffender()
#testpoint()
while(True):
    Scrape()