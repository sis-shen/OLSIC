import dearpygui.dearpygui as dpg
import numpy as np

def setup_ui():
    dpg.create_context()

    # 创建一个窗口
    with dpg.window(label="Example Window"):
        # 创建一个绘图区域
        with dpg.plot(label="Multiple Lines Plot", height=400, width=600):
            dpg.add_plot_legend()  # 添加图例

            # 设置轴标签
            dpg.add_plot_axis(dpg.mvXAxis, label="X Axis")
            y_axis = dpg.add_plot_axis(dpg.mvYAxis, label="Y Axis")

            # 添加多条折线
            for i in range(6):  # 生成 6 条折线
                x = np.linspace(0, 10, 100)  # X 轴数据
                y = np.sin(x + (i * np.pi/6))  # Y 轴数据（每条折线有不同的相位）
                dpg.add_line_series(x, y, label=f"Line {i+1}", parent=y_axis)

    dpg.create_viewport(title='Dear PyGui Multiple Lines Example', width=800, height=600)
    dpg.setup_dearpygui()
    dpg.show_viewport()
    dpg.start_dearpygui()
    dpg.destroy_context()

setup_ui()
