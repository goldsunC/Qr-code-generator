#   -*- coding:utf-8 -*-
#   @Time   :   2020/ 04 / 10
#   @Author :   goldsunC
#   @Email  :   2428022854@qq.com
#   @Blog   :   https://blog.csdn.net/weixin_45634606
import tkinter as tk
from tkinter import ttk
import win32ui
from MyQR import myqr
lianjielist = []
ditu = None
baocunlujinglist =[]
colors = False
#打开文件夹
def openfile1():
    global ditu
    openfile = win32ui.CreateFileDialog(1)
    openfile.SetOFNInitialDir('D:')
    openfile.DoModal()
    filename = openfile.GetPathName()
    name_entered1.delete(0,23)
    name_entered1.insert(0,filename)
    ditu = filename
def openfile2():
    openfile = win32ui.CreateFileDialog(0)
    openfile.SetOFNInitialDir('D:')
    openfile.DoModal()
    filename = openfile.GetPathName()
    name_entered2.insert(0, filename)
    baocunlujinglist.append(filename)
def queren():
    button0.configure(text = '已确认')
    lianjielist.append(name.get())
def shengcheng():
    words = lianjielist[0]
    version = int(number1.get())
    level = number_chosen.get()
    picture = ditu
    colorized = colors
    contrast = float(name3.get())
    brightness = float(name4.get())
    end = baocunlujinglist[0]
    endlist = end.split('\\')
    s = '\\'.join(endlist[0:-1])
    t = endlist[-1]
    save_name = t+number2.get()
    if s[-1] == ':':
        s = s+'\\'
        save_dir = s
    else:
        save_dir = s
    myqr.run(words=words,version=version,level=level,picture=picture,colorized=colorized,
             contrast=contrast,brightness=brightness,save_name=save_name,save_dir=save_dir)
    #button3.configure(text = '任务执行完毕,请退出')
    window.destroy()
#创建一个窗口
window = tk.Tk()
sw = window.winfo_screenwidth()
sh = window.winfo_screenheight()
ww = 500
wh = 308
x = (sw - ww) / 2
y = (sh - wh) / 2
window.geometry('%dx%d+%d+%d' % (ww, wh, x, y))
#增加标题
window.title('Make by goldsun')
#添加分格
tabControl = ttk.Notebook(window)
tab1 = ttk.Frame(tabControl)
tabControl.add(tab1,text = '制作二维码')
tab2 = ttk.Frame(tabControl)
tabControl.add(tab2,text = '文字识别')
tabControl.pack(expand = 1,fill = 'both')
#小框架
intro = ttk.Labelframe(tab1,text = 'Hello! Just do it now !')
intro.grid(column =0,row = 0,padx = 8,pady = 4)
intro1 = ttk.Labelframe(tab2,text = '不好意思，此处功能尚待完善！')
intro1.grid(column = 0,row = 0,padx = 8,pady = 4)
a_label1 = ttk.Label(intro1, text="                    ")
a_label1.grid(column=0, row=0, sticky='W')
#第一行
a_label = ttk.Label(intro, text="   输入链接:")
a_label.grid(column=0, row=0, sticky='W')
button0 = ttk.Button(intro,text = '确认',command = queren)
button0.grid(column = 2,row =0)
#链接方框
name = tk.StringVar()
name_entered = ttk.Entry(intro,width=40, textvariable=name)
name_entered.grid(column=1, row=0, sticky='W')
#底色选择
color = ['黑白底图','彩色底图']
def radCall():
    global colors
    radSel = radVar.get()
    if radSel == 0:
        colors = False
    elif radSel == 1:
        colors = True
radVar = tk.IntVar()
radVar.set(99)
for i in range(2):
    curRad = tk.Radiobutton(intro,text = color[i],variable = radVar,
                            value = i,command = radCall)
    curRad.grid(column = i,row = 2,sticky = tk.W)
#选择底图
a_label1 = ttk.Label(intro, text="   选择底图：")
a_label1.grid(column=0, row=1, sticky='W')
name1 = tk.StringVar()
name_entered1 = ttk.Entry(intro, width=40, textvariable=name1)
name_entered1.grid(column=1, row=1, sticky='W')
name_entered1.insert(0,'默认空值，可以不选(如果不选，请不要随意改动)')
button1 = ttk.Button(intro,text = '浏览',command = openfile1)
button1.grid(column = 2,row =1)
#保存路径
a_label2 = ttk.Label(intro, text="   保存路径：")
a_label2.grid(column=0, row=8, sticky='W')
name2 = tk.StringVar()
name_entered2 = ttk.Entry(intro, width=40, textvariable=name2)
name_entered2.grid(column=1, row=8, sticky='W')
button2 = ttk.Button(intro,text = '浏览',command = openfile2)
button2.grid(column = 2,row =8)
#纠错水平
ttk.Label(intro,text = '纠错水平：').grid(column = 0,row = 3)
number = tk.StringVar()
number_chosen = ttk.Combobox(intro,width = 10,textvariable = number,state='readonly')
number_chosen['values'] = ('L','M','Q','H')
number_chosen.grid(column = 0,row = 4)
number_chosen.current(0)
#version
ttk.Label(intro,text = 'Version：').grid(column = 1,row = 3)
number1 = tk.StringVar()
number_chosen1 = ttk.Combobox(intro,width =10,textvariable = number1,state='readonly')
number_chosen1['values'] = tuple(range(1,41))
number_chosen1.grid(column = 1,row = 4)
number_chosen1.current(0)
#输出文件后缀
ttk.Label(intro,text = '输出文件后缀：').grid(column = 2,row = 3)
number2 = tk.StringVar()
number_chosen2 = ttk.Combobox(intro,width =10,textvariable = number2,state='readonly')
number_chosen2['values'] = ('.png','.jpg','.bmp','.gif')
number_chosen2.grid(column = 2,row = 4)
number_chosen2.current(0)
#对比度
ttk.Label(intro,text = '对比度：').grid(column = 0,row = 5)
name3 = tk.StringVar()
name_entered3 = ttk.Entry(intro, width=10, textvariable=name3)
name_entered3.grid(column=1, row=5, sticky='W')
name_entered3.insert(0,'1.0')
#亮度
ttk.Label(intro,text = '亮度：').grid(column = 0,row = 7)
name4 = tk.StringVar()
name_entered4 = ttk.Entry(intro, width=10, textvariable=name4)
name_entered4.grid(column=1, row=7, sticky='W')
name_entered4.insert(0,'1.0')
#生成
button3 = ttk.Button(intro,text = '生成',command =shengcheng)
button3.grid(column = 1,row =9)
#惊喜
def surp():
    surprise.configure(text = "哈哈哈这个按钮其实可以设计一下用来触发表白事件的程序，不过我没有做哈哈哈")
surprise = tk.Button(window,text="点击此处有惊喜!",padx = 150,pady = 3,command = surp)
surprise.pack()
window.mainloop()
