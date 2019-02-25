while True:
    try:
        result = '''%s''' % input()
        print(result)
    except EOFError:
        break