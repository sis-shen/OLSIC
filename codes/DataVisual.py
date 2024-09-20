import dearpygui.dearpygui as dpg

from DVWrapper import *
import DBManager as dbm
import time


maotai = GZMaoTai()
def getTimestamp():# 获取秒级的当前时间戳
    t=time.time()
    return int(round(t*1000))

dpg.create_context()

def commonMenuCallback(sender,app_data,user_data): # 声明通用的菜单选项的回调函数
    user_data[0].hide_children() #规定user_data[0]为菜单对象,隐藏所有被控组件
    dpg.show_item(user_data[1].target) # 最后再只显示自己

def DBUpdateCallback(sender,app_data):  # 声明按下按钮的回调函数
    dpg.set_item_label(sender,"数据更新中...") #更改按钮显示内容
    dpg.disable_item(sender) # 调用函数期间使按钮无效化
    dbm.clearDB() # 清空数据库
    my_table.clearData() # 情况表格
    items = maotai.get_response(getTimestamp())  # 获取最新数据
    dbm.sendData(items)  # 向数据库发送数据
    fetch_data = dbm.getLatestData()  # 从数据库获取数据
    my_table.updateData(fetch_data)  # 更新表格
    dpg.set_item_label(sender,"更新数据库数据")  # 改回按钮的显示内容
    dpg.enable_item((sender)) # 重新启用按钮


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
my_table = DataTable() # 实例化表格

update_button = Button(label="更新数据库数据",tag="update button") # 实例化按钮
update_button.setcallback(DBUpdateCallback)  # 设置回调函数

kplot = KPlot() # 实例化图标

menubar = MenuBar() # 实例化菜单栏

# 添加菜单栏选项
table_menu = menubar.add_item(label="表格",tag="table",target=my_table.id,font=menufont)
kplot_menu = menubar.add_item(label="日K图",tag="Kplot",target=kplot.id,font=menufont)
# 绑定惨淡了选项的回调函数
dpg.set_item_callback(table_menu,commonMenuCallback)
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


# items = maotai.get_response(getTimestamp())

fetch_data = dbm.getLatestData()
my_table.updateData(fetch_data)
kplot.draw(fetch_data)


dbm.closeDB()
dpg.create_viewport(title='Custom Title', width=1400, height=600)
dpg.setup_dearpygui()
dpg.show_viewport()
dpg.set_primary_window("main_win", True) # 真正设置初始窗口
dpg.start_dearpygui()

dpg.destroy_context()