cod_1, qtd_1, preco_unit_1 = input().split()

cod_2, qtd_2, preco_unit_2 = input().split()

qtd_1, qtd_2, preco_unit_1, preco_unit_2 = int(qtd_1), int(qtd_2), float(preco_unit_1), float(preco_unit_2)

print(f'VALOR A PAGAR: R$ {qtd_1 * preco_unit_1 + qtd_2 * preco_unit_2:.2f}')

