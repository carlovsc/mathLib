class BibliotecaArrays:
    def max(self, x):
        if not x: return None
        max_val = x[0]
        for val in x:
            if val > max_val:
                max_val = val
        return float(max_val)

    def min(self, x):
        if not x: return None
        min_val = x[0]
        for val in x:
            if val < min_val:
                min_val = val
        return float(min_val)

    def size(self, x):
        count = 0
        for _ in x:
            count += 1
        return count

    def average(self, x):
        n = self.size(x)
        if n == 0: return 0.0
        soma = 0.0
        for val in x:
            soma += val
        return soma / n

    def std_dev(self, x):
        n = self.size(x)
        if n <= 1: return 0.0
        media = self.average(x)
        soma_quadrados = 0.0
        for val in x:
            soma_quadrados += (val - media) ** 2
        # Cálculo da variância e raiz quadrada manual (aproximação)
        variancia = soma_quadrados / n
        return variancia ** 0.5

    def sort(self, x, type="asc"):
        n = self.size(x)
        # Cria uma cópia para não alterar o original
        resultado = [val for val in x]
        # Implementação de Bubble Sort
        for i in range(n):
            for j in range(0, n - i - 1):
                if type == "asc":
                    if resultado[j] > resultado[j + 1]:
                        resultado[j], resultado[j+1] = resultado[j+1], resultado[j]
                else: # desc
                    if resultado[j] < resultado[j + 1]:
                        resultado[j], resultado[j+1] = resultado[j+1], resultado[j]
        return resultado

    def reverse(self, x):
        resultado = []
        n = self.size(x)
        for i in range(n - 1, -1, -1):
            resultado.append(x[i])
        return resultado