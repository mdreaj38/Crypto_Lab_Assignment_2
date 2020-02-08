c1 = [0xe9, 0x3a, 0xe9, 0xc5, 0xfc, 0x73, 0x55, 0xd5]
c2 = [0xf4, 0x3a, 0xfe, 0xc7, 0xe1, 0x68, 0x4a, 0xdf]
c1_c2 = [i^j for i,j in zip(c1,c2)]

my_file = open('/usr/share/dict/words', 'r')
all_string = my_file.read().split()
store  = [' ']
for i in all_string:
    if(len(i)==8):
        store.append(i)
for i in store:
    message_1 = [ord(j) for j in i]
    message_2 = [p^q for p,q in zip(message_1,c1_c2)]
    M2 = [chr(j) for j in message_2]
    M2 = ''.join(M2)
    if(M2 in store):
        Pad = [p^q for p,q in zip(message_1,c1)]
        print("Message1: {}, Message2: {}, Pad: {}\n".format(M2,i,Pad))
