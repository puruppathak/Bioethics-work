import pymysql

#making connection to database use proper password and username
connection = pymysql.connect(host='localhost',
                         user='root',
                         password='root',
                         charset='utf8mb4',
                         cursorclass=pymysql.cursors.DictCursor,
                             db = 'puru')

cursor = connection.cursor()

#drug_name = input("Drug Name: ")

#building query string

#Building Ethics applicable list


NCTlist=[]
ECount=[]


cursor.execute('SELECT * FROM viz')


for row in cursor:
        NCTlist.append(row["nct_id"])
        if row["Economy"] == "Peru":
         print("Found")
         print(row["nct_id"])
         ECount.append(row["nct_id"])


        else:
         continue

"""
        if row["DALY"] is None :
         print(row["nct_id"])
        """


"""
    print("Found")
else:
    print("Wrong")
"""


print(len(ECount))

k="Puru"
ID="NCT01857284"
cursor.execute('UPDATE viz SET Economy="Puru"  WHERE nct_id = "NCT01857284"')
print('changed', cursor.rowcount)

connection.commit()



"""



#Building is_reported list from ethics_applicable_list
for row in ethics_applicable_list:
    if (row["Is_Reported"] == 'Y'):
        is_reported_list.append(row)



#Building is_published_Cuttoff list from ethics_applicable_list
for row in ethics_applicable_list:
    if (row["Is_Published_Cutoff"] == 'Y'):
        is_pub_cutoff_list.append(row)

for row in is_pub_cutoff_list:
    print(row)

"""

#closing the connection to the database
cursor.close()
connection.close()