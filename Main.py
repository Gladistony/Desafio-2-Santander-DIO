def calcular_rank(saldo_vitorias):
    if saldo_vitorias < 10:
        nivel = "Ferro"
    elif 11 <= saldo_vitorias <= 20:
        nivel = "Bronze"
    elif 21 <= saldo_vitorias <= 50:
        nivel = "Prata"
    elif 51 <= saldo_vitorias <= 80:
        nivel = "Ouro"
    elif 81 <= saldo_vitorias <= 90:
        nivel = "Diamante"
    elif 91 <= saldo_vitorias <= 100:
        nivel = "Lendário"
    else:
        nivel = "Imortal"
    return nivel

def main():
    vitorias = 0
    derrotas = 0
    while True:
        temp1 = input("Digite o número de vitórias: ")
        temp2 = input("Digite o número de derrotas: ")
        if "+" in temp1:
            vitorias += int(temp1.replace("+", ""))
        elif "-" in temp1:
            vitorias -= int(temp1.replace("-", ""))
        else:
            vitorias = int(temp1)
        if "+" in temp2:
            derrotas += int(temp2.replace("+", ""))
        elif "-" in temp2:
            derrotas -= int(temp2.replace("-", ""))
        else:
            derrotas = int(temp2)
        saldo_vitorias = vitorias - derrotas
        print(f"O Herói tem de saldo de {saldo_vitorias} está no nível de {calcular_rank(saldo_vitorias)}")
        continuar = input("Deseja continuar? (S/N): ")
        if continuar.upper() == "N":
            break

main()