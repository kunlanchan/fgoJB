import pyautogui
import win32gui
import random
import time
import cv2
# from goto import with_goto

def get_windows_info():  # 获取窗口信息
    mnq = u'雷电模拟器'
    handle = win32gui.FindWindow(0, mnq)
    win32gui.SetForegroundWindow(handle)  # 窗口前置激活
    if handle == 0:
        return None
    else:
        return win32gui.GetWindowRect(handle)  # 窗口坐标位置

def find_pic(pic:str):    # 找到图片并点击
    tp = cv2.imread(pic)
    cz = pyautogui.locateCenterOnScreen(tp, confidence=0.9)
    while cz == None:
        cz = pyautogui.locateCenterOnScreen(tp, confidence=0.9)
    time.sleep(1)  # #找图后加载下一动作
    pyautogui.click(cz[0], cz[1])
    time.sleep(1)

'''
#开始任务
ks = pyautogui.locateCenterOnScreen('D:\\fgoJB\\JB\\sc\\zd\\ksrw.png',confidence=0.9,grayscale=True) #点击开始战斗
while ks == None:
    ks = pyautogui.locateCenterOnScreen('D:\\fgoJB\\JB\\sc\\zd\\ksrw.png', confidence=0.9, grayscale=True)  # 点击开始战斗
    time.sleep(1)
    print('开始任务未找到')
time.sleep(3)
pyautogui.doubleClick(ks[0] + sj, ks[1] + sj)
'''

def CD():#C呆技能给一号位置打手
    cd_1 = find_pic('D:\\fgoJB\\JB\\sc\\zd\\CD1.png')  # c呆1技能
    time.sleep(0.3)
    pyautogui.doubleClick(780 + sj, 630 + sj)  # 空点
    cd_2 = find_pic('D:\\fgoJB\\JB\\sc\\zd\\CD2.png')  # c呆2技能
    pyautogui.doubleClick(530 + sj, 640 + sj)  # 选择一号人物
    time.sleep(0.3)
    pyautogui.doubleClick(780 + sj, 630 + sj)  # 空点
    time.sleep(1)
    cd_3 = find_pic('D:\\fgoJB\\JB\\sc\\zd\\CD3.png')  # c呆3技能
    pyautogui.doubleClick(530 + sj, 640 + sj)  #  选择一号人物
    time.sleep(0.3)
    pyautogui.doubleClick(780 + sj, 630 + sj)  # 空点
    time.sleep(1)

'''
#请选择对象
ds = pyautogui.locateCenterOnScreen('D:\\fgoJB\\JB\\sc\\zd\\dashou.png',confidence=0.9,grayscale=True) #c呆二技能
while ds == None:
    ds = pyautogui.locateCenterOnScreen('D:\\fgoJB\\JB\\sc\\zd\\dashou.png', confidence=0.9, grayscale=True)  #c呆二技能
    time.sleep(1)
    print('打手位置未找到')
pyautogui.doubleClick(535 + sj, 666 + sj)
'''


'''           参                            数               '''
sj = random.randint(1, 50)  # 随机点击范围
sj_1 = random.randint(1, 10)

'''           窗                            口               '''

hy = get_windows_info()  # 激活窗口
time.sleep(1)  # print(hy)  (87, 0, 1870, 1020)

lz = pyautogui.locateCenterOnScreen('D:\\fgoJB\\JB\\sc\\zd\\lz.png', confidence=0.9)
while lz == None:
    lz = pyautogui.locateCenterOnScreen('D:\\fgoJB\\JB\\sc\\zd\\lz.png', confidence=0.9)
    '''           第             一              面               '''

    CD()
    JT_1 = find_pic('D:\\fgoJB\\JB\\sc\\zd\\CD1.png')  # 酒吞3技能
    pyautogui.doubleClick(780 + sj, 630 + sj)  # 空点
    time.sleep(1)
    # 攻击
    gj_1 = find_pic('D:\\fgoJB\\JB\\sc\\zd\\gj.png')
    # 选卡
    xk = pyautogui.locateCenterOnScreen('D:\\fgoJB\\JB\\sc\\zd\\xkfh.png', confidence=0.9, grayscale=True)  # 攻击
    while xk == None:
        xk = pyautogui.locateCenterOnScreen('D:\\fgoJB\\JB\\sc\\zd\\xkfh.png', confidence=0.9, grayscale=True)  # 攻击
        time.sleep(1)
        print('攻击位置未被点击')
    time.sleep(1)  # 防止刚加载进入时的点击无效化
    pyautogui.click(620 + sj, 310 + sj)  # 一号宝具位置
    time.sleep(1)
    pyautogui.click(270 + sj, 830 + sj)  # 一号卡位置
    time.sleep(1)
    pyautogui.click(620 + sj, 720 + sj)  # 二号卡位置

    '''           第             二              面               '''

    cg_2 = find_pic('D:\\fgoJB\\JB\\sc\\zd\\CG2.png')  # 陈宫2技能
    pyautogui.doubleClick(780 + sj, 630 + sj)  # 空点
    cg_3 = find_pic('D:\\fgoJB\\JB\\sc\\zd\\CG3.png')  # 陈宫3技能
    pyautogui.doubleClick(1370 + sj, 640 + sj)  # 选择3号人物
    time.sleep(0.3)
    pyautogui.doubleClick(780 + sj, 630 + sj)  # 空点
    time.sleep(1)
    CD()
    jt_2 = find_pic('D:\\fgoJB\\JB\\sc\\zd\\JT2.png')  # 酒吞童子2技能
    pyautogui.doubleClick(780 + sj, 630 + sj)  # 空点
    # 二面攻击
    gj_2 = find_pic('D:\\fgoJB\\JB\\sc\\zd\\gj.png')
    # 二面选卡
    xk = pyautogui.locateCenterOnScreen('D:\\fgoJB\\JB\\sc\\zd\\xkfh.png', confidence=0.9, grayscale=True)  # 攻击
    while xk == None:
        xk = pyautogui.locateCenterOnScreen('D:\\fgoJB\\JB\\sc\\zd\\xkfh.png', confidence=0.9, grayscale=True)  # 攻击
        time.sleep(1)
        print('攻击位置未被点击')
    time.sleep(1)  # 防止刚加载进入时的点击无效化
    pyautogui.click(1270 + sj, 310 + sj)  # 三号宝具位置
    time.sleep(1)
    pyautogui.click(270 + sj, 830 + sj)  # 一号卡位置
    time.sleep(1)
    pyautogui.click(620 + sj, 720 + sj)  # 二号卡位置

    '''           第             三              面               '''

    yzjn = find_pic('D:\\fgoJB\\JB\\sc\\zd\\yzjn.png')
    lmf = find_pic('D:\\fgoJB\\JB\\sc\\zd\\YZ1.png')  # 御主1技能
    pyautogui.doubleClick(530 + sj, 640 + sj)  # 选择一号人物
    time.sleep(0.3)
    pyautogui.doubleClick(780 + sj, 630 + sj)  # 空点
    time.sleep(0.7)
    yzjn_1 = find_pic('D:\\fgoJB\\JB\\sc\\zd\\yzjn.png')
    nx = find_pic('D:\\fgoJB\\JB\\sc\\zd\\NX.png')  # 御主3技能
    pyautogui.doubleClick(530 + sj, 640 + sj)  # 选择一号人物
    time.sleep(0.3)
    pyautogui.doubleClick(780 + sj, 630 + sj)  # 空点
    time.sleep(0.7)
    # 三面攻击
    gj_3 = find_pic('D:\\fgoJB\\JB\\sc\\zd\\gj.png')
    # 三面选卡
    xk = pyautogui.locateCenterOnScreen('D:\\fgoJB\\JB\\sc\\zd\\xkfh.png', confidence=0.9, grayscale=True)  # 攻击
    while xk == None:
        xk = pyautogui.locateCenterOnScreen('D:\\fgoJB\\JB\\sc\\zd\\xkfh.png', confidence=0.9, grayscale=True)  # 攻击
        time.sleep(1)
        print('攻击位置未被点击')
    time.sleep(1)  # 防止刚加载进入时的点击无效化
    pyautogui.click(620 + sj, 310 + sj)  # 一号宝具位置
    time.sleep(1)
    pyautogui.click(270 + sj, 830 + sj)  # 一号卡位置
    time.sleep(1)
    pyautogui.click(620 + sj, 720 + sj)  # 二号卡位置

    '''           结                          算               '''

    jbym = find_pic('D:\\fgoJB\\JB\\sc\\zd\\jbym.png')  # 羁绊结算
    jyzym = find_pic('D:\\fgoJB\\JB\\sc\\zd\\jyzym.png')  # 经验值结算
    zlpxybym = find_pic('D:\\fgoJB\\JB\\sc\\zd\\zlpxybym.png')  # 战利品结算
    lxcjym = find_pic('D:\\fgoJB\\JB\\sc\\zd\\lxcjym.png')  # 连续出击

    xddhfym = pyautogui.locateCenterOnScreen('D:\\fgoJB\\JB\\sc\\zd\\xddhfym.png', confidence=0.9)  # 行动点回复页面
    JPG = pyautogui.locateCenterOnScreen('D:\\fgoJB\\JB\\sc\\zd\\JPG.png', confidence=0.9)  # 行动点回复页面
    # zzym = pyautogui.locateCenterOnScreen('D:\\fgoJB\\JB\\sc\\zd\\.png', confidence=0.9)  # 助战页面

    if xddhfym == None:
        # zzym = pyautogui.locateCenterOnScreen('D:\\fgoJB\\JB\\sc\\zd\\zhuzhan_cyjn.png', confidence=0.9)  # 助战页面
        # if zzym == None:
            # lbgx = find_pic('D:\\fgoJB\\JB\\sc\\zd\\lbgx.png')  #列表更新
            # qdgx = find_pic('D:\\fgoJB\\JB\\sc\\zd\\qdgx.png')  #确定更新
            #
            #
            #


        zz = find_pic('D:\\fgoJB\\JB\\sc\\zd\\zhuzhan_cyjn.png')  # 依据持有技能选择助战
    elif JPG != None:
        JPG = find_pic('D:\\fgoJB\\JB\\sc\\zd\\JPG.png')
        jdsypg = find_pic('D:\\fgoJB\\JB\\sc\\zd\\jdsypg.png')  # 决定使用苹果
        zz = find_pic('D:\\fgoJB\\JB\\sc\\zd\\zhuzhan_cyjn.png')  # 依据持有技能选择助战

    else:
        YPG = find_pic('D:\\fgoJB\\JB\\sc\\zd\\YPG.png')
        jdsypg = find_pic('D:\\fgoJB\\JB\\sc\\zd\\jdsypg.png')  # 决定使用苹果
        zz = find_pic('D:\\fgoJB\\JB\\sc\\zd\\zhuzhan_cyjn.png')  # 依据持有技能选择助战














