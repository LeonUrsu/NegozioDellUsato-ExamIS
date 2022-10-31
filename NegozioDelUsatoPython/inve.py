p = 0.015  # 1.5%
gg = 5
i = 82.02 + 98 + 7.35
tot = i
mesi = 12
precedente = 0
percentualePrelievo = 1/10
prelevato = 0
totPrelevato = 0
for x in range(6 * mesi):
    tot += tot * p * gg
    prelevato = (tot - precedente) * percentualePrelievo
    if tot >= 500:
        tot -= prelevato
        totPrelevato += prelevato
    print(f"giorno {(x + 1) * 5} --> {tot}")
    precedente = tot
print(f"tot prelevato {totPrelevato}" )
print(f"investimento : {i}")