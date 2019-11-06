#!/usr/bin/python

import numpy as np
import cv2
import pyscreenshot as ImageGrab
import time
import random
import pyautogui

def main():
    # load templates on, transform it to gray color
    react = ['like.png', 'liked.png', 'loved.png', 'haha.png', 'wow.png', 'sad.png', 'angry.png']
    reactions_haha = ['haha1.png', 'haha2.png', 'haha3.png', 'haha4.png']
    reactions_like = ['like1.png', 'like2.png']
    reactions_love = ['love1.png', 'love2.png', 'love3.png']
    reactions_sad = ['sad1.png', 'sad2.png', 'sad3.png', 'sad4.png', 'sad5.png']
    reactions_wow = ['wow1.png', 'wow2.png', 'wow3.png', 'wow4.png', 'wow5.png']

    gray_tempplates = []
    for i in react:
        str = '/home/baotd/project fb_auto_like/template/'
        str += i
        templates = cv2.imread(str, cv2.IMREAD_COLOR)
        gray_tempplates.append(cv2.cvtColor(templates, cv2.COLOR_BGR2GRAY))

    gray_reactions_haha = []
    for i in reactions_haha:
        str = '/home/baotd/project fb_auto_like/template/'
        str += i
        reaction = cv2.imread(str, cv2.IMREAD_COLOR)
        gray_reactions_haha.append(cv2.cvtColor(reaction, cv2.COLOR_BGR2GRAY))

    gray_reactions_like = []
    for i in reactions_like:
        str = '/home/baotd/project fb_auto_like/template/'
        str += i
        reaction = cv2.imread(str, cv2.IMREAD_COLOR)
        gray_reactions_like.append(cv2.cvtColor(reaction, cv2.COLOR_BGR2GRAY))

    gray_reactions_love = []
    for i in reactions_love:
        str = '/home/baotd/project fb_auto_like/template/'
        str += i
        reaction = cv2.imread(str, cv2.IMREAD_COLOR)
        gray_reactions_love.append(cv2.cvtColor(reaction, cv2.COLOR_BGR2GRAY))

    gray_reactions_sad = []
    for i in reactions_sad:
        str = '/home/baotd/project fb_auto_like/template/'
        str += i
        reaction = cv2.imread(str, cv2.IMREAD_COLOR)
        gray_reactions_sad.append(cv2.cvtColor(reaction, cv2.COLOR_BGR2GRAY))

    gray_reactions_wow = []
    for i in reactions_wow:
        str = '/home/baotd/project fb_auto_like/template/'
        str += i
        reaction = cv2.imread(str, cv2.IMREAD_COLOR)
        gray_reactions_wow.append(cv2.cvtColor(reaction, cv2.COLOR_BGR2GRAY))

    threshold = 0.8
    font = cv2.FONT_HERSHEY_COMPLEX
    ran = None
    seconds = time.time()

    # main job
    while(True):
        # screen screen recording
        print_screen =  np.array(ImageGrab.grab(bbox=(65,175,760,550)))
        screen_record = cv2.cvtColor(print_screen, cv2.COLOR_BGR2RGB)
        gray_screen_record = cv2.cvtColor(screen_record, cv2.COLOR_BGR2GRAY)
        react_gray_tempplate_index = 0
        # find and highlight the reacted status by comparing templates with frame in video
        # find the reacted symbol under the status
        for gray_tempplate in gray_tempplates:
            w, h = gray_tempplate.shape[::-1]
            res = cv2.matchTemplate(gray_screen_record, gray_tempplate, cv2.TM_CCOEFF_NORMED)
            loc = np.where( res >= threshold)
            for i in zip(*loc[::-1]):
                cv2.rectangle(screen_record, i, (i[0] + w, i[1] + h), (0,255,0), 2)
                cv2.line(screen_record, (i[0] + w, i[1]), (i[0] + w + 30, i[1] - 15),(0,255,0), 2)
                cv2.line(screen_record, (i[0] + w + 30, i[1] - 15), (i[0] + w + 50, i[1] - 15), (0,255,0), 2)
                # highlight the unlike status
                if react_gray_tempplate_index == 0:
                    cv2.line(screen_record, (i[0] + w + 30, i[1] - 15), (i[0] + w + 90, i[1] - 15), (0,255,0), 2)
                    cv2.putText(screen_record, "chua like", (i[0] + w + 30, i[1] - 24), font, 0.65, (255,51,255), 1, cv2.LINE_AA)
                    pyautogui.moveTo(i[0] + w +20, i[1] + h +165, 0.5)
                    time.sleep(0.5)
                    print ("See unlike button")
                    ran = random.randint(1, 5)
                    break
                else:
                    # highlight the liked status
                    if react_gray_tempplate_index == 1:
                        cv2.line(screen_record, (i[0] + w + 30, i[1] - 15), (i[0] + w + 90, i[1] - 15), (0,255,0), 2)
                        cv2.putText(screen_record, 'like roi', (i[0] + w + 30, i[1] - 24), font, 0.65, (255,51,255), 1, cv2.LINE_AA)
                    else:
                        # highlight the loved or heart status
                        if react_gray_tempplate_index == 2:
                            cv2.line(screen_record, (i[0] + w + 30, i[1] - 15), (i[0] + w + 90, i[1] - 15), (0,255,0), 2)
                            cv2.putText(screen_record, 'da tha tim', (i[0] + w + 30, i[1] - 24), font, 0.65, (255,51,255), 1, cv2.LINE_AA)
                        else:
                            # highlight the funny status
                            if react_gray_tempplate_index == 3:
                                cv2.line(screen_record, (i[0] + w + 30, i[1] - 15), (i[0] + w + 90, i[1] - 15), (0,255,0), 2)
                                cv2.putText(screen_record, 'tha haha', (i[0] + w + 30, i[1] - 24), font, 0.65, (255,51,255), 1, cv2.LINE_AA)
                            else:
                                # highlight the surprise status
                                if react_gray_tempplate_index == 4:
                                    cv2.line(screen_record, (i[0] + w + 30, i[1] - 15), (i[0] + w + 90, i[1] - 15), (0,255,0), 2)
                                    cv2.putText(screen_record, 'ngac nhien chua', (i[0] + w + 30, i[1] - 24), font, 0.65, (255,51,255), 1, cv2.LINE_AA)
                                else:
                                    # highlight the sad status
                                    if react_gray_tempplate_index == 5:
                                        cv2.line(screen_record, (i[0] + w + 30, i[1] - 15), (i[0] + w + 90, i[1] - 15), (0,255,0), 2)
                                        cv2.putText(screen_record, 'buon ghe', (i[0] + w + 30, i[1] - 24), font, 0.65, (255,51,255), 1, cv2.LINE_AA)
                                    else:
                                        # highlight the status that makes people angry
                                        if react_gray_tempplate_index == 6:
                                            cv2.line(screen_record, (i[0] + w + 30, i[1] - 15), (i[0] + w + 90, i[1] - 15), (0,255,0), 2)
                                            cv2.putText(screen_record, 'tuc qua ma', (i[0] + w + 30, i[1] - 24), font, 0.65, (255,51,255), 1, cv2.LINE_AA)
            react_gray_tempplate_index += 1
        cv2.imshow('React status', screen_record)
        # find and highlight the reaction by comparing templates with frame in video
        print_screen =  np.array(ImageGrab.grab(bbox=(65,175,760,550)))
        screen_record = cv2.cvtColor(print_screen, cv2.COLOR_BGR2RGB)
        gray_screen_record = cv2.cvtColor(screen_record, cv2.COLOR_BGR2GRAY)
        # find the reaction
        # highlight the haha reaction
        # Move mouse pointer
        if ran == 1:
            for gray_reaction_haha in gray_reactions_haha:
                w, h = gray_reaction_haha.shape[::-1]
                res = cv2.matchTemplate(gray_screen_record, gray_reaction_haha, cv2.TM_CCOEFF_NORMED)
                loc = np.where( res >= threshold)
                for i in zip(*loc[::-1]):
                    cv2.rectangle(screen_record, i, (i[0] + w, i[1] + h), (0,255,0), 2)
                    cv2.line(screen_record, (i[0] + w, i[1]), (i[0] + w + 30, i[1] - 15),(0,255,0), 2)
                    cv2.line(screen_record, (i[0] + w + 30, i[1] - 15), (i[0] + w + 50, i[1] - 15), (0,255,0), 2)
                    pyautogui.moveTo(i[0] + w +40, i[1] + h +160, 0.5)
                    time.sleep(0.5)
                    pyautogui.click()
                    print ("click haha")
                    break
        else:
            # find the reaction
            # highlight the like reaction
            # Move mouse pointer
            if ran == 2:
                for gray_reaction_like in gray_reactions_like:
                    w, h = gray_reaction_like.shape[::-1]
                    res = cv2.matchTemplate(gray_screen_record, gray_reaction_like, cv2.TM_CCOEFF_NORMED)
                    loc = np.where( res >= threshold)
                    for i in zip(*loc[::-1]):
                        cv2.rectangle(screen_record, i, (i[0] + w, i[1] + h), (0,255,0), 2)
                        cv2.line(screen_record, (i[0] + w, i[1]), (i[0] + w + 30, i[1] - 15),(0,255,0), 2)
                        cv2.line(screen_record, (i[0] + w + 30, i[1] - 15), (i[0] + w + 50, i[1] - 15), (0,255,0), 2)
                        pyautogui.moveTo(i[0] + w +40, i[1] + h +160, 0.5)
                        time.sleep(0.5)
                        pyautogui.click()
                        print ("click like")
                        break
            else:
                # find the reaction
                # highlight the love reaction
                # Move mouse pointer
                if ran == 3:
                    for gray_reaction_love in gray_reactions_love:
                        w, h = gray_reaction_love.shape[::-1]
                        res = cv2.matchTemplate(gray_screen_record, gray_reaction_love, cv2.TM_CCOEFF_NORMED)
                        loc = np.where( res >= threshold)
                        for i in zip(*loc[::-1]):
                            cv2.rectangle(screen_record, i, (i[0] + w, i[1] + h), (0,255,0), 2)
                            cv2.line(screen_record, (i[0] + w, i[1]), (i[0] + w + 30, i[1] - 15),(0,255,0), 2)
                            cv2.line(screen_record, (i[0] + w + 30, i[1] - 15), (i[0] + w + 50, i[1] - 15), (0,255,0), 2)
                            pyautogui.moveTo(i[0] + w +40, i[1] + h +160, 0.5)
                            time.sleep(0.5)
                            pyautogui.click()
                            print ("click love")
                            break
                else:
                    # find the reaction
                    # highlight the sad reaction
                    # Move mouse pointer
                    if ran == 4:
                        for gray_reaction_sad in gray_reactions_sad:
                            w, h = gray_reaction_sad.shape[::-1]
                            res = cv2.matchTemplate(gray_screen_record, gray_reaction_sad, cv2.TM_CCOEFF_NORMED)
                            loc = np.where( res >= threshold)
                            for i in zip(*loc[::-1]):
                                cv2.rectangle(screen_record, i, (i[0] + w, i[1] + h), (0,255,0), 2)
                                cv2.line(screen_record, (i[0] + w, i[1]), (i[0] + w + 30, i[1] - 15),(0,255,0), 2)
                                cv2.line(screen_record, (i[0] + w + 30, i[1] - 15), (i[0] + w + 50, i[1] - 15), (0,255,0), 2)
                                pyautogui.moveTo(i[0] + w +40, i[1] + h +160, 0.5)
                                time.sleep(0.5)
                                pyautogui.click()
                                print ("click sad")
                                break
                    else:
                        # find the reaction
                        # highlight the wow reaction
                        # Move mouse pointer
                        if ran == 5:
                            for gray_reaction_wow in gray_reactions_wow:
                                w, h = gray_reaction_wow.shape[::-1]
                                res = cv2.matchTemplate(gray_screen_record, gray_reaction_wow, cv2.TM_CCOEFF_NORMED)
                                loc = np.where( res >= threshold)
                                for i in zip(*loc[::-1]):
                                    cv2.rectangle(screen_record, i, (i[0] + w, i[1] + h), (0,255,0), 2)
                                    cv2.line(screen_record, (i[0] + w, i[1]), (i[0] + w + 30, i[1] - 15),(0,255,0), 2)
                                    cv2.line(screen_record, (i[0] + w + 30, i[1] - 15), (i[0] + w + 50, i[1] - 15), (0,255,0), 2)
                                    pyautogui.moveTo(i[0] + w +40, i[1] + h +160, 0.5)
                                    time.sleep(0.5)
                                    pyautogui.click()
                                    print ("click wow")
                                    break
        cv2.imshow('Chosing react button', screen_record)
        # Auto scroll and random mouse pointer position to act like a human
        if time.time() - seconds > 5:
            seconds = time.time()
            pyautogui.scroll(-2)
            X = random.randint(565, 745)
            Y = random.randint(265, 755)
            pyautogui.moveTo(X, Y, 0.5)

        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

if __name__ == '__main__':
    print ("Begin in 3 ...")
    time.sleep(1)
    print ("Begin in 2 ...")
    time.sleep(1)
    print ("Begin in 1 ...")
    time.sleep(1)
    print ("GO")
    main()
