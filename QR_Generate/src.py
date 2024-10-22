import tkinter as tk
from tkinter import messagebox
from PIL import Image, ImageTk
import qrcode

def generate_qr_code():
    # テキスト入力からデータを取得
    qr_data = entry.get()
    
    if qr_data.strip() == "":
        messagebox.showerror("Error", "QRコードに必要なテキストを入力してください")
        return

    # QRコードの生成
    qr = qrcode.QRCode(
        version=1,
        error_correction=qrcode.constants.ERROR_CORRECT_L,
        box_size=10,
        border=4,
    )
    qr.add_data(qr_data)
    qr.make(fit=True)

    img = qr.make_image(fill='black', back_color='white')

    # 画像をPILからTkinterで表示できる形式に変換
    img = img.resize((200, 200))
    tk_img = ImageTk.PhotoImage(img)

    # キャンバスにQRコードを表示
    canvas.create_image(100, 100, image=tk_img)
    canvas.image = tk_img  # 参照を保持する必要がある

# Tkinterウィンドウの設定
root = tk.Tk()
root.title("QRコード生成アプリ")

# エントリーフィールドとボタン
label = tk.Label(root, text="QRコードにしたいテキストを入力してください：")
label.pack(pady=10)

entry = tk.Entry(root, width=40)
entry.pack(pady=5)

generate_button = tk.Button(root, text="QRコードを生成", command=generate_qr_code)
generate_button.pack(pady=10)

# QRコード表示用のキャンバス
canvas = tk.Canvas(root, width=200, height=200)
canvas.pack(pady=20)

# メインループ
root.mainloop()
