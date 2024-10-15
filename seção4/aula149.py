# Try e Except para tratar excecoes

try:
    a = 10
    b = 0
    print(b[0])
    c = a/b
    print(c)
    print(b[0])
except ZeroDivisionError:
    print('you divided by zero')
# as error vai pegar qual foi o erro
# as é como criar uma var e error é o nome dessa var
except (TypeError, IndexError) as error:
    print('Type error + IndexError')
    print('MSG:', error)
    #saber se foi TypeError e IndexError
    print('Name:', error.__class__.__name__)

except NameError as a:
    print(a)
except Exception:
    print('unknow error')

