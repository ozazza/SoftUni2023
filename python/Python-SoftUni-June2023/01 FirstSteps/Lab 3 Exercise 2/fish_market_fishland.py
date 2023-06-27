price_scumria = float(input())
price_caca = float(input())
kg_palamud = float(input())
kg_safrid = float(input())
kg_scallops = float(input())

price_palamud = price_scumria + (price_scumria * 0.6)
praice_safrid = price_caca + (price_caca * 0.8)

scallops = kg_scallops * 7.50
palamud =kg_palamud * price_palamud
safrid = kg_safrid * praice_safrid

amount = scallops + palamud + safrid

print(f'{amount:.2f}')