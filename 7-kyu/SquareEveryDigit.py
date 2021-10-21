def square_digits(num):
    final_num = ""

    for n in str(num):
        x = int(n)**2
        final_num += f"{x}"
    return int(final_num)


a = square_digits(912)
print(a)
