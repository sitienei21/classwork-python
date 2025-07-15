#def fibonacci(n):
 #   if n ==1:
 #       return  1
  #  elif n==2:
    #    return 1
   # elif n>2:
     #   return fibonacci(n-1)+fibonacci(n-2)
#for i in range(1,5):
 #   print(i,":",fibonacci(i))

cache={}

value=0

def fib2(n):
    if n==1:
        value=1
    elif n==2:
        value=1
    elif n>2:
        value=fib2(n-1)+fib2(n-2)

    cache[n]=value
    return value
for i in range(1,500):
    print(f"{i}Term>{fib2(i)}")

    from functools import  lru_cache
    #L= last, R= recently,C=
    @lru_cache(maxsize=1000)
    def fib3(n):
        if n ==1 or n==2:
            return 1
        elif n>2:
            return fib3(n-1)+fib3(n-2)

    for i in range (1,10000):
        print (i,":",fib3(i))

    def TowerofHanoi(n,source,destination_rod,auxilliary_rod):
        if n==1:
            print("Move disk 1 from source",source, "to destination",destination_rod)
            return
        TowerofHanoi((n-1),source, auxilliary_rod,destination_rod)
        print("Move disk",n, "from source", source, "to destination", destination_rod)
        TowerofHanoi((n-1),source,auxilliary_rod,destination_rod)

    n=3
    TowerofHanoi(n,'A','B','C')