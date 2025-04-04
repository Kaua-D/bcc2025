import sys

def classificar_velocidade(velocidade):
    if velocidade < 10:
        return 1
    elif 10 <= velocidade < 20:
        return 2
    else:
        return 3

def main():
    for linha in sys.stdin:
        L = int(linha.strip())
        velocidades = list(map(int, sys.stdin.readline().strip().split()))
        
        # Encontrar a velocidade máxima
        velocidade_maxima = max(velocidades)
        
        # Classificar a velocidade máxima
        nivel = classificar_velocidade(velocidade_maxima)
        
        # Imprimir o nível
        print(nivel)

if __name__ == "__main__":
    main()