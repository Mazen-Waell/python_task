K,M=  map( int,(input().split()) )
lists=[list(map(int,input().split()))[1:] for _ in range(K)]
 
remainders={0}
for lis in lists :
    remainders = {(r+x**2) % M for r in remainders for x in lis}
 

print( max(remainders))