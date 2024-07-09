# Exercicio - Jogo da palavra secreta

"""
Faça um jogo para o usuário adivinhar qual
a palavra secreta.
- Você vai propor uma palavra secreta
qualquer e vai dar a possibilidade para
o usuário digitar apenas uma letra.
- Quando o usuário digitar uma letra, você 
vai conferir se a letra digitada está
na palavra secreta.
    - Se a letra digitada estiver na
    palavra secreta; exiba a letra;
    - Se a letra digitada não estiver
    na palavra secreta; exiba *.
Faça a contagem de tentativas do seu
usuário.
"""

palavra_secreta = 'agua'
repeticoes = 0
letras_acertadas = ''

while True:

    letra  = input(f'Digite uma letra da palavra secreta ({repeticoes}x): ')
    repeticoes += 1

    if len(letra) > 1:
        print('Digite apenas uma letra')

    #guardar todas a letras que foram acertadas
    if letra in palavra_secreta:
        letras_acertadas += letra
    
    #formar a palavra p quando for igual a secreta sair do while
    palavra_formada = ''

    # percorrer cada letra da palavra secreta e ver se as que foram acertadas estao nela
    for letra_secreta in palavra_secreta:
        if letra_secreta in letras_acertadas:
            print(letra_secreta)
            palavra_formada += letra_secreta
        else:
            print('*')
    
    if palavra_formada == palavra_secreta:
        break
    
print('PARABENS voce acertou, a palavra é: Agua.')