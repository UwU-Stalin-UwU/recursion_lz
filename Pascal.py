def pascal(n):                                                   #Построение треугольника Паскаля
    if n == 0:                                                   #При полном обнулении введенного выходим из рекурсии
        return [1]                                               
    else:      
        st = [1]                                                #Иначе идем построчно, создавая новую строку треугольника и генерируя предыдущую через рекурсию 
        previous_st = pascal(n - 1)                             
        for i in range(len(previous_st) - 1):
            st.append(previous_st[i] + previous_st[i + 1])    
        st.append(1)
        print(st)
        return st
    

vvod=input("Введите длину треугольника Паскаля: ")                                                      #Ввод нужного количества строк в треугольнике Паскаля
vvod=int(vvod)
print("Треугольник Паскаля до", vvod, "уровня: ")
print("[1]")                                                      #Вывод
final=pascal(vvod-1)