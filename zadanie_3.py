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