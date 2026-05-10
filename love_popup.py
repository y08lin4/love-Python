import math
import random
import sys
import tkinter as tk


# ===== Douyin-like preset (base design: 1920x1080) =====
POPUP_W = 168
POPUP_H = 42
WINDOW_PADDING = 3
WINDOW_CORNER_BORDER = 1
WINDOW_EDGE_MARGIN = 12

HEART_COUNT = 82
HEART_SCALE_X = 28
HEART_SCALE_Y = 27
HEART_CENTER_X_RATIO = 0.50
HEART_CENTER_Y_RATIO = 0.46

HEART_INTERVAL_MS = 11
HEART_HOLD_MS = 1100
SCATTER_INTERVAL_MS = 6

SCATTER_MIN_COUNT = 95
SCATTER_MAX_COUNT = 180
SCATTER_COUNT_OFFSET = 35

FONT_NAME = "Microsoft YaHei UI"
FONT_SIZE = 15
TOPMOST = True
BORDER_COLOR = "#fff7fb"
TEXT_COLOR = "#222222"

BASE_TEXTS = [
    "多喝水哦~",
    "好好爱自己",
    "好好吃饭",
    "保持好心情",
    "我想你了",
    "顺顺利利",
    "天天开心",
    "万事胜意",
    "平安喜乐",
    "所愿皆成",
    "好运常伴",
    "笑口常开",
    "心想事成",
    "万事顺遂",
    "一路生花",
    "眼里有光",
    "心里有糖",
    "被爱包围",
    "喜乐无忧",
    "岁岁欢愉",
    "日日温柔",
    "梦想成真",
    "前程似锦",
    "未来可期",
    "诸事皆顺",
    "好运爆棚",
    "开心加倍",
    "烦恼退散",
    "快乐满格",
    "幸福满满",
    "温柔常在",
    "可爱常在",
    "热爱常在",
    "好运在线",
    "健康平安",
    "吃嘛嘛香",
    "睡个好觉",
    "别熬夜啦",
    "早点休息",
    "按时吃饭",
    "记得添衣",
    "天冷多穿",
    "别太辛苦",
    "慢慢来呀",
    "你超棒的",
    "给你比心",
    "抱抱你呀",
    "今天很乖",
    "明天更甜",
    "生活很甜",
    "春风得意",
    "一路顺风",
    "事事有回应",
    "件件有着落",
    "天天有惊喜",
    "每天都闪光",
    "快乐不打烊",
    "浪漫不缺席",
    "好运不迟到",
    "烦恼全清零",
    "开心全拉满",
    "好运在路上",
    "温暖在身旁",
    "月亮也爱你",
    "星星陪着你",
    "花会为你开",
    "风会抱抱你",
    "雨后见彩虹",
    "抬头见好运",
    "低头捡快乐",
    "心情亮晶晶",
    "笑容甜甜的",
    "元气满满呀",
    "好运连连呀",
    "生活亮堂堂",
    "一切都值得",
    "你值得被爱",
    "你值得最好",
]

WISHES = [
    "被偏爱",
    "被珍惜",
    "有底气",
    "有勇气",
    "有热爱",
    "有惊喜",
    "有好运",
    "有晴天",
    "有糖吃",
    "有花收",
    "有梦做",
    "有光芒",
    "不孤单",
    "少烦恼",
    "多欢笑",
    "常自在",
    "常欢喜",
    "常安稳",
    "常被爱",
    "常幸运",
    "常开心",
    "常明媚",
    "常热烈",
    "常温柔",
    "常发光",
    "常如愿",
    "常顺利",
    "常自由",
    "常浪漫",
    "常漂亮",
    "常可爱",
    "常优秀",
    "常勇敢",
    "常坚定",
    "常清醒",
    "常快乐",
    "常幸福",
    "常健康",
    "常平安",
    "常闪耀",
    "常被宠",
    "常安心",
    "常美好",
    "常有钱",
    "常开挂",
    "常满分",
    "常惊艳",
    "常从容",
    "常明亮",
    "常灿烂",
    "常轻松",
    "常得偿",
    "常圆满",
    "常雀跃",
    "常被懂",
    "常被疼",
    "常被护",
    "常被夸",
    "常有糖",
    "常有光",
]

COMPANIONS = [
    "好运",
    "快乐",
    "幸福",
    "平安",
    "健康",
    "温柔",
    "浪漫",
    "热爱",
    "惊喜",
    "甜蜜",
    "阳光",
    "鲜花",
    "星光",
    "自由",
    "勇气",
    "底气",
    "福气",
    "财运",
    "灵感",
    "笑容",
]

TEXTS = list(
    dict.fromkeys(
        BASE_TEXTS
        + [f"愿你{wish}" for wish in WISHES]
        + [f"{item}常伴" for item in COMPANIONS]
        + [f"{item}满满" for item in COMPANIONS[:12]]
    )
)

COLORS = [
    "#ffd1dc",
    "#c7efff",
    "#b7f7b0",
    "#fff6bf",
    "#ff7adf",
    "#9ef58e",
    "#91ddff",
    "#ffc4d6",
    "#d9c7ff",
    "#ffe0a3",
]


def enable_dpi_awareness() -> None:
    if not sys.platform.startswith("win"):
        return

    try:
        import ctypes

        try:
            ctypes.windll.shcore.SetProcessDpiAwareness(1)
        except Exception:
            ctypes.windll.user32.SetProcessDPIAware()
    except Exception:
        pass


class ShuffledBag:
    """Randomly consume every item once before repeating."""

    def __init__(self, items: list[str]) -> None:
        if not items:
            raise ValueError("items must not be empty")

        self.items = items[:]
        self.queue: list[str] = []
        self.last: str | None = None

    def next(self) -> str:
        if not self.queue:
            self.queue = self.items[:]
            random.shuffle(self.queue)

            # Avoid the last item from the previous round appearing again first.
            if self.last is not None and len(self.queue) > 1 and self.queue[-1] == self.last:
                self.queue[0], self.queue[-1] = self.queue[-1], self.queue[0]

        value = self.queue.pop()
        self.last = value
        return value


class LovePopupApp:
    def __init__(self) -> None:
        enable_dpi_awareness()

        self.root = tk.Tk()
        self.root.withdraw()

        self.screen_w = self.root.winfo_screenwidth()
        self.screen_h = self.root.winfo_screenheight()
        self.ui_scale = max(0.85, min(1.2, min(self.screen_w / 1920, self.screen_h / 1080)))

        self.popup_w = max(132, int(POPUP_W * self.ui_scale))
        self.popup_h = max(36, int(POPUP_H * self.ui_scale))
        self.font = (FONT_NAME, max(14, int(FONT_SIZE * self.ui_scale)))
        self.window_edge_margin = max(8, int(WINDOW_EDGE_MARGIN * self.ui_scale))

        self.text_pool = ShuffledBag(TEXTS)
        self.color_pool = ShuffledBag(COLORS)

        self.heart_windows: list[tk.Toplevel] = []
        self.scatter_windows: list[tk.Toplevel] = []
        self.scatter_done = False

        self.points = self.build_heart_points(HEART_COUNT)
        self.scatter_total = self.build_scatter_total()

        self.root.bind_all("<Escape>", self.close_all)
        self.root.bind_all("<space>", self.close_all)

    def build_scatter_total(self) -> int:
        raw = (
            (self.screen_w // max(self.popup_w, 1))
            * (self.screen_h // max(self.popup_h + self.window_edge_margin, 1))
            - SCATTER_COUNT_OFFSET
        )
        return max(SCATTER_MIN_COUNT, min(SCATTER_MAX_COUNT, raw))

    def build_heart_points(self, count: int) -> list[tuple[int, int]]:
        points: list[tuple[int, int]] = []
        scale_x = HEART_SCALE_X * self.ui_scale
        scale_y = HEART_SCALE_Y * self.ui_scale
        center_x = self.screen_w * HEART_CENTER_X_RATIO
        center_y = self.screen_h * HEART_CENTER_Y_RATIO

        max_x = max(0, self.screen_w - self.popup_w)
        max_y = max(0, self.screen_h - self.popup_h - self.window_edge_margin)

        for i in range(count):
            t = i / count * 2 * math.pi
            x = 16 * math.sin(t) ** 3
            y = (
                13 * math.cos(t)
                - 5 * math.cos(2 * t)
                - 2 * math.cos(3 * t)
                - math.cos(4 * t)
            )

            sx = int(center_x + x * scale_x - self.popup_w / 2)
            sy = int(center_y - y * scale_y - self.popup_h / 2)

            sx = max(0, min(max_x, sx))
            sy = max(0, min(max_y, sy))
            points.append((sx, sy))

        return points

    def create_popup(self, x: int, y: int, text: str | None = None, color: str | None = None) -> tk.Toplevel:
        win = tk.Toplevel(self.root)
        win.overrideredirect(True)
        win.configure(bg=BORDER_COLOR)
        win.geometry(f"{self.popup_w}x{self.popup_h}+{x}+{y}")
        win.resizable(False, False)

        try:
            win.attributes("-topmost", TOPMOST)
        except tk.TclError:
            pass

        frame = tk.Frame(win, bg=BORDER_COLOR, bd=0, highlightthickness=0)
        frame.pack(fill="both", expand=True)

        label = tk.Label(
            frame,
            text=text or self.text_pool.next(),
            bg=color or self.color_pool.next(),
            fg=TEXT_COLOR,
            font=self.font,
            relief="flat",
            bd=0,
            padx=WINDOW_PADDING,
        )
        label.pack(
            fill="both",
            expand=True,
            padx=WINDOW_CORNER_BORDER,
            pady=WINDOW_CORNER_BORDER,
        )

        win.protocol("WM_DELETE_WINDOW", lambda w=win: self.close_one(w))
        for widget in (win, frame, label):
            widget.bind("<Escape>", self.close_all)
            widget.bind("<space>", self.close_all)
            widget.bind("<Button-3>", self.close_all)

        win.bind("<Button-1>", lambda _event, w=win: w.focus_force())
        win.lift()
        return win

    def close_one(self, win: tk.Toplevel) -> None:
        try:
            win.destroy()
        except tk.TclError:
            pass
        self.cleanup_dead_windows()

    def cleanup_dead_windows(self) -> None:
        self.heart_windows = [w for w in self.heart_windows if w.winfo_exists()]
        self.scatter_windows = [w for w in self.scatter_windows if w.winfo_exists()]

        if self.scatter_done and not self.heart_windows and not self.scatter_windows:
            self.close_all()

    def close_all(self, _event=None) -> None:
        for win in self.heart_windows + self.scatter_windows:
            try:
                win.destroy()
            except tk.TclError:
                pass

        self.heart_windows.clear()
        self.scatter_windows.clear()

        try:
            self.root.quit()
            self.root.destroy()
        except tk.TclError:
            pass

    def show_heart(self, index: int = 0) -> None:
        if index >= len(self.points):
            self.root.after(HEART_HOLD_MS, self.clear_heart)
            return

        x, y = self.points[index]

        text = None
        color = None
        if index == len(self.points) // 2:
            text = "保持好心情"
            color = "lightgreen"

        win = self.create_popup(x, y, text=text, color=color)
        self.heart_windows.append(win)
        self.root.after(HEART_INTERVAL_MS, self.show_heart, index + 1)

    def clear_heart(self) -> None:
        for win in self.heart_windows:
            try:
                win.destroy()
            except tk.TclError:
                pass
        self.heart_windows.clear()
        self.show_scatter()

    def show_scatter(self, index: int = 0) -> None:
        if index >= self.scatter_total:
            self.scatter_done = True
            self.cleanup_dead_windows()
            return

        max_x = max(0, self.screen_w - self.popup_w)
        max_y = max(0, self.screen_h - self.popup_h - self.window_edge_margin)
        x = random.randint(0, max_x)
        y = random.randint(0, max_y)

        win = self.create_popup(x, y)
        self.scatter_windows.append(win)
        self.root.after(SCATTER_INTERVAL_MS, self.show_scatter, index + 1)

    def run(self) -> None:
        self.show_heart()
        self.root.mainloop()


if __name__ == "__main__":
    LovePopupApp().run()
