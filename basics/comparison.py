# COMPARISON OPERATORS..................
    # "==","<=",">=","<",">" gives o/p in true or false


a=3
b=9
print(a==b) 
print(a<=b) 
print(a>=b)
print(a>b)
print(a<b)

# in case of string ..............

x = "hello"
y = "heLlo"
print(2)
print(x==y) # false
print(x==y.lower()) # true

print("A">"S") # false as ascii of S is bigger
print(ord("A")) # gives ascii code 

#   AND OR NOT OPERATOR...............

p=23
q=20
r=30

res1 = p==q
res2 = r>q
res3 = p<r
res4 = res1 or res2     # res1-->false but res2 --> true so it is true
print("res4 is ",res4)
res5 = res1 and res2 or res3    
print("res5 is ",res5)
res6 = res1 or (not res2) and res3  # precidence (1st not --> then and --> last or)
print ("res6 is ",res6)