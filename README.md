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

## 打包 EXE

项目已配置 GitHub Actions 自动打包 Windows 版 `love_popup.exe`：

1. 打开 GitHub 仓库的 `Actions` 页面
2. 进入 `Build Windows EXE`
3. 等待运行完成后，在页面底部 `Artifacts` 下载 `love_popup-windows-exe`

也可以在本地使用 PyInstaller 打包：

```bash
python -m pip install pyinstaller
pyinstaller --noconfirm --clean --onefile --windowed --name love_popup love_popup.py
```

打包结果在 `dist/love_popup.exe`。

## 项目结构

```text
.
├── .github/workflows/build-windows-exe.yml
├── love_popup.py   # 主程序
├── README.md       # 项目说明
└── .gitignore      # Git 忽略规则
```
