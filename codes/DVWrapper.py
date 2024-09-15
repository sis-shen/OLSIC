import time

import dearpygui.dearpygui as dpg
from SnowBallCrawler import  *

TOP_CHILD_WINDOW = "top_child_win"
def showTable():
    dpg.configure_item()

def mystampToNumStr(stamp):
    date = time.strftime("%Y/%m/%d", time.localtime(int(stamp / 1000.0)))
    return date

dpg.create_context()


columns = ['序号','时间','成交量(手)','开盘价','最高价','最低价','收盘价','涨跌额','涨跌幅','换手率','成交额(亿)']

class Window:

    def __init__(self,label,tag):
        self._children = []
        with dpg.stage() as stage:
            self.id = dpg.add_window(label=label,tag=tag)
        self.stage = stage

    def add_child(self,child):
        dpg.move_item(child.id,parent=self.id)

    def add_childID(self,childID):
        dpg.move_item(childID,parent=self.id)

    def submit(self):
        dpg.unstage(self.stage)
class DataTable:
    def __init__(self,tag='main table'):
        with dpg.stage():
            self.id = dpg.add_table(header_row=True, policy=dpg.mvTable_SizingFixedFit, row_background=True, reorderable=True,
                   resizable=True, no_host_extendX=False, hideable=True,
                   borders_innerV=True, delay_search=True, borders_outerV=True, borders_innerH=True,
                   borders_outerH=True,height=300,tag=tag)

            dpg.push_container_stack(self.id)
            for i in range(len(columns)):
                dpg.add_table_column(label=columns[i],width_stretch=True, init_width_or_weight=0.0)

            dpg.pop_container_stack()


    def updateData(self,items):
        # 先清除列表
        for item in dpg.get_item_children(self.id,1):
            dpg.delete_item(item)
        dpg.push_container_stack(self.id)
        row = 0
        for item in items:
            row+=1
            with dpg.table_row():
                dpg.add_text(str(row))
                for j in range(len(item)):
                    if(j == 0):
                        date = mystampToNumStr(item[0])
                        dpg.add_text(date)
                    elif(j==10):
                        break
                    else:
                        dpg.add_text(item[j])

        dpg.pop_container_stack()

class MenuItem():
    def __init__(self,menubar,label,tag,target):
        self.parent = menubar.id
        self.target = target
        dpg.push_container_stack(self.parent)
        self.id = dpg.add_menu_item(label=label,tag=tag,user_data=[menubar,self])
        dpg.pop_container_stack()

    def HideCallback(self):
        current_visible = dpg.is_item_visible(self.target)
        if current_visible:
            dpg.hide_item(self.target)
    def setCallback(self,callback):
        dpg.set_item_callback(self.id,callback=callback)
class MenuBar():
    def __init__(self,tag='main menu'):
        self.children = []
        with dpg.stage():
            self.id = dpg.add_menu_bar(tag=tag)

    def add_item(self,label,tag,target,font):
        print(f"new item: tag:{tag},target:{target}")
        self.children.append(MenuItem(self,label=label,tag=tag,target=target))
        child_id = self.children[-1].id
        dpg.bind_item_font(child_id,font)
        self.children[-1].HideCallback()
        return child_id

    def hide_children(self):
        for child in self.children:
            child.HideCallback()

class Button:
    def __init__(self,label,tag):
        with dpg.stage():
            self.id=dpg.add_button(label=label,tag=tag,width=150,height=40)

    def setcallback(self,callback):
        dpg.set_item_callback(self.id,callback=callback)

class KPlot:
    def __init__(self):
        with dpg.stage():
            with dpg.plot(label="日K图",tag='kplot',height=-1,width=-1,show=False) as self.id:
                dpg.add_plot_legend()

    def draw(self,fetch_data):
        xData=[]
        yDatas={"volume":[],"open":[],"high":[],"low":[],
                "close":[],"chg":[],"percent":[],
                "turnoverrate":[],"amount":[]}
        for line in fetch_data:
            line = list(line)
            xData.append(line.pop(0))
            yDatas["volume"].append(line.pop(0))
            yDatas["open"].append(line.pop(0))
            yDatas["high"].append(line.pop(0))
            yDatas["low"].append(line.pop(0))
            yDatas['close'].append(line.pop(0))
            yDatas['chg'].append(line.pop(0))
            yDatas['percent'].append(line.pop(0))
            yDatas['turnoverrate'].append(line.pop(0))
            yDatas['amount'].append(line.pop(0))
        def custom_tooltip_handler(sender,app_data):
            x_data,y_data=dpg.get_plot_mouse_pos()
            date = mystampToNumStr(x_data)
            index = 0
            while( index < len(xData) and date != mystampToNumStr(xData[index]) ):
                index+=1
            if(index < len(xData)):
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
            dpg.add_mouse_move_handler(callback=custom_tooltip_handler)

        dpg.push_container_stack(self.id)
        dpg.add_plot_axis(dpg.mvXAxis,label="日期")
        dpg.add_plot_axis(dpg.mvYAxis,label="成交量",tag="volume")

        sid1 = dpg.add_line_series(xData,yDatas["volume"],parent="volume")

        with dpg.tooltip(sid1,label='tool tip',tag="tool tip"):
            dpg.add_text("Hover the plot",tag="volume tip")


        dpg.pop_container_stack()


class HorGroup:
    def __init__(self,width=40):
        with dpg.stage():
            self.id = dpg.add_group(horizontal=True,width=width)

    def add_child(self,child):
        dpg.move_item(child.id,parent=self.id)

    def add_spacer(self):
        dpg.push_container_stack(self.id)
        dpg.add_spacer()
        dpg.pop_container_stack()


class Child_Window:
    def __init__(self,width=1200,height=300,tag=TOP_CHILD_WINDOW):
        with dpg.stage():
            self.id = dpg.add_child_window(tag=tag,width=width,height=height)
    def add_child(self,child):
        dpg.move_item(child.id,parent=self.id)
