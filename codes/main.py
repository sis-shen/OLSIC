# import dearpygui.dearpygui as dpg
# import dearpygui.demo as demo
#
# dpg.create_context()
# dpg.create_viewport(title='Custom Title', width=600, height=600)
#
# demo.show_demo()
#
# dpg.setup_dearpygui()
# dpg.show_viewport()
# dpg.start_dearpygui()
# dpg.destroy_context()

# import dearpygui.dearpygui as dpg
#
# dpg.create_context()
#
# def button_callback(sender,app_data,user_data):
#     print(f"sender is {sender}")
#     print(f"app_data is {app_data}")
#     print(f"user_data is {user_data}")
#
# with dpg.window(tag="Example Window"):
#     t1= dpg.add_text("Hello, world")
#     b1 = dpg.add_button(label="Save")
#     dpg.add_input_text(label="string", default_value="Quick brown fox")
#     dpg.add_slider_float(label="float", default_value=0.273, max_value=1)
#
#     with dpg.group():
#         dpg.add_button(label='Button3',callback=button_callback,user_data="some what data",tag="im button 3")
#         dpg.add_text("Fuck!")
#         with dpg.group() as  group1:
#             pass
#         with dpg.group():
#             dpg.add_text("6666666666666666")
#             dpg.add_text("xxxxxxxxxxxxxx")
#
#
# dpg.add_text("ccchild",parent=group1)
#
# dpg.create_viewport(title='Custom Title', width=600, height=200)
# dpg.set_primary_window("Example Window",True)
# dpg.setup_dearpygui()
# dpg.show_viewport()
#
# print(t1)
# print(b1)
#
# # below replaces, start_dearpygui()
# while dpg.is_dearpygui_running():
#     # insert here any code you would like to run in the render loop
#     # you can manually stop by using stop_dearpygui()
#     # print("this will run every frame")
#     dpg.render_dearpygui_frame()
#
# dpg.destroy_context()


# import dearpygui.dearpygui as dpg
#
# dpg.create_context()
#
# def button_callback(sender, app_data, user_data):
#     print(f"sender is: {sender}")
#     print(f"app_data is: {app_data}")
#     print(f"user_data is: {user_data}")
#
# with dpg.window(label="Tutorial"):
#     # user data and callback set when button is created
#     dpg.add_button(label="Apply", callback=button_callback, user_data="Some Data")
#
#     # user data and callback set any time after button has been created
#     btn = dpg.add_button(label="Apply 2", )
#     dpg.set_item_callback(btn, button_callback)
#     dpg.set_item_user_data(btn, "Some Extra User Data")
#
# dpg.create_viewport(title='Custom Title', width=800, height=600)
# dpg.setup_dearpygui()
# dpg.show_viewport()
# dpg.start_dearpygui()
# dpg.destroy_context()


# import dearpygui.dearpygui as dpg
#
# dpg.create_context()
#
# def print_value(sender):
#     print(dpg.get_value(sender))
#
# with dpg.window(width=300):
#     input_txt1 = dpg.add_input_text()
#     # The value for input_text2 will have a starting value
#     # of "This is a default value!"
#     input_txt2 = dpg.add_input_text(
#         label="InputTxt2",
#         default_value="This is a default value!",
#         callback=print_value
#     )
#
#     slider_float1 = dpg.add_slider_float()
#     # The slider for slider_float2 will have a starting value
#     # of 50.0.
#     slider_float2 = dpg.add_slider_float(
#         label="SliderFloat2",
#         default_value=50.0,
#         callback=print_value
#     )
#
#     dpg.set_item_callback(input_txt1, print_value)
#     dpg.set_item_callback(slider_float1, print_value)
#
#     print(dpg.get_value(input_txt1))
#     print(dpg.get_value(input_txt2))
#     print(dpg.get_value(slider_float1))
#     print(dpg.get_value(slider_float2))
#
# dpg.create_viewport(title='Custom Title', width=800, height=600)
# dpg.setup_dearpygui()
# dpg.show_viewport()
# dpg.start_dearpygui()
# dpg.destroy_context()

# import dearpygui.dearpygui as dpg
# import time
#
# dpg.create_context()
#
# def chane_text(sender,app_data):
#     print("got it")
#     dpg.set_value("out put",f"Mouse Button ID: {app_data}")
#
# def hover(sender):
#     print(f"{sender} hovering")
#
# with dpg.window(width=500,height=300):
#     dpg.add_button(label="Click me",tag="text item")
#     dpg.add_text("Listening",tag="out put")
#     with dpg.item_handler_registry(tag="widget handler") as handler:
#         dpg.add_item_clicked_handler(callback=chane_text)
#         dpg.add_item_hover_handler(callback=hover)
#     dpg.bind_item_handler_registry("text item","widget handler")



# dpg.create_viewport(title='Custom Title', width=800, height=600)
# dpg.setup_dearpygui()
# dpg.show_viewport()
# dpg.start_dearpygui()
# dpg.destroy_context()


import dearpygui.dearpygui as dpg

dpg.create_context()

def change_text(sender, app_data):
    dpg.set_value("text item", f"Mouse Button ID: {app_data}")

def visible_call(sender, app_data):
    print("I'm visible")

with dpg.window(tag="Primary Window"):
    dpg.add_text("Hello, world")
    dpg.add_text("Click me with any mouse button", tag="text item")
    dpg.add_text("Close window with arrow to change visible state printing to console", tag="text item 2")

dpg.bind_item_handler_registry("text item", "widget handler")
dpg.bind_item_handler_registry("text item 2", "widget handler")

dpg.create_viewport(title='Custom Title', width=600, height=200)
dpg.setup_dearpygui()
dpg.show_viewport()
dpg.set_primary_window("Primary Window", True)
dpg.start_dearpygui()
dpg.destroy_context()