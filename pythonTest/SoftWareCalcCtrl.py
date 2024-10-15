
import uiautomation as auto

winName = "计算器"
# 查找主窗口
window = auto.WindowControl(searchDepth=10, Name=winName)

# # 打印所有控件的名称和类型
# for control, depth in auto.WalkControl(window):
#     print(f"{' ' * depth * 2}{control.ControlType}: {control.Name}")

window.SetTopmost(True)
window.ButtonControl(AutomationId="num7Button").Click()
window.ButtonControl(AutomationId="plusButton").Click()
window.ButtonControl(AutomationId="num5Button").Click()
window.ButtonControl(AutomationId="equalButton").Click()

result = window.TextControl(AutomationId="DisplayControls")
print(f"Result: {result.Name}")
