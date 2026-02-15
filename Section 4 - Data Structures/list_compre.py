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

# create a nested list [[1,1,1],[2,4,8],[3,9,27]]

new = []

for i in range(1,4):
    new.append((i,i**2,i**3))

print(new)


neww = [[i,i**2,i**3] for i in range(1,4)]

print(neww)

flatten_list = []
for i in neww:
    for j in i:
        flatten_list.append(j)

print(flatten_list)

# using list comprehension

listtt = [j for i in neww for j in i ]

print(listtt)

orders_listt = [
    [101,'2023-07-25 00:00:00.0',11599,'CLOSED'],
    [102,'2023-07-25 00:00:00.0',256,'PENDING_PAYMENT'],
    [103,'2023-07-25 00:00:00.0',12111,'COMPLETE']
]
# get the closed order only 
newest = []

for i in orders_listt:
    if i[3] == 'CLOSED':
        newest.append(i)

print(newest)


newss = [i for i in orders_listt if i[3] == 'CLOSED']

print(newss)


# unpacking 

order_id,order_date,customer_id,order_status = orders_listt[0]

print(order_id)



# slicing 

customers = [1,'Shivam Kumar','xxxxxxxxx','xxxxxxxx','6303 Heather Plaza', 'Delhi','IND',78521]


print(customers[0:2]+ customers[4:])







