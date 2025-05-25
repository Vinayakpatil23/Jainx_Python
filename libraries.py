import numpy as np
from numpy.ma.core import reshape

# arr=np.array([1,2,3,4,5])
# print(arr)

# arr1=np.array([[1,2],[3,4]])
# arr2=np.array([[1,2],[3,4]])
# res1=np.matmul(arr1,arr2)
# res2=arr1*arr2
# print(res1)
# print(res2)

# arr1=np.array([[1,2,3],[4,5,6]])
# arr2=np.array([[1,2],[3,4],[5,6]])
# res1=np.matmul(arr1,arr2)
# # res2=arr1*arr2 --> it is not possible to multiply bcz no equal rows and columns
# print(res1)
# # print(res2)

# arr1=np.array([[1,2,3],[4,5,6]])
# print(arr1)
# res1=np.transpose(arr1)
# print(res1)

# arr1=np.array([[1,2,3],[4,5,6]])
# print(arr1)
# res1=np.invert(arr1)
# print(res1)

# arr1=np.array([[1,2],[3,4]])
# print(arr1)
# res1=np.linalg.inv(arr1)
# print(res1)

# arr=np.arange(10)
# print(arr)

# arr=np.arange(12)
# reshaped_arr=np.reshape(arr,(3,4))
# print(reshaped_arr)

# arr=np.array([[1,2,3],[4,5,6]])
# col_mean=np.mean(arr,axis=0)
# row_mean=np.mean(arr,axis=1)
# print(row_mean)
# print(col_mean)


# arr=np.array([[1,2,3],[4,5,6]])
# col_sum=np.sum(arr,axis=0)
# row_sum=np.sum(arr,axis=1)
# print(col_sum)
# print(row_sum)

# rand_arr=np.random.rand(5)
# print(rand_arr)

import pandas as pd
from pandas import read_json

data={
    'Name':['Vinayak','Mahesh','Prajwal'],
    'Age':[24,27,30],
    'City':['Bengaluru','Badami','Andra']
}

# print(data)
# df=pd.DataFrame(data)
# print(df)
# df.to_csv('employee.csv',index=False)
# df.to_json('employee1.json',orient='records')
# read=pd.read_csv('employee.csv')
# print(read)
# read1=pd.read_json('employee1.json')
# print(read1)

#------- adding new data to csv file ----------
# new_data=pd.DataFrame([{'Name':'David','Age':25,'City':'Gadag'}])
# df_csv=pd.read_csv('employee.csv')
# df_csv=pd.concat([df_csv,new_data],ignore_index=True)
#
# df_csv.to_csv('employee.csv',index=False)


#------- adding new data to json file ----------
# new_json=pd.DataFrame([{'Name':'David','Age':25,'City':'Gadag'}])
# df_json=pd.read_json('employee1.json')
# df_json=pd.concat([df_json,new_json],ignore_index=True)
#
# df_json.to_json('employee1.json',orient="records")


#---------- deleting a data from csv file ------------------
# df_csv=pd.read_csv('employee.csv')
# df_csv=df_csv[df_csv['Name']!='Mahesh']
#
# df_csv.to_csv('employee.csv',index=False)


#---------- deleting a data from json file ------------------
# df_json=pd.read_json('employee1.json')
# df_json=df_json[df_json['Name']!='Mahesh']
#
# df_json.to_json('employee1.json',orient="records")

