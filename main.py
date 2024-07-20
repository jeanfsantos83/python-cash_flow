import pandas as pd

class FluxoCaixa:
    def __init__(self):
        self.dados = pd.DataFrame(columns=['Data', 'Descricao', 'Entrada', 'Saida', 'Saldo'])

    def adicionar_transacao(self, data, descricao, entrada, saida):
        novo_registro = pd.DataFrame({'Data': [data], 'Descricao': [descricao], 'Entrada': [entrada], 'Saida': [saida], 'Saldo': [self.saldo_atual + entrada - saida]})
        self.dados = pd.concat([self.dados, novo_registro])
        self.dados['Saldo'] = self.dados['Entrada'].cumsum() - self.dados['Saida'].cumsum()

    def saldo_atual(self):
        return self.dados['Saldo'].iloc[-1] if not self.dados.empty else 0

    def relatorio_fluxo_caixa(self):
        print(self.dados)

    def relatorio_saldo_atual(self):
        print(f"Saldo atual: {self.saldo_atual()}")

def main():
    fluxo_caixa = FluxoCaixa()

    while True:
        print("Menu:")
        print("  1. Adicionar transação")
        print("  2. Relatório de fluxo de caixa")
        print("  3. Relatório de saldo atual")
        print("  4. Sair")
        opcao = input("Escolha uma opção: ")

        if opcao == "1":
            data = input("Digite a data da transação (DD/MM/YYYY): ")
            descricao = input("Digite a descrição da transação: ")
            entrada = float(input("Digite o valor de entrada: "))
            saida = float(input("Digite o valor de saída: "))
            fluxo_caixa.adicionar_transacao(data, descricao, entrada, saida)
            print("Transação adicionada com sucesso!")
        elif opcao == "2":
            fluxo_caixa.relatorio_fluxo_caixa()
        elif opcao == "3":
            fluxo_caixa.relatorio_saldo_atual()
        elif opcao == "4":
            print("Saindo do programa...")
            break
        else:
            print("Opção inválida. Tente novamente.")

if __name__ == "__main__":
    main()