import socket

import time

def fuzz():
    
    server = raw_input("\n[*] Enter the FTP servers IP you would like to fuzz :\n>")

    user = raw_input("\n[*] Enter the FTP servers username:\n>")

    print "\n[*] Enter the password for FTP user %s:" % user

    userp = raw_input(">")

    print "\n[*] You entered %s. Please wait!\n" % server

    time.sleep(1)

    chars = ["A","B","C","D","E","F","G","H","I","J","K","L","M","N","O","P","Q","R","S","T","U","V","W","X","Y","Z","0","1","2","3","4","5","6","7","8","9"]

    chars += ["(",")","-","_","=","+","!","@","#","$","%","^","&","*","}","{",";",":",".","/","?","<",">","`","~","\n"] 

    fuzzData = [] # fuzz icin data	

    counter = 1

    add = 1

    while counter <= 150:

        for char in chars:

            fuzzData.append(char*add)

        add = add + 100

        counter = counter + 1

   
    cmds = ["user", "pass"]

    try: 

  

        for cmd in cmds:

            for element in fuzzData:

                print "\n[!] Fuzzing " + cmd + " with character " + element[0:1] + " with length " + str(len(element))

                time.sleep(.005)

                s=socket.socket(socket.AF_INET, socket.SOCK_STREAM)

                connect=s.connect((server,21))

                data = s.recv(1024)

                print "\n[*] Server Banner: %s" % data

                s.send("user " + user + "\r\n")

                data = s.recv(1024)

                print "[--] %s" % data

                s.send("pass " + userp + "\r\n")

                data = s.recv(1024)

                print "[--] %s" % data

                s.send(cmd + " " + element + "\r\n") 

                data = s.recv(1024)

                print "[--] %s" % data

                s.send("QUIT\r\n")

                s.close()

    except:

        print "\n[!!!!] Erorr try again. [!!!!]\n"

def main():

    print "\n[*] Welcome to the \"Cehennem\" Fuzzer!!!!! [*]\n"

    time.sleep(1)

    contin = ""

    while contin.lower() != "yes" and contin.lower() != "no":

        contin = raw_input("\n[*] Would you like to fuzz a FTP server?\n[*] Please type \"yes\" to continue or \"no\" to exit.[*]\n\n[*] hadi yes de?\n>")

        if contin == "no":

            print "\n[!!!!] Hmmm..Maybe another time [!!!!]\n"

        elif contin == "yes":

            fuzz()

        elif contin != "yes" and "no":

            print "\n\n[!!!!] You responded with %s. Please respond with yes or no! [!!!!]\n\n "% contin
   
if __name__ == "__main__":

    main() 
