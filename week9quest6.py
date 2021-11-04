def vowels(v):
   v = 0;
   c = 0;
   for char in v:
       if ((ord(char) >= 65 and ord(char) <= 90) or (ord(char) >= 97 and ord(char) <= 122)):
           if (char== 'a' or char == 'e' or char == 'i' or char == 'o' or char == 'u' or char == 'A' or char == 'E' or char== 'I' or char == 'O' or char == 'U'):
               v += 1;
           else:
               c += 1
   print ('Total vowels: '+str(v))
   print ('Total consonants: '+str(c))
    
