#!/usr/bin/env python
from socket import * 

if __name__ == '__main__':
    target = input('host girin: ')
    targetIP = gethostbyname(target)
    print ('Başladı ', targetIP)

    #scan reserved ports
    for i in range(1, 60000):
        s = socket(AF_INET, SOCK_STREAM)

        result = s.connect_ex((targetIP, i))

        if(result == 0) :
            print ('Port {}: OPEN'.format(i))
        s.close()
