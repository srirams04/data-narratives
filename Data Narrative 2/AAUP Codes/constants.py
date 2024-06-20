import pandas as pd
import numpy as np

us_states = {
    "AL": "Alabama",
    "AK": "Alaska",
    "AZ": "Arizona",
    "AR": "Arkansas",
    "CA": "California",
    "CO": "Colorado",
    "CT": "Connecticut",
    "DC": "Dst. of Columbia",
    "DE": "Delaware",
    "FL": "Florida",
    "GA": "Georgia",
    "HI": "Hawaii",
    "ID": "Idaho",
    "IL": "Illinois",
    "IN": "Indiana",
    "IA": "Iowa",
    "KS": "Kansas",
    "KY": "Kentucky",
    "LA": "Louisiana",
    "ME": "Maine",
    "MD": "Maryland",
    "MA": "Massachusetts",
    "MI": "Michigan",
    "MN": "Minnesota",
    "MS": "Mississippi",
    "MO": "Missouri",
    "MT": "Montana",
    "NE": "Nebraska",
    "NV": "Nevada",
    "NH": "New Hampshire",
    "NJ": "New Jersey",
    "NM": "New Mexico",
    "NY": "New York",
    "NC": "North Carolina",
    "ND": "North Dakota",
    "OH": "Ohio",
    "OK": "Oklahoma",
    "OR": "Oregon",
    "PA": "Pennsylvania",
    "RI": "Rhode Island",
    "SC": "South Carolina",
    "SD": "South Dakota",
    "TN": "Tennessee",
    "TX": "Texas",
    "UT": "Utah",
    "VT": "Vermont",
    "VA": "Virginia",
    "WA": "Washington",
    "WV": "West Virginia",
    "WI": "Wisconsin",
    "WY": "Wyoming"
}

west_coast_states = ['AK', 'AZ', 'CA', 'CO', 'HI', 'ID', 'MT', 'NV', 'NM', 'OR', 'UT', 'WA', 'WY']
east_coast_states = ['ME', 'NH', 'VT', 'MA', 'RI', 'CT', 'NY', 'NJ', 'PA', 'MD', 'DE', 'VA', 'NC', 'SC', 'GA', 'FL']

avg_sal = {}
avg_comp = {}
num_of = {}
avg_sal['full'] = "Average Salary - Full Professors"
avg_sal['assc'] = "Average Salary - Associate Professors"
avg_sal['asst'] = "Average Salary - Associate Professors"
avg_sal['all'] = "Average Salary - All Ranks"
avg_comp['full'] = "Average Compensation - Full Professors"
avg_comp['assc'] = "Average Compensation - Associate Professors"
avg_comp['asst'] = "Average Compensation - Assistant Professors"
avg_comp['all'] = "Average Compensation - All Ranks"
num_of['full'] = "Number of Full Professors"
num_of['assc'] = "Number of Associate Professors"
num_of['asst'] = "Number of Assistant Professors"
num_of['inst'] = "Number of Instructors"
num_of['all'] = "Number of Faculty - All Ranks"
ranks = {"full": "Full", 'assc': "Associate", 'asst': "Assistant"}

font1 = {'family':'Sans','color':'blue','size':18}
font2 = {'family':'serif','color':'darkred','size':15}

df = pd.read_csv('aaup.csv')

for dic in (avg_sal, avg_comp, num_of):
    for val in dic.values():
        df[val] = df[val].mask(df[val] == '*', np.nan)
        df[val] = pd.to_numeric(df[val], errors="coerce")
