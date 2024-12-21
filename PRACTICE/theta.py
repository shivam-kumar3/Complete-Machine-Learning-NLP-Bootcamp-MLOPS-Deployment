import pandas as pd 

x = [1,2,3,4,5]
y = [2,3,5,4,6]

df = pd.DataFrame({"X":x,"Y":y})
print(df)


x_mean = df["X"].mean()
y_mean = df["Y"].mean()

print(x_mean)
print(y_mean)


theta_1 = sum((df["X"]- x_mean) * (df['Y']- y_mean)) / sum((df['X']- x_mean)**2)

print(theta_1)


theta_0 = y_mean - (theta_1 * x_mean)

print(round(theta_0,2 ))


