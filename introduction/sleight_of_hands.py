def read_data():
    k = int(input())
    matrix = f'{input()}{input()}{input()}{input()}'
    return k, matrix


def solutions(k, matrix, line='0123456789'):
    result = sum(0 < matrix.count(i) <= k * 2 for i in line)
    print(result)


if __name__ == '__main__':
    k, matrix = read_data()
    solutions(k, matrix)
