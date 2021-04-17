import os
import csv
import pandas as pd


def pre_processing(gesture,header):
    filepath="data/raw_"+gesture+".csv" 
    p=open(filepath)
    lines = p.readlines()
    final = []
    final.append(header)
    for line in lines:
        if line!="" or line is None:
            s=line.split(",")
            s=s[:42]
            #print(len(s))
            l=[]
            for i in range(0,42,2):
                # print(i)
                # print(int(s[i])-int(s[0]))
                # print(i+1)
                #print(int(s[i+1])-int(s[1]))
                l.append(int(s[i])-int(s[0]))
                l.append(int(s[i+1])-int(s[1]))
            l.append(gesture)
            final.append(l)
    filepath = 'data/processed_'+gesture+'.csv'
    with open(filepath, 'w') as f:
        write = csv.writer(f)
        write.writerows(final)
    
def create_finalfile(header):
    for i in range(1,101):
        path = "data/final_"+str(i)+".csv"
        if os.path.isfile(path):
            pass
        else:
            df = pd.DataFrame(columns=header)
            with open(path, 'w') as f:
                write = csv.writer(f)
                write.writerow(header)
                for root, directories, files in os.walk("data/"):
                    for filename in files:
                        if "processed" in filename:
                            filepath = os.path.join("data/", filename)
                            df2 = pd.read_csv(filepath)
                            df = df.append(df2)
            df.to_csv(path,index=False)
            break




def main(gesture,is_create_final):
    os.chdir(os.path.join(os.path.split(os.path.abspath(__file__))[0],".."))
    cols=[]
    for i in range(1,43):
        cols.append("col-"+str(i))
    cols.append("target")

    if gesture=="all": 
        for root, directories, files in os.walk("data/"):
            for filename in files:
                if "raw" in filename:
                    pre_processing(filename[4:-4],cols)
    else:
        pre_processing(gesture,cols)
    
    if is_create_final:
        create_finalfile(cols)

if __name__ == "__main__":
    gesture = "all"
    is_create_final = True
    main(gesture, is_create_final)