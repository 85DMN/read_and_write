with open('recipes.txt') as f:
    cook_book = {}
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

def get_shop_list_by_dishes(dishes,person_count):
    result = {}
    naimenovanie = ['ingredient','quantity','measure']
    for j in dishes:
        if cook_book.get(j) == None:
            print(f"Блюда '{j}' нет в меню")
        else:
            for m in cook_book[j]:
                if result.get(m[keys[0]])==None:
                    result[m[naimenovanie[0]]] = {naimenovanie[2]:m[naimenovanie[1]]*person_count,
                                                  naimenovanie[1]:m[naimenovanie[2]]}
                else:
                    result[m[naimenovanie[0]]] = {naimenovanie[2]:m[naimenovanie[1]]*person_count+result[m[naimenovanie[0]]][naimenovanie[-1]],
                                                  naimenovanie[1]:m[naimenovanie[2]]}
    return result
# print(cook_book) 
print(get_shop_list_by_dishes(['Омлет','Фахитос','Омлет'],5))