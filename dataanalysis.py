
def getGradeBySurname(data,surname,attempt):
    for index, row in data.iterrows():
        if(row["Surname"] == surname):
            if(attempt == "first"):
                return row["Pre-Test Grade"]
            if(attempt == "last"):
                return row["Post-Test Grade (1st attempt)"]
            if(attempt == "both"):
                return "Pre: " + str(row["Pre-Test Grade"]) + ", " + "Post: " + str(row["Post-Test Grade (1st attempt)"]) 

def getGradeBySurname(data,surname,attempt):
    for index, row in data.iterrows():
        if(row["Surname"] == surname):
            if(attempt == "first"):
                return row["Pre-Test Grade"]
            if(attempt == "last"):
                return row["Post-Test Grade (1st attempt)"]
            if(attempt == "both"):
                return "Pre: " + str(row["Pre-Test Grade"]) + ", " + "Post: " + str(row["Post-Test Grade (1st attempt)"]) 
