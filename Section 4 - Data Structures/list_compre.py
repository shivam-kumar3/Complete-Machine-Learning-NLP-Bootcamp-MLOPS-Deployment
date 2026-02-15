# List comprehension


order_amt = [100,200,50,500,400,900,1200,70]

# create a new list including gst amt 


order_gst = []

# using for loop 

for i in order_amt:
    order_gst.append(i +i*0.18 )


print(order_gst)

order = [i+i*0.18 for i in order_amt]

print(order)
order2 = [i+i*0.18 for i in order_amt if i > 200]

print(order2)


# with list of tuples with gst rate 

order_tup = [(100,5),(200,10),(50,12),(500,18),(400,12),(900,5),(1200,18),(70,12)]


order_tupp = []

for i in order_tup:
    order_tupp.append(i[0] + i[0]*i[1]/100)


print(order_tupp)

order_tuppp = [(i[0],i[1],i[0] +i[0]*i[1]/100) for i in order_tup]

print(order_tuppp)











