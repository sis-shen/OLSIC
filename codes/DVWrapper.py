import time

import dearpygui.dearpygui as dpg
from SnowBallCrawler import  *

TOP_CHILD_WINDOW = "top_child_win" # 定义默认的子窗口id

def mystampToNumStr(stamp): # 封装一个把毫秒级时间戳转换成年月日的函数
    date = time.strftime("%Y/%m/%d", time.localtime(int(stamp / 1000.0)))
    return date

dpg.create_context()

# 准备一个储存列名称的列表，方便建立表格
columns = ['序号','时间','成交量(手)','开盘价','最高价','最低价','收盘价','涨跌额','涨跌幅','换手率','成交额(亿)']

class Window:

    def __init__(self,label,tag):
        with dpg.stage() as stage: # 创建临时上下文
            self.id = dpg.add_window(label=label,tag=tag) # 在里面创建一个window组件
        self.stage = stage # 储存临时上下文的id

    def add_child(self,child): # 直接添加含有self.id的自定义类为孩子
        dpg.move_item(child.id,parent=self.id)

    def add_childID(self,childID): # 按照id添加孩子
        dpg.move_item(childID,parent=self.id)

    def submit(self): # 将临时上下文合并到主dpg上下文,效果上是让组件可见
        dpg.unstage(self.stage)
class DataTable:
    def __init__(self,tag='main table'):
        with dpg.stage(): # 创建临时上下文
            self.id = dpg.add_table(header_row=True, policy=dpg.mvTable_SizingFixedFit, row_background=True, reorderable=True,
                   resizable=True, no_host_extendX=False, hideable=True,
                   borders_innerV=True, delay_search=True, borders_outerV=True, borders_innerH=True,
                   borders_outerH=True,tag=tag)  # 创建一个会自动伸缩，可修改列宽度的，比较自由的表格

            dpg.push_container_stack(self.id) # 展开表格组件的上下文，下面创建的组件自动成为表格的子组件
            # 添加表格的列
            for i in range(len(columns)):
                dpg.add_table_column(label=columns[i],width_stretch=True, init_width_or_weight=0.0)

            dpg.pop_container_stack() # 关闭表格的上下文


    def clearData(self):
        # 清除列表
        for item in dpg.get_item_children(self.id,1):
            dpg.delete_item(item)
    def updateData(self,items): # 上传数据到表格

        dpg.push_container_stack(self.id) # 打开表格的上下文
        row = 0
        for item in items:
            row+=1
            with dpg.table_row():
                dpg.add_text(str(row)) # 输入行号到行号列
                for j in range(len(item)):
                    if(j == 0): # 时间要转换成时间戳
                        date = mystampToNumStr(item[0])
                        dpg.add_text(date)
                    elif(j==10):
                        break
                    else:
                        dpg.add_text(item[j])

        dpg.pop_container_stack()

class MenuItem():
    def __init__(self,menubar,label,tag,target): # 菜单选项与多个组件有关
        self.parent = menubar.id # 储存parent的id
        self.target = target # 储存目标空间的id
        dpg.push_container_stack(self.parent)  # 将自己添加到parent中
        self.id = dpg.add_menu_item(label=label,tag=tag,user_data=[menubar,self])
        dpg.pop_container_stack()

    def HideCallback(self):
        current_visible = dpg.is_item_visible(self.target)  # 获取当前可见性
        if current_visible:
            dpg.hide_item(self.target) # 若可见，则隐藏
    def setCallback(self,callback): # 设置当菜单选项被点击时调用的回调函数
        dpg.set_item_callback(self.id,callback=callback)
class MenuBar():
    def __init__(self,tag='main menu'):
        self.children = [] # 列表用于管理所有子组件（惨淡选项）
        with dpg.stage():
            self.id = dpg.add_menu_bar(tag=tag)

    def add_item(self,label,tag,target,font): # 设计思想上，菜单选项必须能过管理它对应的目标组件，所以需要一个target成员变量储存目标id
        self.children.append(MenuItem(self,label=label,tag=tag,target=target))
        child_id = self.children[-1].id
        dpg.bind_item_font(child_id,font) # 绑定菜单选项的字体(由外部提供)
        self.children[-1].HideCallback() # 新的孩子默认调用一下使目标隐藏的回调函数
        return child_id # 返回新插入孩子的id,外边外界绑定回调函数

    def hide_children(self):# 提供使所有被控组件隐藏的接口(不是让菜单选项隐藏)
        for child in self.children:
            child.HideCallback() # 规定MenuItem类必须有一个HideCallback回调函数

class Button:
    def __init__(self,label,tag):
        with dpg.stage():
            self.id=dpg.add_button(label=label,tag=tag,width=150,height=40)

    def setcallback(self,callback):
        dpg.set_item_callback(self.id,callback=callback)

class KPlot:
    def __init__(self):
        with dpg.stage():
            # 创建一个plot组件
            with dpg.plot(label="贵州茅台股票日K图",tag='kplot',height=-1,width=-1,show=False) as self.id:
                dpg.add_plot_legend()

    def draw(self,fetch_data):
        xData=[]
        # 这里使用原生字典+列表解析获取到的数据
        yDatas={"volume":[],"open":[],"high":[],"low":[],
                "close":[],"chg":[],"percent":[],
                "turnoverrate":[],"amount":[]}
        for line in fetch_data:
            line = list(line) #将元组转成列表，这样才能执行pop操作

            xData.append(line.pop(0)/1000)
            yDatas["volume"].append(line.pop(0))
            yDatas["open"].append(line.pop(0))
            yDatas["high"].append(line.pop(0))
            yDatas["low"].append(line.pop(0))
            yDatas['close'].append(line.pop(0))
            yDatas['chg'].append(line.pop(0))
            yDatas['percent'].append(line.pop(0))
            yDatas['turnoverrate'].append(line.pop(0))
            yDatas['amount'].append(line.pop(0))

        def custom_tooltip_handler(sender,app_data): #声明一个回调函数，用于在鼠标上悬停显示每天的股票参数
            x_data,y_data=dpg.get_plot_mouse_pos()
            date = mystampToNumStr(x_data*1000)  # 将横坐标时间戳转换成具体日期
            index = 0
            # 通过日期反向寻找下标，然后再通过下标找到当天股票的数据
            while( index < len(xData) and date != mystampToNumStr(xData[index]*1000) ):
                index+=1
            if(index < len(xData)):
                # 通过setValue设置悬停显示的信息
                dpg.set_value("volume tip",f"时间:{date} \n "
                                           f"成交量:{yDatas['volume'][index]}\n"
                                           f"开盘价:{yDatas['open'][index]}\n"
                                           f"最高价:{yDatas['high'][index]}\n"
                                           f"最低价:{yDatas['low'][index]}\n"
                                           f"收盘价:{yDatas['close'][index]}\n"
                                           f"涨跌额:{yDatas['chg'][index]}\n"
                                           f"涨跌幅{yDatas['percent'][index]}\n"
                                           f"换手率:{yDatas['turnoverrate'][index]}\n"
                                           f"成交额:{yDatas['amount'][index]}")

        with dpg.handler_registry(tag="volume hander"):
            # 将鼠标移动事件的回调函数绑定成上面的自定义函数
            dpg.add_mouse_move_handler(callback=custom_tooltip_handler)

        # 准备开始绘制曲线
        dpg.push_container_stack(self.id)
        xaxis = dpg.add_plot_axis(dpg.mvXAxis,label="日期",time=True) # 创建横坐标,并标记为以时间为横坐标
        dpg.add_plot_axis(dpg.mvYAxis,label='开盘价',tag="open") # 创建纵坐标1
        dpg.add_plot_axis(dpg.mvYAxis,label='换手率',tag="turnoverrate") # 创建纵坐标2
        dpg.add_plot_axis(dpg.mvYAxis,label='交易额',tag="amount") # 创建纵坐标3


        dpg.add_line_series(xData,yDatas["volume"],parent="amount",label="成交量") # 绘制折线图
        # 绘制K图
        s1id = dpg.add_candle_series(xData,opens=yDatas['open'],closes=yDatas['close'],lows=yDatas['low'],highs=yDatas['high'],parent='open',label='K图',time_unit=dpg.mvTimeUnit_Day)
        dpg.add_line_series(xData,yDatas["open"],parent='open',label="开盘价") # 绘制折线图，下同
        dpg.add_line_series(xData,yDatas["high"],parent='open',label="最高价")
        dpg.add_line_series(xData,yDatas["low"],parent='open',label='最低价')
        dpg.add_line_series(xData,yDatas["close"],parent='open',label='收盘价')
        dpg.add_line_series(xData,yDatas["chg"],parent='turnoverrate',label='涨跌额')
        dpg.add_line_series(xData,yDatas["percent"],parent='turnoverrate',label='涨跌幅')
        dpg.add_line_series(xData,yDatas["turnoverrate"],parent='turnoverrate',label='换手率')
        dpg.add_line_series(xData,yDatas["amount"],parent='amount',label='成交额')

        dpg.fit_axis_data(xaxis) # 使横坐标自适应，最终显示为具体日期
        with dpg.tooltip(s1id,label='tool tip',tag="tool tip"): # 创建鼠标悬停显示的组件
            dpg.add_text("Hover the plot",tag="volume tip")

        dpg.pop_container_stack()



class HorGroup:
    def __init__(self,width=40):# 提供可设置的宽度
        with dpg.stage():
            # horizontal=True,设置组内的组件水平放置
            self.id = dpg.add_group(horizontal=True,width=width)

    def add_child(self,child): #  提供增加子组件的接口
        dpg.move_item(child.id,parent=self.id)

    def add_spacer(self):#  提供增加空位的接口
        dpg.push_container_stack(self.id)
        dpg.add_spacer()
        dpg.pop_container_stack()


class Child_Window:
    def __init__(self,width=1200,height=300,tag=TOP_CHILD_WINDOW):
        with dpg.stage():
            self.id = dpg.add_child_window(tag=tag,width=width,height=height)
    def add_child(self,child): # 提供增加子组件的接口
        dpg.move_item(child.id,parent=self.id)
