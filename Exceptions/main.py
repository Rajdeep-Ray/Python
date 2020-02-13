T=int(input())
for i in range(T):
    a=input()
    a=a.strip()
    a=list(a.replace(" ",''))
    a1=(a[0])
    a2=(a[1])
    try:
        print(int(a1)//int(a2))
    except ZeroDivisionError as e:
        print("Error Code:",e)
    except ValueError as e:
        print("Error Code:",e)
