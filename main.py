import sympy as sp
import pandas as pd
from IPython.display import display


class MetodoBissecao:

    def __init__(self, a, b, precisao, funcao):
        """Atributos necessarios para inicializar a classe"""
        self.a = a
        self.b = b
        self.precisao_usuario = precisao
        self.funcao = funcao

    def _calcular_funcao(self, funcao, x_valor):
        """Recebe a string de uma função e transforma na função
        É usado apenas no método final"""
        x = sp.Symbol('x')
        funcao = sp.sympify(funcao)
        resultado = funcao.subs(x, x_valor)
        return round(float(resultado), 5)

    def _calcular_Xi(self, a, b):
        """Calcula Xi"""
        try:
            xi = (a + b) / 2
            return xi
        except:
            print("Erro ao calcular xi")

    def _calcular_precisao_final(self, a, b):
        """"Calula precisao final"""
        precisao_final = b - a
        return precisao_final

    def metodo_bissecao(self):
        a = self.a
        b = self.b
        iteracoes = []
        contador = 0

        while True:
            contador += 1
            xi = self._calcular_Xi(a, b)
            f_a = self._calcular_funcao(self.funcao, a)
            f_b = self._calcular_funcao(self.funcao, b)
            f_xi = self._calcular_funcao(self.funcao, xi)
            precisao_final = self._calcular_precisao_final(a, b)
            iteracoes.append([contador, a, b, xi, f_a, f_b, f_xi, precisao_final])

            if f_a * f_xi < 0:
                b = xi
            elif f_b * f_xi < 0:
                a = xi
            else:
                print("Erro no programa. Multiplicações deram positivo.")
                break

            if self.verificar_precisao(precisao_final, self.precisao_usuario):
                break

        return iteracoes, f_xi, contador

    def verificar_precisao(self, precisao_final, precisao_usuario):
        return precisao_final <= precisao_usuario


def main():
    A = float(input("Informe o valor de A: "))
    B = float(input("Informe o valor de B: "))
    precisao = str(input("Informe a precisão desejada: "))
    precisao = precisao.replace(",", ".")
    precisao = float(precisao)
    funcao = input("Informe a função f(x): ")
    trabalho = MetodoBissecao(A, B, precisao, funcao)
    iteracoes, valor_final, total_iteracoes = trabalho.metodo_bissecao()
    df = pd.DataFrame(iteracoes, columns=['Iteração', 'A', 'B', 'Xi', 'f(A)', 'f(B)', 'f(Xi)', 'Precisão'])
    display(df)
    print(f"\nPrecisão atingida após {total_iteracoes} iterações.")
    print(f"O valor final aproximado da F(x{total_iteracoes}) = {valor_final}")


if __name__ == "__main__":
    main()
