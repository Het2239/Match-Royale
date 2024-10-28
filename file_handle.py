import csv


# method to read data based on name
def scoreDataonNo():
    data = {}
    with open("score.csv", mode='r') as file:
        csv_reader = csv.DictReader(file)
        for row in csv_reader:
            
            name=row['NAME']
            score=row['SCORE']
            time=row['TIME']
            game_no=row['Game_No.']
        
            data[game_no]={'Name' : name,'Score':score,'Time taken':time,'Game No.':game_no}
    return data

def scoreDataOnName():
    data = {}
    with open("score.csv", mode='r') as file:
        csv_reader = csv.DictReader(file)
        for row in csv_reader:
            
            name=row['NAME']
            score=row['SCORE']
            time=row['TIME']

        
            data[name]={'Name' : name,'Score':score,'Time taken':time}
    return data
# method to make an entry in the file
def scoreUpdate(name,score,time,id):
    
    
    
    sdata=scoreSearch(name)
    
    a=sdata
    if len(sdata)>0 :
        if score<int(a['Score']):
            
            
            lis=[name,score,time,id]
            with open("Tkinter\match royale\data.csv", mode='a', newline='') as file:
                writer = csv.writer(file)
            
                writer.writerow(lis)
    elif(len(sdata)==0):
        
        
        lis=[name,score,time,id]
        with open("score.csv", mode='a', newline='') as file:
            writer = csv.writer(file)
        
            writer.writerow(lis)
# method to search the score of a particular player
def scoreSearch(name):
    lis=scoreDataOnName()
    try:
        a=lis[name.upper()]
        return a
    except KeyError:
        return {}



