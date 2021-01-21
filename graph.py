import matplotlib.pyplot as plt
import pandas as pd
empdata={"empid":[1001,1002,1003,1004,1005],"ename":["Adil","Aqib","Amir","Armaan","Ashu"],"sal":[9000,10340,9800,12000,10020],"dob":["10-10-2000","10-2-2012","23-2-1999","23-9-1998","12-2-1908"]}
df=pd.DataFrame(empdata)
x=df['empid']
y=df['sal']
plt.bar(x,y,label='Employee data',color='red')
plt.xlabel('Employee id')
plt.ylabel('Employee Salaries')
plt.title('Micsoft inc')
plt.legend()
plt.show()