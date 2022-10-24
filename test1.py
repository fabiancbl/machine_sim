import pd_sim as pd
df = pd.DataFrame([[0, 2, 3], [0, 4, 1], [10, 20, 30]],columns=['A', 'B', 'C'])
print(df.iat[0,1])