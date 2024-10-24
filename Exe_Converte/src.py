import os
import tkinter as tk
from tkinter import filedialog
from tkinter import messagebox
import subprocess

# ファイルを選択する関数
def select_file():
    file_path = filedialog.askopenfilename(filetypes=[("Python files", "*.py")])
    if file_path:
        entry.delete(0, tk.END)
        entry.insert(0, file_path)

# 実行ボタンを押したときにpyinstallerを実行する関数
def convert_to_exe():
    file_path = entry.get()
    if not file_path:
        messagebox.showwarning("警告", "Pythonファイルのパスを入力してください。")
        return
    if not os.path.exists(file_path):
        messagebox.showerror("エラー", "指定されたファイルが存在しません。")
        return

    # PyInstallerコマンドの作成
    command = f"pyinstaller --onefile {file_path}"

    try:
        # コマンドの実行
        subprocess.run(command, shell=True, check=True)
        messagebox.showinfo("成功", "exe化が完了しました。")
    except subprocess.CalledProcessError as e:
        messagebox.showerror("エラー", f"exe化に失敗しました。\n{str(e)}")

# メインウィンドウの設定
root = tk.Tk()
root.title("Py to EXE Converter")
root.geometry("400x150")

# ラベル
label = tk.Label(root, text="Pythonファイルのパスを入力してください：")
label.pack(pady=10)

# ファイルパス入力ボックス
entry = tk.Entry(root, width=40)
entry.pack(pady=5)

# ファイル選択ボタン
file_button = tk.Button(root, text="ファイル選択", command=select_file)
file_button.pack(pady=5)

# 実行ボタン
convert_button = tk.Button(root, text="実行", command=convert_to_exe)
convert_button.pack(pady=10)

# メインループ
root.mainloop()
