import tkinter as tk
import time

top_frame_size = 300
app_width = '1080'
app_height = '680'

app = tk.Tk()
app.geometry(app_width+'x'+app_height)
app.resizable(True,True)

labels = ['序号','时间','容量','开盘价','最高价','最低价','收盘价','涨跌额','涨跌幅','换手率','成交量（手）','成交额(亿)']
frames = []
def updateLabel(self,Label,btn):
    Label['text'] = 'click!'
    btn['state'] =tk.DISABLED
    time.sleep(2)

def InitFrames(topFrame):
    for i in range(len(labels)):
        frame = tk.Frame(topFrame,bg='green',width=int(app_width)/len(labels))
        frame.pack(side=tk.LEFT,fill=tk.BOTH,expand=True)
        label = tk.Label(frame,fg='black',text=labels[i],bd=2,relief='solid',bg='blue')
        label.pack(side=tk.TOP,fill=tk.X,expand=True)

        frames.append(frame)

def InitNO():
    frame = frames[0]
    for i in range(30):
        label = tk.Label(frame,text=str(i))
        label.pack()


topFrame = tk.Frame(app,background='grey',height=top_frame_size,bg='#a11000000')
topFrame.pack(fill=tk.BOTH,side=tk.TOP)

InitFrames(topFrame)
InitNO()
app.mainloop()





