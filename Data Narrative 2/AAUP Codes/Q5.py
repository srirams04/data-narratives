# To find the top 5 colleges offering doctoral degrees (I), master's degrees (IIA) and baccalaureate degrees (IIB) respectively. The top 5 colleges are classified based on the amount spent on the faculty.

import pandas as pd

# Load the CSV file into a DataFrame
df = pd.read_csv("aaup.csv")

# Convert columns to integers
df["Average Salary - All Ranks"] = df["Average Salary - All Ranks"].astype(int)
df["Average Compensation - All Ranks"] = df["Average Compensation - All Ranks"].astype(int)
df["Number of Faculty - All Ranks"] = df["Number of Faculty - All Ranks"].astype(int)

# Group colleges by type
grouped = df.groupby("Type")

# Loop through each type
for name, group in grouped:
    # Calculate the amount spent on faculty for each college
    group["Amount Spent on Faculty"] = (group["Average Salary - All Ranks"] + group["Average Compensation - All Ranks"]) * group["Number of Faculty - All Ranks"]
    
    # Sort colleges by amount spent on faculty
    group = group.sort_values("Amount Spent on Faculty", ascending=False)
    
    # Display the top 5 colleges for this type
    print("Type:", name)
    print(group[["College Name", "Amount Spent on Faculty"]].head(5))
    print()

"""
Type: I
                    College Name  Amount Spent on Faculty
1028    Univ. of Texas at Austin                  2707710
480   Univ.of Michigan-Ann Arbor                  2686320
153        University of Florida                  2609194
465    Michigan State University                  2368080
1110    University of Washington                  2367252

Type: IIA
                    College Name  Amount Spent on Faculty
58    San Diego State University                  1127160
59     San Jose State University                   980343
51        Cal.St.Univ-Long Beach                   957060
95     San Francisco State Univ.                   868525
53  Cal.Poly.St.U-Sn Luis Obispo                   865640

Type: IIB
                  College Name  Amount Spent on Faculty
696             Ithaca College                   428000
1050    Weber State University                   416313
648   William Paterson College                   387504
655      Trenton State College                   380295
460   Grand Valley State Univ.                   343791

"""