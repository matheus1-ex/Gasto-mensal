nomeServico = input("Nome do serviço: ")
valorMensal = float(input("Digite o valor mensal: R$"))
DiasMes = int(input("Quantos dias no mês o serviço é usado: "))
#calculando...
GastoDiario = valorMensal / DiasMes
GastoSemanal = GastoDiario * 7
print(f"""Gasto por semana: R${GastoSemanal:.2f}
Gasto por dia: R${GastoDiario:.2f}""")
if GastoDiario > 6.0:
    print("Vale a pena: Não")
else:
    print("Vale a pena: SIM")

input("Pressione ENTER para sair...")