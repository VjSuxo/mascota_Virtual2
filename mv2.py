def hambre(cart):
    if cart[1]<10.0:
        cart[1]=cart[1]+1.5       
    if cart[4] > 0:
        cart[4]=cart[4]-0.5
        if int(cart[4])<=0:
            print("=====================================")
            print("=     Su mascota esta muy sucia     =")
            print("=====================================")
           
    if int(cart[1])>=10:

        print("=====================================")
        print("=     Su mascota esta llena         =")
        print("=====================================")

    menu(cart)
def sueño(cart):
    if int(cart[2])<10:
        cart[2]=cart[2]+2
    if int(cart[1])>0:
        cart[1]=cart[1]-1.5
        if int(cart[1])<=0:
            print("=====================================")
            print("=  Su mascota tiene mucha hambre    =")
            print("=====================================")
    if (int(cart[2])>=10):

        print("=====================================")
        print("=   Su mascota  ya durmio bastante  =")
        print("=====================================")         
    menu(cart)

def divercion(cart):
    if int(cart[3])<10:
        cart[3]=cart[3]+3
    if int(cart[1])>0:
        cart[1]=cart[1]-2.5
        if int(cart[1])<=0:
            print("=====================================")
            print("=   Su mascota tiene mucha hambre   =")
            print("=====================================")
    if cart[2]>0:
        cart[2]=cart[2]-1.5
        if int(cart[2])<=0:
            print("=====================================")
            print("=  Su mascota tiene mucha hambre    =")
            print("=====================================")
    if cart[4]>0: 
        cart[4]=cart[4]-2.5
        if int(cart[4])<=0:
            print("=====================================")
            print("=     Su mascosa esta muy sucia    =")
            print("=====================================")
    if int(cart[3])>=10:
        print("=====================================")
        print("=   Su mascota ya no quiere jugar   =")
        print("=====================================")
    menu(cart)

def limpieza(cart):
    if int(cart[4])<10:
        cart[4]=cart[4]+1.5
        if int(cart[2])<=0:
            print("=====================================")
            print("=  Su mascota tiene mucha hambre    =")
            print("=====================================")
    if int(cart[2])>0:
        cart[2]=cart[2]-0.5

    if int(cart[4])>=10:
            print("=====================================")
            print("=     Su mascota esta brillando     =")
            print("=====================================")
    menu(cart)

def dibujar(cart):

    BH = ""
    BS = ""
    BD = ""
    Bs = ""
    x = cart[1]

    for i in range (int(x)):
        
        if(cart[1]==(i+0.5)):

            BH = BH+"-"

        else:    

            BH = BH + "|"

    x = cart[2]    
    for i in range (int(cart[2])):
        
        if (cart[2]==(i+0.5)):

            BS = BS+"-"
        else:    

            BS = BS + "|"
    
    x = cart[3]    

    for i in range (int(cart[3])):
        
        if(cart[3]==(i+1+0.5)):

            BD = BD+"-"
        else:    

            BD = BD + "|"
    
    x = cart[4]
    
    for i in range (int(cart[4])):
        
        if(cart[4]==(i+1+0.5)):

            Bs = Bs +  "-"
        else:    
            Bs = Bs + "|"
                

    print("Hambre ",BH)
    print("Sueño  ",BS)
    print("Diver  ",BD)
    print("Baño   ",Bs)

def menu(cart):

    sele=1
    salir = True
    dibujar(cart)
    while salir:
        print("[1] alimentar mascota","[2] Dormir mascota","[3] Jugar mascota","[4] Bañar mascota","[0] Salir")
        
        sele=int(input())
        
        
        if sele==1:
            hambre(cart)
            break
        if sele==2:
            sueño(cart)
            break
        if sele==3:
            divercion(cart)
            break        
        if sele==4:
            limpieza(cart)
            break
        if sele==" ":
            sele=6
            break   
        if sele==0:
            print("--------------------------------------------------------------------------------------------------------------")
            print("--------------------------------------------------------------------------------------------------------------")
            print("--   **************  ***********      ***********  **************  ****  ************  **************       --")
            print("--   **************  ***      ****    ***********  **************  ****  ************  **************       --")
            print("--   ****            ***        ***   ***     ***  ***             ****  ***      ***  ****                 -- ")
            print("--   ****   *******  ***         **   ***     ***  ***             ****  ***      ***  ****                 --")
            print("--   ****   *******  *************    ***********  ***             ****  ************  **************       --")
            print("--   ****     *****  ***       ***    ***     ***  ***             ****  ***      ***            ****       --")
            print("--   **************  ***         ***  ***     ***  *************   ****  ***      ***  **************       --")
            print("--   **************  ***         ***  ***     ***  *************   ****  ***      ***  **************       --")
            print("--------------------------------------------------------------------------------------------------------------")
            print("--------------------------------------------------------------------------------------------------------------")
            salir=False
            break    




cart=[5,5,5,5,5]
menu(cart)
