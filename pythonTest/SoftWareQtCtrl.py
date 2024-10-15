
import uiautomation as auto

window = auto.WindowControl(searchDepth=10, Name='ImgProcess')  # 应用程序窗口标题

# 查找 QTableWidget 控件，通过 AutomationId 定位
qtable_widget = window.TabControl(AutomationId='ImgProcessClass.centralWidget.tabWidget.qt_tabwidget_tabbar')  # 替换为实际的 AutomationId

if not qtable_widget.Exists():
    print('未找到 QTableWidget 控件')
else:
    print('QTableWidget 已找到，开始扫描子项...')

    # 遍历子项
    table_items = qtable_widget.GetChildren()  # 获取 QTableWidget 的所有子项
    for item in table_items:
        print(f'子项：{item.Name}, 控件类型：{item.ControlTypeName}')

        # 查找名称为 "色域" 的子项
        if item.Name == "图像处理":
            print('找到色域子项，准备点击...')
            item.Click()  # 点击 "色域" 子项
            break
    else:
        print('未找到名字为 "色域" 的子项')