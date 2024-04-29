def verificar_clima():
    clima = input("Como está o clima hoje? (Bom/Ruim): ").lower()
    if clima == "bom":
        print("Ótimo! Vá para a praia!")
    elif clima == "ruim":
        print("Que pena! Fique em casa.")
    else:
        print("Desculpe, não entendi a sua resposta.")

verificar_clima()
