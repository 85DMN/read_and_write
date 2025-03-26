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

print(cook_book)

def get_shop_list_by_dishes(dishes,person_count):
    result = {}
    for j in dishes:
        for m in cook_book[j]:
            result[m[keys[0]]]={keys[2]:m[keys[1]]*person_count,keys[1]:m[keys[2]]}
    return result

print(get_shop_list_by_dishes(['Утка по-пекински'],2))

fs,ln = ['1.txt','2.txt','3.txt'],[]
for j in fs:
    with open(j,'r',encoding='cp1251') as f:
        d = 0
        for j in f:
            d+=1
        ln.append(d)

with open("result_t.txt",'w') as f:
    for jj in sorted(ln):
        f.write(f'{fs[ln.index(jj)]}\n')
        f.write(f'{jj}\n')
        with open(f'{fs[ln.index(jj)]}','r',encoding='cp1251') as fm:
            for j in fm:
                f.write(f'{j}')