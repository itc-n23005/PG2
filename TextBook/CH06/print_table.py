def print_table(table_data):
    cols = len(table_data)
    col_width = [0] * cols
    for i in range(cols):
        col_width[i] = len(max(table_data[i], key=len))
    for i in range(4):
        for j in range(cols):
            print(table_data[j][i].rjust(col_width[j]) + ' ', end='')
        print('')

table_data = [
    ['apples', 'oranges', 'cherries', 'bananas'],
    ['Alice', 'Bob', 'Carol', 'David'],
    ['dogs', 'cats', 'moose', 'goose']
]

print_table(table_data)
