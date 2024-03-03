cod_1, qtd_1, preco_unit_1 = input().split()

cod_2, qtd_2, preco_unit_2 = input().split()

qtd_1_int = int(qtd_1)
qtd_2_int = int(qtd_2)
preco_unit_1_float = float(preco_unit_1)
preco_unit_2_float = float(preco_unit_2)
valor = qtd_1_int * preco_unit_1_float + qtd_2_int * preco_unit_2_float
print(f'VALOR A PAGAR: R$ {valor:.2f}')
