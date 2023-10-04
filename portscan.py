import socket

ports = []
while True:
    option = input("Start Scan? Y/N: ")
    if option == "Y" or option == "y":
        while True:
            port = int(input("Insert the port: "))
            ports.append(port)
            answ = input("Add more ports? Y/N: ")
            if answ == "N" or answ == "n":
                break
            elif answ != "N" and answ != "n" and answ != "Y" and answ != "y":
                print("Incorrect option!")
        for port in ports:
            client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            client.settimeout(1)
            code = client.connect_ex(("dominio-exemplo.com", port))
            if code == 0:
                print(f"{port}: Open")
            else:
                print(f"{port}: Closed")
    elif option == "N" or option == "n":
        print("Finalizing program...")
        exit()
    else:
        print("Incorrect option!")
    break
