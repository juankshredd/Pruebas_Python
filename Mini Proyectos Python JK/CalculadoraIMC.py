def imc():
	x = int(input("ingrese su peso en kilos: "))
	y = float(input("ingrese su altura en metros: "))
	i = x/(y**2)
	if i < 18.5:
		m = 'bajo peso'
		print("tu IMC es {i}, tu estado actual es {m}")
	elif i >=18.5 and i <=24.9:
		m = 'peso normal'
		print(f"tu IMC es {i}, tu estado actual es {m}")
	elif i >= 25 and i <= 29.9:
		m = 'sobrepeso'
		print(f"tu IMC es {i}, tu estado actual es {m}")
	else:
		m= 'obesidad'
		print(f"tu IMC es {i}, tu estado actual es {m}")
imc()