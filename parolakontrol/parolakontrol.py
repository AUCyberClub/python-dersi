current_psw="Abcde12345."
psswd = input("Password:")
if(len(psswd)<8 or len(psswd)>16):
    psswd = input("Invalid form!! Try new psswd:")
if (psswd != current_psw):
    psswd = input("It's too easy!! Try new psswd:")

else:
    print("DONE!")
