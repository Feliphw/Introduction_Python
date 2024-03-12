s = int(input("Digite o salario do colaborador: "))
   
if s <= 1903.98:
    print("Isento, não há redução salarial.")
elif s > 1903.98 and s <= 2826.65: 
  r = s * 7.5 / 100
  sf = s - r
  print(f"Dedução em reais {s} sera de R$ {r}.")
  print(f"O colabroador recebera: {sf}")
elif s > 2826.66 and s <= 3751.05:
   r = (s * 15) / 100 
   sf = s - r
   print(f"Dedução em reais {s} sera de R$ {r}.")
   print(f"O colabroador recebera: {sf}")
elif s > 3751.06 and s <= 4664.68:
   r = (s * 22.5) / 100 
   sf = s - r
   print(f"Deduç
   ão em reais {s} sera de R$ {r}.")
   print(f"O colabroador recebera: {sf}")
elif s > 4664.68:
  r = s * 27.5 / 100
  sf = s - r
  
  print(f"Dedução em reais {s} sera de R$ {r}.")
  print(f"O colabroador recebera: {sf}")

else:
   print("Salario digitado incorretamente")
 