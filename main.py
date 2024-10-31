import sympy as sp
import pandas as pd
from IPython.display import display


class MetodoBissecao:
    def __init__(self, A, B, precisao, funcao):
        self.a = A
        self.b = B
        self.precisao_usuario = precisao
        self.funcao = funcao
        self.x = sp.Symbol('x')

    def calcular_funcao(self, x_valor):
        try:
            funcao = sp.sympify(self.funcao)
            return funcao.subs(self.x, x_valor)
        except Exception as e:
            print(f"Erro ao calcular a função em x = {x_valor}: {e}")
            return None

    def _calcular_Xi(self, a, b):
        return (a + b) / 2

    def _calcular_precisao_final(self, a, b):
        return b - a

    def metodo_bissecao(self):
        a = self.a
        b = self.b
        iteracoes = []
        contador = 0

        f_a = self.calcular_funcao(a)
        f_b = self.calcular_funcao(b)

        if f_a is None or f_b is None:
            print("Erro ao calcular f(A) ou f(B). Verifique a função e os valores de A e B.")
            return None, None, None

        if f_a * f_b > 0:
            print("Erro: f(A) e f(B) devem ter sinais opostos para que o método da bisseção funcione.")
            return None, None, None

        while True:
            contador += 1
            xi = self._calcular_Xi(a, b)
            f_xi = self.calcular_funcao(xi)
            precisao_final = self._calcular_precisao_final(a, b)

            if f_xi is None:
                print(f"Erro ao calcular f(Xi) na iteração {contador}. Verifique a função.")
                return None, None, None

            iteracoes.append([contador, a, b, xi, f_a, f_b, f_xi, precisao_final])

            if f_a * f_xi < 0:
                b = xi
                f_b = f_xi
            elif f_b * f_xi < 0:
                a = xi
                f_a = f_xi
            else:
                print("Erro no programa. Multiplicações deram positivo, o que indica falta de mudança de sinal.")
                return None, None, None

            if self.verificar_precisao(precisao_final, self.precisao_usuario):
                break

        return iteracoes, xi, contador

    def verificar_precisao(self, precisao_final, precisao_usuario):
        return precisao_final <= precisao_usuario


def main():
    try:
        A = float(input("Informe o valor de A: "))
        B = float(input("Informe o valor de B: "))

        precisao_input = input("Informe a precisão desejada: ")
        precisao = float(precisao_input.replace(',', '.'))
        if precisao <= 0:
            print("Erro: A precisão deve ser um número positivo.")
            return

        funcao = input("Informe a função f(x): ")
        trabalho = MetodoBissecao(A, B, precisao, funcao)
        iteracoes, valor_final, total_iteracoes = trabalho.metodo_bissecao()

        if iteracoes is None:
            print("Erro: Não foi possível completar o método da bisseção devido a problemas nos parâmetros ou na função.")
            return

        df = pd.DataFrame(iteracoes, columns=['Iteração', 'A', 'B', 'Xi', 'f(A)', 'f(B)', 'f(Xi)', 'Precisão'])
        display(df)
        print(f"\nPrecisão atingida após {total_iteracoes} iterações.")
        print(f"O valor final aproximado da raiz é: {valor_final}")

    except ValueError:
        print("Erro: Verifique se A, B e precisão são números válidos e se a função é válida.")
    except Exception as e:
        print(f"Ocorreu um erro inesperado: {e}")
