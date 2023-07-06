{"filter":false,"title":"lab_17_2.py","tooltip":"/lab_17_2.py","undoManager":{"mark":4,"position":4,"stack":[[{"start":{"row":0,"column":0},"end":{"row":55,"column":24},"action":"insert","lines":["# Module Lab: Caesar Cipher Program Bug #2","#","# In a previous lab, you created a Caesar cipher program. This version of","# the program is buggy. Use a debugger to find the bug and fix it.","","# Double the given alphabet","def getDoubleAlphabet(alphabet):","    doubleAlphabet = alphabet + alphabet","    return doubleAlphabet","","# Get a message to encrypt","def getMessage():","    stringToEncrypt = input(\"Please enter a message to encrypt: \")","    return stringToEncrypt","","# Get a cipher key","def getCipherKey():","    shiftAmount = input(\"Please enter a key (whole number from 1-25): \")","    return shiftAmount","","# Encrypt message","def encryptMessage(message, cipherKey, alphabet):","    encryptedMessage = \"\"","    uppercaseMessage = \"\"","    uppercaseMessage = message","    for currentCharacter in uppercaseMessage:","        position = alphabet.find(currentCharacter)","        newPosition = position + int(cipherKey)","        if currentCharacter in alphabet:","            encryptedMessage = encryptedMessage + alphabet[newPosition]","        else:","            encryptedMessage = encryptedMessage + currentCharacter","    return encryptedMessage","","# Decrypt message","def decryptMessage(message, cipherKey, alphabet):","    decryptKey = -1 * int(cipherKey)","    return encryptMessage(message, decryptKey, alphabet)","","# Main program logic","def runCaesarCipherProgram():","    myAlphabet=\"ABCDEFGHIJKLMNOPQRSTUVWXYZ\"","    print(f'Alphabet: {myAlphabet}')","    myAlphabet2 = getDoubleAlphabet(myAlphabet)","    print(f'Alphabet2: {myAlphabet2}')","    myMessage = getMessage()","    print(myMessage)","    myCipherKey = getCipherKey()","    print(myCipherKey)","    myEncryptedMessage = encryptMessage(myMessage, myCipherKey, myAlphabet2)","    print(f'Encrypted Message: {myEncryptedMessage}')","    myDecryptedMessage = decryptMessage(myEncryptedMessage, myCipherKey, myAlphabet2)","    print(f'Decrypted Message: {myDecryptedMessage}')","","# Main logic","runCaesarCipherProgram()"],"id":1}],[{"start":{"row":18,"column":11},"end":{"row":18,"column":12},"action":"insert","lines":["i"],"id":2},{"start":{"row":18,"column":12},"end":{"row":18,"column":13},"action":"insert","lines":["n"]},{"start":{"row":18,"column":13},"end":{"row":18,"column":14},"action":"insert","lines":["t"]},{"start":{"row":18,"column":14},"end":{"row":18,"column":15},"action":"insert","lines":["("]}],[{"start":{"row":18,"column":26},"end":{"row":18,"column":27},"action":"insert","lines":[")"],"id":3}],[{"start":{"row":24,"column":30},"end":{"row":24,"column":31},"action":"insert","lines":["."],"id":4},{"start":{"row":24,"column":31},"end":{"row":24,"column":32},"action":"insert","lines":["u"]},{"start":{"row":24,"column":32},"end":{"row":24,"column":33},"action":"insert","lines":["p"]},{"start":{"row":24,"column":33},"end":{"row":24,"column":34},"action":"insert","lines":["p"]},{"start":{"row":24,"column":34},"end":{"row":24,"column":35},"action":"insert","lines":["e"]},{"start":{"row":24,"column":35},"end":{"row":24,"column":36},"action":"insert","lines":["r"]}],[{"start":{"row":24,"column":36},"end":{"row":24,"column":38},"action":"insert","lines":["()"],"id":5}]]},"ace":{"folds":[],"scrolltop":27,"scrollleft":0,"selection":{"start":{"row":11,"column":17},"end":{"row":11,"column":17},"isBackwards":false},"options":{"guessTabSize":true,"useWrapMode":false,"wrapToView":true},"firstLineState":{"row":0,"state":"start","mode":"ace/mode/python"}},"timestamp":1688649777356,"hash":"14612548d4e555db6e4a9525053d617eae73371c"}