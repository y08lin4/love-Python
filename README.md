# love-Python

一个使用 Python Tkinter 制作的桌面爱心弹窗小程序：先按爱心轨迹弹出无边框提示块，再随机铺满屏幕。

## 功能特点

- 使用标准库 `tkinter`，无需安装第三方依赖
- 自动根据屏幕分辨率缩放弹窗尺寸与字体
- Windows 下启用 DPI 感知，减少高分屏显示偏差
- 168 条祝福语随机不重复轮播，减少重复内容
- 支持按 `Esc` / `Space` 或右键弹窗一键关闭

## 运行环境

- Python 3.10+
- 推荐 Windows 桌面环境运行

## 使用方法

```bash
python love_popup.py
```

运行后会依次显示爱心弹窗动画和随机弹窗。若需要提前退出，按 `Esc` / `Space`，或右键任意弹窗即可。

## 项目结构

```text
.
├── love_popup.py   # 主程序
├── README.md       # 项目说明
└── .gitignore      # Git 忽略规则
```
