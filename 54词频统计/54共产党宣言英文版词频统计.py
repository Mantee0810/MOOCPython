
def Get_TXT(adr):
    txt = open(adr,'r').read()
    txt = txt.lower()
    for char in '!@#$%^&*()[];'"|<>?":
        txt = txt.replace(char,' ')
    return txt

def main():
    adr = "Manifesto_of_the_Communist_Party.txt"
    CP_txt = Get_TXT(adr)
    words = CP_txt.split()
    counts = {}

    for word in words:
        counts[word] = counts.get(word,0)+1
    items = list(counts.items())
    items.sort(key=lambda x:x[1],reverse=True)
    for i in range(50):
        word,count = items[i]
        print("{:<10}{:>5}".format(word,count))

if __name__ == '__main__':
    main()










