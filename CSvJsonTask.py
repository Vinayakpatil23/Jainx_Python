import pandas as pd

BookData={
    'BID':[1,2,3],
    'Bname':['DSA','PYTHON','C'],
    'Author':['Vinayak','Prajwal','Sahana'],
    'Price':[1000,2000,500]
}

# d=pd.DataFrame(BookData)
# B_csv=d.to_csv('Book.csv',index=False)
# B_json=d.to_json('Books.json',orient="records")

# read=pd.read_csv('Book.csv')
# print(read)
# read1=pd.read_json('Books.json')
# print(read1)

# new_data=pd.DataFrame([{'BID':4,'Bname':'JAVA','Author':'Mahesh','Price':2000}])
# read1=pd.read_json('Books.json')
# read1=pd.concat([read1,new_data],ignore_index=True)
# read1.to_json('Books.json',orient="records")

# new_data=pd.DataFrame([{'BID':4,'Bname':'JAVA','Author':'Mahesh','Price':2000}])
# read=pd.read_csv('Book.csv')
# read=pd.concat([read,new_data],ignore_index=True)
# read.to_csv('Book.csv',index=False)

df_csv=pd.read_csv('Book.csv')
df_csv=df_csv[df_csv['Author']!='Mahesh']
df_csv.to_csv('Book.csv',index=False)

# df_json=pd.read_json('Books.json')
# df_json=df_json[df_json['Author']!='Mahesh']
# df_json.to_json('Books.json',orient="records")


