frase = str(input("Digite uma frase: ")).strip().lower()
if "a" in frase:
    print(f"A letra 'A' aparece {frase.count('a')} vezes na frase")
    print(f"Posição da primeira letra 'A': {frase.find('a')+1}")
    print(f"Posição da última letra 'A': {frase.rfind('a')+1}")