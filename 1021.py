valor = eval(input());

n100 = n50 = n20 = n10 = n5 = n2 = n1 = 0;
m50 = m25 = m10 = m5 = m1 = 0;

valor = float("%.2f" % valor)
if int(valor/100) >= 1:
	n100 = int(valor/100);
	valor -= n100*100;

valor = float("%.2f" % valor)
if int(valor/50) >= 1:
	n50 = int(valor/50);
	valor -= n50*50;

valor = float("%.2f" % valor)
if int(valor/20) >= 1:
	n20 = int(valor/20.00);
	valor -= n20*20;

valor = float("%.2f" % valor)
if int(valor/10) >= 1:
	n10 = int(valor/10);
	valor -= n10*10.00;

valor = float("%.2f" % valor)
if int(valor/5) >= 1:
	n5 = int(valor/5);
	valor -= n5*5;

valor = float("%.2f" % valor)
if int(valor/2) >= 1:
	n2 = int(valor/2);
	valor -= n2*2;

valor = float("%.2f" % valor)
if int(valor/1) >= 1:
	n1 = int(valor/1);
	valor -= n1*1;

valor = float("%.2f" % valor)
if int(valor/0.50) >= 1:
	m50 = int(valor/0.50);
	valor -= m50*0.50;

valor = float("%.2f" % valor)
if int(valor/0.25) >= 1:
	m25 = int(valor/0.25);
	valor -= m25*0.25;

valor = float("%.2f" % valor)
if int(valor/0.10) >= 1:
	m10 = int(valor/0.10);
	valor -= m10*0.10;

valor = float("%.2f" % valor)
if int(valor/0.05) >= 1:
	m5 = int(valor/0.05);
	valor -= m5*0.05;

valor = float("%.2f" % valor)
if int(valor/0.01) >= 0.998:
	m1 = int(valor/0.01);
	valor -= m1*0.01;

print("NOTAS:");
print("%d nota(s) de R$ 100.00" % n100);
print("%d nota(s) de R$ 50.00" % n50);
print("%d nota(s) de R$ 20.00" % n20);
print("%d nota(s) de R$ 10.00" % n10);
print("%d nota(s) de R$ 5.00" % n5);
print("%d nota(s) de R$ 2.00" % n2);

print("MOEDAS:");
print("%d moeda(s) de R$ 1.00" % n1);
print("%d moeda(s) de R$ 0.50" % m50);
print("%d moeda(s) de R$ 0.25" % m25);
print("%d moeda(s) de R$ 0.10" % m10);
print("%d moeda(s) de R$ 0.05" % m5);
print("%d moeda(s) de R$ 0.01" % m1);