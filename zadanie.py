cook_book = {}

with open('recipes.txt') as f:
    for l in (f):
        if l.count('|')==0 and len(l)>2:#выводим все названия
            cook_book[l[:-1]]=[]
            key = l[:-1]
        elif l.count('|')>0:
            keys,sl = ['ingredient','quantity','measure'],{}
            for idx, j in enumerate(keys):
                if idx<2:
                    pos = l.index('|')
                    sl[j]=l[:(pos-1)] if idx==0 else int(l[:(pos-1)])
                    l = l[pos+2:]
                else:
                    sl[j]=l[:-1]

            cook_book[key].append(sl)

            