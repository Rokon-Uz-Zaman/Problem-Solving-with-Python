def fun2():
  
  ar=list(map(int,input().split()))
  s=range(0,len(ar))


  for e in ar :
    if ar.count(e) > 1:
      dub=e
    if e not in s:
      miss=s

      
  sum  = dub+miss
  return sum


fun2()
