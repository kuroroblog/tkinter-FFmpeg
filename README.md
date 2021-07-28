# tkinter-FFmpeg
Tkinterを使って、FFmpegをダウンロードする機構を作成する。

# Croudworksの案件リンク
・https://crowdworks.jp/public/jobs/6618056?ref=recommend_by_recent_activities#application_list

# 仕様書
[(配布用)_FFmpegのGUI作成.pdf](https://github.com/kuroroblog/tkinter-FFmpeg/files/6892030/_FFmpeg.GUI.pdf)

# zipをダウンロードしてから動作確認する
1. https://github.com/kuroroblog/tkinter-FFmpeg へアクセスする。
2. 緑色の「Code」と書かれたボタンを選択
3. 「Download ZIP」を選択
4. ダウンロードされたzipファイルをデスクトップへ移動
5. zipファイルをダブルクリック
6. ターミナルを開く。
7. ターミナルを活用して、zipを展開して生成されたフォルダへ移動する。(`$ cd Desktop/tkinter-FFmpeg-master`)
8. `$ python cmd.py`を実行する。
9. 動作確認を行う。

# exeファイル化の流れ
1. terminalを開く。
2. `$ pip list`を実行する。(pyinstaller, pip, pyinstaller-hooks-contribが入っていることを確認) ないライブラリがある場合はpipでinstallする。
3. 実行ファイルディレクトリ箇所へ移動する。(`$ cd /path_to/`)
4. `pyinstaller xxx.py --onefile --clean --noconsole` を実行する。(xxx.pyはファイル名。pyinstallerのオプション詳細 : https://pyinstaller.readthedocs.io/en/stable/usage.html)
5. distフォルダ内に存在する、cmdを実行する。
6. TkinterのWindowが表示される。該当箇所へ値を入力し、「実行」ボタンを選択する。
7. FFmpegがダウンロードされるか、確認する。

# 結果画像
<img width="1680" alt="screenshot 2021-07-28 19 14 33" src="https://user-images.githubusercontent.com/23373288/127305968-2a0938da-f2ba-427f-85f2-8402c857e266.png">
