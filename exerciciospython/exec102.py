def fatorial(num, show=False):
    fatorialf = ''
    if show:
        valorfinal = 1
        for i in range(1 ,num+1):
            if i == 1:
                valorfinal *= i
                fatorialf = fatorialf+str(i)
                continue
            valorfinal *= i
            fatorialf = fatorialf+' x '+str(i)

        fatorialf = fatorialf+' = '+str(valorfinal)

        return fatorialf


    else:
        valorfinal = 1
        for i in range(num + 1):
            if i == 0:
                continue
            valorfinal *= i

        return valorfinal

print(fatorial(7, show=True))