#1.zadatak
brojac=0
for red in open('index1.txt'):
    if red=='\n':
        brojac+=1
print brojac
#2.zadatak
lista=[]
for red in open('index1.txt'):
    red=red.decode('utf8').lower().strip()
    if red!='':
        if red.split('\t')[3]=='n' and red.split('\t')[1][-1] not in 'aeiou':
            red=red.split('\t')
            lista.append(red[2])
print lista
#3.zadatak
fajl=open('leme_imenica_kraj_na_suglasnike.txt','w')
for dio in lista:
    fajl.write(dio.encode('utf8')+'\n')
fajl.close()
citaj=open('leme_imenica.txt').read()
print citaj
#4.zadatak
pridjevi=0
imenice=0
for red in open('index1.txt'):
    red=red.decode('utf8').lower().strip()
    if red!='':
        if red.split('\t')[3]=='A':
            pridjevi+=1
        if red.split('\t')[3]=='N':
            imenice+=1
print pridjevi, imenice
#5.zadatak
redova=0
uk_rijec=''
uk_leme=''
rijec=0
leme=0
for red in open('index1.txt'):
    red=red.decode('utf8').lower().strip()
    if red!='':
        uk_rijec=uk_rijec+red.strip().split('\t')[1]
        rijec+=1
        uk_leme=uk_leme+red.strip().split('\t')[2]
        leme+=1
print float(len(uk_rijec))/rijec, float(len(uk_leme))/leme