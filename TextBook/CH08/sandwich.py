import pyinputplus as pyip

def sandwich_maker():
    bread_price = {'小麦パン':100, '白パン':120, 'サワー種':150}
    protain_price = {'チキン':200, 'ハム':180, 'ターキー':250, '豆腐':170}
    cheese_price = {'チェダー':50, 'スイス':60, 'モッツァレラ':70}
    extra_price = {'トマト':20, 'レタス':15, 'マヨネーズ':10, 'マスタード':10}

    bread = pyip.inputMenu(['小麦パン', '白パン', 'サワー種'], prompt='パンを選んでください:\n', )
    protain = pyip.inputMenu(['チキン', 'ハム', 'ターキー', '豆腐'], prompt='タンパク質の種類を選んでください:\n',)
    cheese = pyip.inputYesNo(prompt = 'チーズは入れますか？\n', yesVal='yes', noVal='no', )
    if cheese == 'yes':
        cheese = pyip.inputMenu(['チェダー', 'スイス', 'モッツァレラ'], prompt='チーズの種類を選んでください:\n', )
    else:
        cheese = 'no'
    tomato = pyip.inputYesNo(prompt='トマトは入れますか？\n', yesVal='yes', noVal='no', )
    lettuce = pyip.inputYesNo(prompt='レタスは入れますか？\n', yesVal='yes', noVal='no', )
    mayo = pyip.inputYesNo(prompt='マヨネーズは入れますか？\n', yesVal='yes', noVal='no', )
    mustard = pyip.inputYesNo(prompt='マスタードは入れますか？\n', yesVal='yes', noVal='no', )

    count = pyip.inputInt(prompt='サンドイッチの数を入力してください:', min=1)

    total_price = 0
    total_price += bread_price[bread]
    total_price += protain_price[protain]
    if cheese == 'yes':
        total_price += cheese_prices[cheese]
    total_price += extra_price['トマト'] if tomato == 'yes' else 0
    total_price += extra_price['レタス'] if tomato == 'yes' else 0
    total_price += extra_price['マヨネーズ'] if tomato == 'yes' else 0
    total_price += extra_price['マスタード'] if tomato == 'yes' else 0

    total_price *= count

    print(f'注文内容は以下のとおりです:\n'
            f'パン: {bread}\n'
            f'タンパク質: {protain}\n'
            f'チーズ: {cheese}\n'
            f'トマト: {tomato}\n'
            f'レタス: {lettuce}\n'
            f'マヨネーズ: {mayo}\n'
            f'マスタード: {mustard}\n'
            f'サンドイッチの数: {count}\n'
            f'合計金額: {total_price}円\n'
            f'ありがとうございました')

if __name__ == '__main__':
        sandwich_maker()
