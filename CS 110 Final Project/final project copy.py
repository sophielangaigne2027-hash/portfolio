#Visualization of Chicago Public Schools
#COMP_SCI 110 Final Project
#Chicago Public Schools CSV File
#Sophie Langaigne


import csv
from tkinter import Tk, Canvas



###-----------------------------Constants for Data Visualization---------------------###
GUTTER = 30 
MARGIN = 15 
CHART_WIDTH = 900
CHART_HEIGHT = 350
CANVAS_WIDTH = CHART_WIDTH + GUTTER * 2
CANVAS_HEIGHT = CHART_HEIGHT + GUTTER * 2
BAR_COUNT = 10
BAR_WIDTH = (CHART_WIDTH - MARGIN * 2) / BAR_COUNT
COLORS = ['black', 'yellow', 'red', 'blue', 'pink', 'green', 'purple']
RACES = ["White Students",
         "African American Students",
         "Native American Students",
         "Hispanic Students",
         "Multiracial Students",
         "Asian Students",
         "Hawaiian and Pacific Islander Students"]
KEY_HEIGHT = 100
KEY_WIDTH = 300


######----------------------FUNCTIONS----------------------------#######
def change_int(value : str, default_value = 0):
    if value.strip() == '': return default_value 
    try:
        return int(value.strip())
    except:
        print('Bad integer value:', value)
        return default_value

def change_float(value : str, default_value = 0.0): 
    if value.strip() == '': return default_value
    try:
        return float(value.strip())
    except:
        print('Bad float value:', value)
        return default_value


def load_data(row):
    school_ID = change_int(row[0])
    school_name = row[1].strip()
    network = row[2].strip()
    governance = row[3].strip()
    school_type = row[4].strip()
    community_area = row[5].strip()
    total_students = change_int(row[6])
    white_students = change_int(row[7])
    aa_students = change_int(row[8])
    na_students = change_int(row[9])
    h_students = change_int(row[10])
    mr_students = change_int(row[11])
    asian_s = change_int(row[12])
    hawaiian_students = change_int(row[13])

    return {
        'School ID' : school_ID,
        'School Name' : school_name,
        'Network' : network,
        'Governance' : governance,
        'School Type' : school_type,
        'Community Area' : community_area,
        'Total Students' : total_students,
        'White Students' : white_students,
        'African American Students' : aa_students,
        'Native American Students' : na_students,
        'Hispanic Students' : h_students,
        'Multiracial Students' : mr_students,
        'Asian Students' : asian_s,
        'Hawaiian and Pacific Islander Students' : hawaiian_students

    }

#######------------VISUALIZATION FUNCTIONS------------------------------########
def draw_bar(canvas, x, race_array):
    total = 0
    for race_num in race_array:
        total += race_num
    y = CANVAS_HEIGHT - GUTTER
    for i in range(7):
        race_num = race_array[i]
        color = COLORS[i]
        height = race_num / 25
        canvas.create_rectangle(x, y, x + BAR_WIDTH, y - height, fill= color, outline="")
        y -= height
        

def draw_data_bars(canvas, community_areas):
    x = GUTTER + MARGIN
    count = 0
    for area_name in community_areas:
        draw_bar(canvas, x, community_areas[area_name])
        x += BAR_WIDTH / 2
        canvas.create_text(x, CANVAS_HEIGHT - (GUTTER / 2), text=area_name, fill='black', font='Helvetica 10')
        x += BAR_WIDTH / 2
        count += 1
        if count == 10:
            break

def draw_legend(canvas):
    canvas.create_rectangle(GUTTER, GUTTER - 2, KEY_WIDTH, KEY_HEIGHT + GUTTER + 2, fill = 'white')
    text_height = (KEY_HEIGHT / 7) - 2
    height = GUTTER + 1
    for i in range(7):
        color = COLORS[i]
        race = RACES[i]
        canvas.create_text(GUTTER + 24, height, text= race, anchor= 'nw')
        canvas.create_rectangle(GUTTER + 2, height, GUTTER + 22, height + text_height, fill= color)
        height += text_height + 2

#####---------------------------LOADING DATA-------------------------------######

file = open('CPS_Schools.csv')
next(file)

data_reader = csv.reader(file)      

CPS_data = []
for row in data_reader:
    #print(row)
    if len(row) != 14:
        print("invalid")
        continue
    info = load_data(row)
    CPS_data.append(info)
print(CPS_data)

community_areas = {}
for key in CPS_data:
    #print(key)
    community_area = key['Community Area']
    white_students = key['White Students']
    aa_students = key['African American Students']
    na_students = key['Native American Students']
    h_students = key['Hispanic Students']
    mr_students = key['Multiracial Students']
    asian_s = key['Asian Students']
    hawaiian_students = key['Hawaiian and Pacific Islander Students']
    

    if community_area not in community_areas:
        community_areas[community_area] = [0, 0, 0, 0, 0, 0, 0]
    community_areas[community_area][0] = community_areas[community_area][0] + white_students 
    community_areas[community_area][1] = community_areas[community_area][1] + aa_students
    community_areas[community_area][2] = community_areas[community_area][2] + na_students
    community_areas[community_area][3] = community_areas[community_area][3] + h_students
    community_areas[community_area][4] = community_areas[community_area][4] + mr_students
    community_areas[community_area][5] = community_areas[community_area][5] + asian_s
    community_areas[community_area][6] = community_areas[community_area][6] + hawaiian_students

print(community_areas)
######---------------TKINTER WINDOW---------------------------######
gui = Tk()
gui.title('Chicago Public Schools and the Proportions of Races')

canvas = Canvas(gui, width = CANVAS_WIDTH, height = CANVAS_HEIGHT,
background = '#cccccc')
canvas.pack()



draw_data_bars(canvas, community_areas)
draw_legend(canvas)


