#Lunes - nivel inicial
#Martes - nivel intermedio
#Miercoles - nivel avanzado
#NO TIENEN EXAMENES:
#Jueves - práctica hablada
#Viernes - inglés para viajeros

#solicita fecha actual, formato "dia,DD/MM"
date=input("Ingrese la fecha atual: ")
week_days=["lunes","martes","miercoles","jueves","viernes"]
day_of_week=date[0:date.find(',')]
day_of_week=day_of_week.lower()
day=int(date[date.find(' ')+1:date.find("/")])
month=int(date[date.find('/')+1:])
print(day_of_week," dia: ", day," mes: ",month)
flag=True
if (day_of_week in week_days)==False:
  print("el dia no es corecto")
  flag=False
else:
  if month<1 or month>12:
    print("el mes no es corecto")
    flag=False
  else:
    #el mes es correcto, veificamos que el dia este dentro del mes
    #31: 01/03/05/07/08/10/12
    #30: 04/06/09/11
    #28:02
    if day>31 or day<0:
      print("dia incorrecto")
      flag=False
    else:
      if month==4 or month==6 or month==9 or month==11:
        if day>30:
          print("dia incorecto")
          flag=False
      elif month==2:
        if day>28:
          print("dia incorecto")
          flag=False

##validaos que sea lunes/martes o miercoles

if flag==True:
  if day_of_week=="jueves": 
    print("#Practica hablada")
    assistance=int(input("ingrese el porcentaje de asistenica: "))
    if assistance>50:
      print("Asistió la mayoría")
    else:
      print("No asistió la mayoría")
      
  elif day_of_week=="viernes": 
    print("Ingles para viajeros")
    if month==1 or month==7:#comienzo de ciclo
      if day==1:
        print("COMIENZO DE NUEVO CICLO!!")
        n_student=int(input("Ingrese la cantidad de alumnos: "))
        price=int(input("ingrese el arancel de cada alumno: $"))
        print("Ingreso total: $",(price*n_student))
  else:
    approved=int(input("Ingrese la cantidad de alumnos aprobados: "))
    disappoved=int(input("Ingrese la cantidad de alumnos desaprobados: "))
    total_al=approved+disappoved
    #10 aprovados, 4 desaprovados
    percentage_pass=int((approved*100)/total_al)
    print(f"el porcentaje de aprobados fue de: {percentage_pass}%")