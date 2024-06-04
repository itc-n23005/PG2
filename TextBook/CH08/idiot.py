import pyinputplus as pyip

while True:
    prompt='バカを何時間も忙しくさせておく方法を知りたいですか？'
    response = pyip.inputYesNo(prompt)
    if response == 'yes':
        print(prompt)
    if response == 'no':
        print('ありがとう、ごきげんよう。')
        break

