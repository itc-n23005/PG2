#! python3

text = {'agree': 'そうですね。私も賛同します。それがいいと思います。',
        'busy': 'すみませんが、今週後半か来週にしていただけませんか。',
        'upsell': 'これを毎月の寄付にすることを検討いただけませんか？'}

import sys
import pyperclip

if len(sys.argv) < 2:
    print('使い方: python mclip.py[keyname]')
    print('キーフレーズに対応するテキストをクリップボードにコピーします。')
    sys.exit()

keyname = sys.argv[1]

if keyname in text:
    pyperclip.copy(text[keyname])
    print(keyname + 'のテキストをクリップボードにコピーしました。')
else:
    print(keyname + 'に対応するテキストがありません。')
