import tkinter as tk
from tkinter import messagebox
import subprocess

class Application(tk.Frame):
    # ffmpegのあるディレクトリの変数
    ffmDirectory = None
    # 引数1の変数
    arg1 = None
    # 引数2の変数
    arg2 = None
    # 引数3の変数
    arg3 = None
    # 出力先の変数
    outputDir = None
    # ファイル名の変数
    outputFile = None

    # 「実行」ボタンが選択された場合に、実行される関数
    def executeFunc(self):
        if self.arg1.get() == '' and self.arg2.get() == '' and self.arg3.get() == '':
            # messageboxについて : https://kuroro.blog/python/MQcodS4gkjZ4G7JYhQ9Q/
            messagebox.showwarning('入力エラー', '引数が入力されていません。')
            return
        if self.ffmDirectory.get() == '':
            # messageboxについて : https://kuroro.blog/python/MQcodS4gkjZ4G7JYhQ9Q/
            messagebox.showwarning('入力エラー', 'ffmpegのあるディレクトリが入力されていません。')
            return
        if self.outputDir.get() == '':
            # messageboxについて : https://kuroro.blog/python/MQcodS4gkjZ4G7JYhQ9Q/
            messagebox.showwarning('入力エラー', '出力先が入力されていません。')
            return
        if self.outputFile.get() == '':
            # messageboxについて : https://kuroro.blog/python/MQcodS4gkjZ4G7JYhQ9Q/
            messagebox.showwarning('入力エラー', 'ファイル名が入力されていません。')
            return

        subprocess.run(self.ffmDirectory.get() + ' ' + self.arg1.get() + ' ' + self.arg2.get() + ' ' + self.arg3.get() + ' ' + self.outputDir.get() + '/' + self.outputFile.get(), shell=True)
        messagebox.showinfo('完了しました。')

    def __init__(self, master=None):
        # Windowの初期設定を行う。
        super().__init__(master)

        # Windowの画面サイズを設定する。
        # geometryについて : https://kuroro.blog/python/rozH3S2CYE0a0nB3s2QL/
        self.master.geometry("640x480")
        # Windowへタイトルをつける。
        self.master.title('ffmpegダウンロード')

        # Windowを親要素として、frame Widget(Frame)を作成する。
        # Frameについて : https://kuroro.blog/python/P20XOidA5nh583fYRvxf/
        frame = tk.Frame(self.master)
        # Windowを親要素とした場合に、frame Widget(Frame)をどのように配置するのか?
        # packについて : https://kuroro.blog/python/UuvLfIBIEaw98BzBZ3FJ/
        frame.pack()

        # frame Widget(Frame)を親要素として、label Widgetを作成する。
        # text : テキスト情報
        # Labelについて : https://kuroro.blog/python/Pj4Z7JBNRvcHZvtFqiKD/
        label = tk.Label(frame, text="ffmpegのあるディレクトリ:")
        # frame Widget(Frame)を親要素として、label Widgetをどのように配置するのか。
        # gridについて : https://kuroro.blog/python/JoaowDiUdLAOj3cSBxiX/
        label.grid(column=0, row=0)
        # frame Widget(Frame)を親要素として、entry Widgetを作成する。
        # width : 幅の設定
        # Entryについて : https://kuroro.blog/python/PUZp77YFxrXvMCjpZbUg/
        self.ffmDirectory = tk.Entry(frame, width=50)
        # frame Widget(Frame)を親要素とした場合に、entry Widgetをどのように配置するのか?
        # gridについて : https://kuroro.blog/python/JoaowDiUdLAOj3cSBxiX/
        self.ffmDirectory.grid(column=1, row=0)

        # frame Widget(Frame)を親要素として、label Widgetを作成する。
        # text : テキスト情報
        # Labelについて : https://kuroro.blog/python/Pj4Z7JBNRvcHZvtFqiKD/
        label = tk.Label(frame, text="引数1:")
        # frame Widget(Frame)を親要素として、label Widgetをどのように配置するのか。
        # gridについて : https://kuroro.blog/python/JoaowDiUdLAOj3cSBxiX/
        label.grid(column=0, row=1)
        # frame Widget(Frame)を親要素として、entry Widgetを作成する。
        # width : 幅の設定
        # Entryについて : https://kuroro.blog/python/PUZp77YFxrXvMCjpZbUg/
        self.arg1 = tk.Entry(frame, width=50)
        # frame Widget(Frame)を親要素とした場合に、entry Widgetをどのように配置するのか?
        # gridについて : https://kuroro.blog/python/JoaowDiUdLAOj3cSBxiX/
        self.arg1.grid(column=1, row=1)

        # frame Widget(Frame)を親要素として、label Widgetを作成する。
        # text : テキスト情報
        # Labelについて : https://kuroro.blog/python/Pj4Z7JBNRvcHZvtFqiKD/
        label = tk.Label(frame, text="引数2:")
        # frame Widget(Frame)を親要素として、label Widgetをどのように配置するのか。
        # gridについて : https://kuroro.blog/python/JoaowDiUdLAOj3cSBxiX/
        label.grid(column=0, row=2)
        # frame Widget(Frame)を親要素として、entry Widgetを作成する。
        # width : 幅の設定
        # Entryについて : https://kuroro.blog/python/PUZp77YFxrXvMCjpZbUg/
        self.arg2 = tk.Entry(frame, width=50)
        # frame Widget(Frame)を親要素とした場合に、entry Widgetをどのように配置するのか?
        # gridについて : https://kuroro.blog/python/JoaowDiUdLAOj3cSBxiX/
        self.arg2.grid(column=1, row=2)

        # frame Widget(Frame)を親要素として、label Widgetを作成する。
        # text : テキスト情報
        # Labelについて : https://kuroro.blog/python/Pj4Z7JBNRvcHZvtFqiKD/
        label = tk.Label(frame, text="引数3:")
        # frame Widget(Frame)を親要素として、label Widgetをどのように配置するのか。
        # gridについて : https://kuroro.blog/python/JoaowDiUdLAOj3cSBxiX/
        label.grid(column=0, row=3)
        # frame Widget(Frame)を親要素として、entry Widgetを作成する。
        # width : 幅の設定
        # Entryについて : https://kuroro.blog/python/PUZp77YFxrXvMCjpZbUg/
        self.arg3 = tk.Entry(frame, width=50)
        # frame Widget(Frame)を親要素とした場合に、entry Widgetをどのように配置するのか?
        # gridについて : https://kuroro.blog/python/JoaowDiUdLAOj3cSBxiX/
        self.arg3.grid(column=1, row=3)

        # frame Widget(Frame)を親要素として、label Widgetを作成する。
        # text : テキスト情報
        # Labelについて : https://kuroro.blog/python/Pj4Z7JBNRvcHZvtFqiKD/
        label = tk.Label(frame, text="出力先:")
        # frame Widget(Frame)を親要素として、label Widgetをどのように配置するのか。
        # gridについて : https://kuroro.blog/python/JoaowDiUdLAOj3cSBxiX/
        label.grid(column=0, row=4)
        # frame Widget(Frame)を親要素として、entry Widgetを作成する。
        # width : 幅の設定
        # Entryについて : https://kuroro.blog/python/PUZp77YFxrXvMCjpZbUg/
        self.outputDir = tk.Entry(frame, width=50)
        # frame Widget(Frame)を親要素とした場合に、entry Widgetをどのように配置するのか?
        # gridについて : https://kuroro.blog/python/JoaowDiUdLAOj3cSBxiX/
        self.outputDir.grid(column=1, row=4)

        # frame Widget(Frame)を親要素として、label Widgetを作成する。
        # text : テキスト情報
        # Labelについて : https://kuroro.blog/python/Pj4Z7JBNRvcHZvtFqiKD/
        label = tk.Label(frame, text="ファイル名:")
        # frame Widget(Frame)を親要素として、label Widgetをどのように配置するのか。
        # gridについて : https://kuroro.blog/python/JoaowDiUdLAOj3cSBxiX/
        label.grid(column=0, row=5)
        # frame Widget(Frame)を親要素として、entry Widgetを作成する。
        # width : 幅の設定
        # Entryについて : https://kuroro.blog/python/PUZp77YFxrXvMCjpZbUg/
        self.outputFile = tk.Entry(frame, width=50)
        # frame Widget(Frame)を親要素とした場合に、entry Widgetをどのように配置するのか?
        # gridについて : https://kuroro.blog/python/JoaowDiUdLAOj3cSBxiX/
        self.outputFile.grid(column=1, row=5)

        # Windowを親要素として、button Widgetを作成する。
        # text : テキスト情報
        # command : ボタンを選択した場合に、実行する関数を設定する。self.executeFuncとする。
        # Buttonについて : https://kuroro.blog/python/oFju6EngDtcYtIiMIDf1/
        button = tk.Button(self.master, text="実行", command=self.executeFunc)
        # Windowを親要素とした場合に、button Widgetをどのように配置するのか?
        # packについて : https://kuroro.blog/python/UuvLfIBIEaw98BzBZ3FJ/
        button.pack()

# Tkinter初学者参考 : https://docs.python.org/ja/3/library/tkinter.html#a-simple-hello-world-program
if __name__ == "__main__":
    # Windowを生成する。
    # Windowについて : https://kuroro.blog/python/116yLvTkzH2AUJj8FHLx/
    root = tk.Tk()
    app = Application(master=root)
    # Windowをループさせて、継続的にWindow表示させる。
    # mainloopについて : https://kuroro.blog/python/DmJdUb50oAhmBteRa4fi/
    app.mainloop()
