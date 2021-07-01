import sqlite3

#Connection to the database
MyCricket=sqlite3.connect('Database_cricket.db')
curs=MyCricket.cursor()

#Create Match Table
curs.execute('''CREATE TABLE IF NOT EXISTS match(Player TEXT NOT NULL PRIMARY KEY,Scored INTEGER,Faced INTEGER,FOURS INTEGER,Sixes INTEGER, Bowled INTEGER,Maiden INTEGER, Given INTEGER,Wkts INTEGER, Catches INTEGER, Stumping INTEGER, RO INTEGER);''' )

#create Stats table
curs.execute('''CREATE TABLE IF NOT EXISTS stats(Player TEXT PRIMARY KEY,Matches INTEGER,Runs INTEGER,Hundreads INTEGER,Fifties INTEGER,Value INTEGER, ctg TEXT);''')

#create teams table
curs.execute('''CREATE TABLE IF NOT EXISTS teams (Name TEXT NOT NULL,Players TEXT NOT NULL,Value INTEGER);''')

#Display Data from match table if exists
sql="SELECT * FROM match"
curs.execute(sql)
result=curs.fetchall()
if(result):
    for i in result:
        print(i)
    
else:
    print("No data Found")
option=input("\n Do you want to add more details (Y/N): ?")
#adding data to match table
while(option=='Y' or option=='y'):
    name=input("Enter Plyer name: ")
    score=int(input("Score: "))
    faced=int(input("Faced: "))
    fours=int(input("Fours: "))
    sixes=int(input("Sixes: "))
    bowled=int(input("Bowled: "))
    maiden=int(input("Maiden: "))
    given=int(input("Given: "))
    wkts=int(input("Wkts: "))
    catches=int(input("Catches: "))
    stumping=int(input("Stumping: "))
    ro=int(input("Run Out: "))

    try:
        curs.execute("INSERT INTO match(Player,Scored,Faced,Fours,Sixes,Bowled,Maiden,Given,Wkts,Catches,Stumping,RO)values(?,?,?,?,?,?,?,?,?,?,?,?);",(name,score,faced,fours,sixes,bowled,maiden,given,wkts,catches,stumping,ro))
        MyCricket.commit()
        print("Record added sucessfully in match table")
    except:
        print("error in operation")
        MyCricket.rollback()

    #adding data to stats table
    print("Enter player information in the stats table ")
    T_matches=int(input("Total Matches: "))
    T_runs=int(input("Total runs: "))
    hundreads=int(input("100s : "))
    fifties=int(input("50s: "))
    value=int(input("Value: "))
    ctg=input("Category (BAT,BWL,AR,WK): ")
    try:
        curs.execute("INSERT INTO stats(Player,Matches,Runs,Hundreads,Fifties,Value,ctg)values(?,?,?,?,?,?,?);",(name,T_matches,T_runs,hundreads,fifties,value,ctg))
        MyCricket.commit()
        print("Record added sucessfully in stats table")
    except:
        print("error in operation")
        MyCricket.rollback()
    option=input("\n Do you want to add more details (Y/N): ?")
MyCricket.close()
