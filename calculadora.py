def division(num1, num2):
    
    if num2 == 0:
        
        return "Error: División por cero"

    div = num1 % num2
   
    return(div)

def suma(num1, num2):
    
    suma = num1 + num2 
    
    return(suma)

def resta(resta1, resta2):
    
    resta = resta1 - resta2
    
    return(resta)

def multiplicar(num1, num2):

    multi = num1 * num2
    
    return(multi)

def potencia(num1, num2):

    potencia = num1 ** num2
    
    return(potencia)

while True:
    
    print("\nBienvenido a la calculadora :D\n")
    
    print("1 para suma\n2 para resta\n3 para multiplicar\n4 para division\n5 para potenciacion\n6 para salir\n")
    
    usuario = input("> ")

    try:

        if usuario == "1":
            
            print("\ningrese 2 valores\n")
            
            num1 = float(input())
            num2 = float(input())      
            
            print("\nEl resultado de la suma es:\n")
            print(suma(num1, num2))
        
        if usuario == "2":
            
            print("\ningrese 2 valores\n")
            
            num1 = float(input())
            num2 = float(input()) 
            
            print("\nEl resultado de la resta es:\n")
            print(resta(num1, num2))
        
        if usuario == "3":

            print("\ningrese 2 valores\n")
            
            num1 = float(input())
            num2 = float(input())  

            print("\nEl resultado de la multiplicacion es:\n")
            print(multiplicar(num1, num2))
        
        elif usuario == "4":
            
            print("\ningrese 2 valores\n")
            
            num1 = float(input())
            num2 = float(input())  

            print("\nEste es el resultado de la division:\n")
            print(division(num1, num2))

        elif usuario == "5":
            
            try:
                print("\ningrese 2 valores\n")
                num1 = float(input())
                num2 = float(input()) 
                
                print("\nEste es el resultado de la potenciacion:\n")
                print(potencia(num1, num2))
            
            except OverflowError:
                
                print("\nEl numero es muy grande como para calcular :(\n")
        
        elif usuario == "6":

            break
        
        else:
            
            continue
    
    except ValueError:
        
        print("\nSolo aceptamos numeros")
