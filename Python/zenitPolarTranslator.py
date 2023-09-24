def traduzir(mensagemOriginal):
    mensagemTraduzida = ''
    for letra in mensagemOriginal:
        match(letra):
            case 'z':
                mensagemTraduzida += 'p'
            case 'p':
                mensagemTraduzida += 'z'
            case 'e':
                mensagemTraduzida += 'o'
            case 'o':
                mensagemTraduzida += 'e'
            case 'n':
                mensagemTraduzida += 'l'
            case 'l':
                mensagemTraduzida += 'n'
            case 'i':
                mensagemTraduzida += 'a'
            case 'a':
                mensagemTraduzida += 'i'
            case 't':
                mensagemTraduzida += 'r'
            case 'r':
                mensagemTraduzida += 't'
                
            case 'Z':
                mensagemTraduzida += 'P'
            case 'P':
                mensagemTraduzida += 'Z'
            case 'E':
                mensagemTraduzida += 'O'
            case 'O':
                mensagemTraduzida += 'E'
            case 'N':
                mensagemTraduzida += 'L'
            case 'L':
                mensagemTraduzida += 'N'
            case 'I':
                mensagemTraduzida += 'A'
            case 'A':
                mensagemTraduzida += 'I'
            case 'T':
                mensagemTraduzida += 'R'
            case 'R':
                mensagemTraduzida += 'T'
    return mensagemTraduzida


print(traduzir(str(input('Digite a mensagem que irá ser traduzida: '))))