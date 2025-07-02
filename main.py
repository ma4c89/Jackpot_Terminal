import random
import time
from colorama import Fore, Style, init

init(autoreset=True)

simbolos = ["🍒", "🍋", "🍇", "⭐", "💎", "🔔"] * 3
pontos = 100
modo_facil = False  # trapaça desligada inicialmente

def menu():
    print(Fore.YELLOW + "📜 INFORMAÇÕES DO JOGO")
    print(Fore.YELLOW + "→ Você começa com 100 créditos.")
    print(Fore.YELLOW + "→ Cada rodada custa 10 créditos.")
    print(Fore.YELLOW + "→ Você ganha 20 créditos se acertar 2 símbolos iguais.")
    print(Fore.YELLOW + "→ Você ganha 50 créditos se fizer JACKPOT (3 símbolos iguais).")
    print(Fore.YELLOW + "→ Se o seu saldo chegar a 0, o jogo acaba.")
    print(Fore.LIGHTMAGENTA_EX + "💡 Dica: Existe um código secreto escondido...")
    print()

def sair():
    global modo_facil
    comando = input(Fore.YELLOW + "Digite 'sair' para encerrar, ou pressione Enter para continuar: ").strip().lower()
    if comando == "sair":
        print(Fore.YELLOW + "\n🎮 Jogo encerrado. Até a próxima!")
        return True
    elif comando == "banana":
        modo_facil = not modo_facil
        status = "ativado" if modo_facil else "desativado"
        print(Fore.LIGHTGREEN_EX + f"\n💥 Modo TRAPAÇA {status}! Suas chances de vitória {'aumentaram' if modo_facil else 'voltaram ao normal'}!")
        time.sleep(2)
        return False
    return False

while True:
    menu()
    print(Fore.YELLOW + "🎰 BEM-VINDO À MÁQUINA CAÇA-NÍQUEL 🎰")
    print(Fore.CYAN + f"💰 Créditos disponíveis: {pontos}")

    if pontos <= 0:
        print(Fore.RED + "\n⚠️ Você ficou sem créditos. FIM DE JOGO!")
        break

    if sair():
        break

    input(Fore.YELLOW + "Pressione Enter para girar os símbolos...")

    pontos -= 10

    if modo_facil:
        chance = random.randint(1, 100)
        if chance <= 25:
            simbolo = random.choice(simbolos)
            a = b = c = simbolo
        elif chance <= 65:
            a = b = random.choice(simbolos)
            c = random.choice([s for s in simbolos if s != a])
        else:
            a, b, c = random.choices(simbolos, k=3)
    else:
        a, b, c = random.choices(simbolos, k=3)

    for _ in range(5):
        a, b, c = random.choices(simbolos, k=3)
        print(Fore.YELLOW + "\n🎰 Girando...")
        print(f"|  {a}  |  {b}  |  {c}  |")
        time.sleep(1)

    print(Fore.YELLOW + "\n🎯 Resultado:")
    if a == b == c:
        print(Fore.GREEN + "🏆 JACKPOT!!! Você ganhou 50 créditos!")
        pontos += 50
    elif a == b or b == c or a == c:
        print(Fore.BLUE + "🌟 Parabéns! Você acertou dois símbolos e ganhou 20 créditos.")
        pontos += 20
    else:
        print(Fore.RED + "🙁 Não foi dessa vez. Tente novamente!")

    time.sleep(2)
