def voto(ano):
    from datetime import date
    atual = date.today().year
    idade = atual - ano
    if idade < 16:
        return f"Com essa idade {idade}, não vota"
    elif 16 <= idade <18 or idade > 65:
        return f"Com essa idade {idade}, voto opcional"
    else:
        return f"Com essa idade {idade}, voto obrigatorio"
print(voto(2010))

    