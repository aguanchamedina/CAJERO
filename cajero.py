print("-----------------------------------------------")
print("-------------PROGRAMA CENTINELA BANCO----------")
print("-----------------------------------------------")


#INPUT
cheque = int(input("Ingrese el valor del cheque: "))

total_bill_10000 = 0
total_bill_2000 = 0
total_mon_100 = 0

#PROCESS 
while cheque != 0:
    if cheque % 100 == 0:
        bill_10000= cheque//10000
        bill_2000= cheque%10000
        bill_2000= bill_2000// 2000
        mon_100= cheque%2000
        mon_100= mon_100//100 
        
        print("El cheque de" + str(cheque) + " equivale a: ")
        print("Billetes de 10000 " + str(bill_10000))
        print("Billetes de 2000: " + str(bill_2000))
        print("Monedas de 100:  " + str(mon_100))
        total_bill_10000= total_bill_10000 + bill_10000
        total_bill_2000= total_bill_2000 + bill_2000
        total_mon_100= total_mon_100 + mon_100
    
    else:
        print("Sr. cliente, ese cheque no se puede cambiar")
    cheque = int(input("Ingrese el valor del cheque: "))

print("BALANCE DEL DIA: ")
print(" Total de billetes de 10000: "+ str(total_bill_10000))
print(" Total de billetes de 2000: "+ str(total_bill_2000))
print(" Total de billetes de 10000: "+ str(total_mon_100))
print("Eso fue todo :) ....")

#OUTPUT