faturamento = {
    'sp': 67836.43,
    'rj': 36678.66,
    'mg': 29229.88,
    'es': 27165.48,
    'outros': 19849.53
}

faturamentoTotal = sum(faturamento.values())

for estado, valor in faturamento.items():
    percentual = valor / faturamentoTotal * 100
    print(f'{estado}: {percentual:.2f}%')