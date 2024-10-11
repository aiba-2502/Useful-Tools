import tkinter as tk
from tkinter import messagebox
import time
import threading
from plyer import notification

# タイマー処理の関数
def start_timer():
    try:
        # ユーザー入力を取得して秒に変換
        hours = int(entry_hours.get())
        minutes = int(entry_minutes.get())
        seconds = int(entry_seconds.get())
        total_seconds = hours * 3600 + minutes * 60 + seconds

        if total_seconds <= 0:
            messagebox.showwarning("警告", "時間を正しく入力してください。")
            btn_start.config(state="normal")  # 開始ボタンを再度有効化
            return

        # カウントダウンを開始
        while total_seconds > 0:
            time.sleep(1)
            total_seconds -= 1

            # 残り時間を時:分:秒に変換して表示
            remaining_hours = total_seconds // 3600
            remaining_minutes = (total_seconds % 3600) // 60
            remaining_seconds = total_seconds % 60
            time_str = f"{remaining_hours:02}:{remaining_minutes:02}:{remaining_seconds:02}"
            label_timer.config(text=time_str)

        # カウントダウン終了後に通知
        notify()

    except ValueError:
        messagebox.showerror("エラー", "無効な入力です。数字を入力してください。")
        btn_start.config(state="normal")  # 開始ボタンを再度有効化

# 通知の関数
def notify():
    global notification_active
    if not notification_active:  # 通知がまだアクティブでない場合のみ通知を表示
        notification.notify(
            title="タイマー終了",
            message="タイマーが終了しました！",
            timeout=10  # 通知が自動で消える時間（秒）
        )
        notification_active = True
        btn_clear_notification.config(state="normal")

# 通知を消す関数
def clear_notification():
    global notification_active
    label_timer.config(text="00:00:00")
    btn_clear_notification.config(state="disabled")
    btn_start.config(state="normal")  # 開始ボタンを再度有効化
    notification_active = False  # 通知を消す

# タイマーを別スレッドで実行
def start_thread():
    btn_start.config(state="disabled")  # 開始ボタンを無効化
    thread = threading.Thread(target=start_timer)
    thread.start()

# GUI設定
root = tk.Tk()
root.title("タイマーアプリ")

# グローバル変数
notification_active = False  # 通知がアクティブかどうかを管理

# 時・分・秒の入力フィールドとラベル
frame = tk.Frame(root)
frame.pack(pady=20)

label_hours = tk.Label(frame, text="時:")
label_hours.grid(row=0, column=0)
entry_hours = tk.Entry(frame, width=5)
entry_hours.grid(row=0, column=1)

label_minutes = tk.Label(frame, text="分:")
label_minutes.grid(row=0, column=2)
entry_minutes = tk.Entry(frame, width=5)
entry_minutes.grid(row=0, column=3)

label_seconds = tk.Label(frame, text="秒:")
label_seconds.grid(row=0, column=4)
entry_seconds = tk.Entry(frame, width=5)
entry_seconds.grid(row=0, column=5)

# タイマー表示ラベル
label_timer = tk.Label(root, text="00:00:00", font=("Helvetica", 48))
label_timer.pack(pady=20)

# 開始ボタン
btn_start = tk.Button(root, text="開始", command=start_thread)
btn_start.pack(pady=10)

# 通知を消すボタン
btn_clear_notification = tk.Button(root, text="通知を消す", command=clear_notification, state="disabled")
btn_clear_notification.pack(pady=10)

# メインループ開始
root.mainloop()
