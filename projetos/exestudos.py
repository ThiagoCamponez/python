chuveiro_eletr = 3 * 1
freezer = 0.2 * 24
geladeira = 0.25 * 24
lampada = 0.12 * 5

consumo_mes = 30 #kWh
valor_kwh = 0.30 #R$

cons_mes_chuv = chuveiro_eletr * consumo_mes
cons_mes_free = freezer * consumo_mes
cons_mes_geladeira = geladeira * consumo_mes
cons_mes_lampada = lampada * consumo_mes
total_kw_mes = cons_mes_geladeira + cons_mes_free + cons_mes_chuv + cons_mes_lampada
total_valor_mes = total_kw_mes * valor_kwh

print('O chuveiro-elétrico consumiu {}kW no mês.'.format(cons_mes_chuv))
print('O freezer consumiu {:.2f}kW no mês.'.format(cons_mes_free))
print('A geladeira consumiu {}kW no mês.'.format(cons_mes_geladeira))
print('A lampada consumiu {}kW no mês.'.format(cons_mes_lampada))
print('Seus equipamentos consumiram {}kW no mês, então deverá pagar R${} de energia elétrica.'.format(total_kw_mes, total_valor_mes))