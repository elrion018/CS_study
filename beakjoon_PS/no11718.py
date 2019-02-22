
while True:
    try:
        in_put = input()
        result = '''%s''' % in_put
        print(result)
    except EOFError:
        break