def number_transformer(inp: str) -> str:
    phone_number = ''.join([c for c in inp if c.isdigit()])
    if len(phone_number) == 7:
        phone_number = '8495' + phone_number
    if phone_number.startswith('7'):
        phone_number = '8' + phone_number[1:]
    return phone_number


inp_added_number = input()
add_number = number_transformer(inp_added_number)
for i in range(3):
    inp_number = input()
    number = number_transformer(inp_number)
    if number == add_number:
        print('YES')
    else:
        print('NO')
