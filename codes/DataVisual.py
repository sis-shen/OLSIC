import dearpygui.dearpygui as dpg

from DVWrapper import *
import DBManager as dbm
import time

maotai = GZMaoTai()
def getTimestamp():
    t=time.time()
    return int(round(t*1000))

dpg.create_context()

def commonMenuCallback(sender,app_data,user_data):
    print("commonMenuCallbackMenuCallback")
    user_data[0].hide_children()
    dpg.show_item(user_data[1].target)
def DBclearCallback():
    dbm.clearDB()

def DBUpdateCallback(sender,app_data):
    dbm.clearDB()
    dpg.set_item_label(sender,"数据更新中...")
    dpg.disable_item(sender)
    items = maotai.get_response(getTimestamp())
    dbm.sendData(items)
    fetch_data = dbm.getLatestData()
    my_table.updateData(fetch_data)
    dpg.set_item_label(sender,"更新数据库数据")
    dpg.enable_item((sender))


######  设置字体 ###########

with dpg.font_registry():
    with dpg.font("./fonts/msyh.ttc",20) as default_font:
        dpg.add_font_range_hint(dpg.mvFontRangeHint_Chinese_Simplified_Common)
    with dpg.font("./fonts/msyh.ttc",25) as big_font:
        dpg.add_font_range_hint(dpg.mvFontRangeHint_Chinese_Simplified_Common)
    with dpg.font("./fonts/msyh.ttc",20) as menufont:
        dpg.add_font_range_hint(dpg.mvFontRangeHint_Chinese_Simplified_Common)



###### 程序主要内容 ########
# 构建可视化组件
my_table = DataTable()

update_button = Button(label="更新数据库数据",tag="update button")
update_button.setcallback(DBUpdateCallback)

# clear_button = Button(label="清空数据库数据",tag="clear button")
# clear_button.setcallback(DBclearCallback)

kplot = KPlot()

print(kplot.id)

menubar = MenuBar()

table_menu = menubar.add_item(label="表格",tag="table",target=my_table.id,font=menufont)
kplot_menu = menubar.add_item(label="日K图",tag="Kplot",target=kplot.id,font=menufont)


dpg.set_item_callback(table_menu,commonMenuCallback)
dpg.set_item_callback(kplot_menu,commonMenuCallback)
dpg.set_item_callback(kplot_menu,commonMenuCallback)
# 创建窗口
main_win = Window(label="main_win",tag="main_win")
# 创建子窗口
top_child_win = Child_Window(width=-1,height=400)
top_child_win.add_child(my_table)
top_child_win.add_child(kplot)

## 构建父子关系
dpg.bind_font(default_font)
dpg.bind_item_font(update_button.id,big_font)
# dpg.bind_item_font(clear_button.id,big_font)
dpg.bind_item_font(menubar.id,menufont)
main_win.add_child(menubar)
main_win.add_child(top_child_win)



button_group = HorGroup(width=300)
button_group.add_spacer()
inner_group = HorGroup()
inner_group.add_child(update_button)
# inner_group.add_child(clear_button)
button_group.add_child(inner_group)
button_group.add_spacer()
main_win.add_child(button_group)

main_win.submit()


items = maotai.get_response(getTimestamp())

fetch_data = dbm.getLatestData()
print(fetch_data)
my_table.updateData(fetch_data)
kplot.draw(fetch_data)


dbm.closeDB()
dpg.create_viewport(title='Custom Title', width=1400, height=600)
dpg.setup_dearpygui()
dpg.show_viewport()
dpg.set_primary_window("main_win", True) # 真正设置初始窗口
dpg.start_dearpygui()

dpg.destroy_context()