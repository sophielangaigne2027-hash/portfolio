'''For this year’s final project, I used the Chicago Public Schools dataset provided by Professor Horn. This dataset included demographic information about all of the schools in the Chicago Public School system.
I was curious about the proportion of each race of students in each neighborhood for the Chicago Public Schools since this data is from recent years and I was interested in whether or not the public
school system in Chicago is segregated.  

Cleaning Data

Overall, the data in the CSV file was formatted in a way that was easy to read and extract data from, however, in many parts of the data that included strings there were spaces.
Due to these spaces, I was required to strip parts of the data using the .strip function. For the numbers in the CSV file I was also required to turn these numbers into integers, so I had to create
a function called change_int and I also created one called change_float just in case there were any float data types that I missed. 

In my change_int and change_float functions, I also included try and except lines to account for
unexpected errors in converting data types.


Aggregating and Processing Data 
I started aggregating and processing my data by creating a list of dictionaries to hold the data from the CSV file. Each piece of the list represented each row of the CSV file and I
created keys for each column name. I did that using my load_data function and by creating a list called CPS data where the computer would read each row of the CSV file and append the information
into the list. 

Then using that list, I created another dictionary with all of the data that I wanted to include, which was the community_area(the neighborhood) and each race of students.
For each key in the list that I previously created, I went through each neighborhood and I indexed each race to find the amount of students in that neighborhood of each race.
This created a list fpr each neighborhood with the amount of students of each race. Using this aggregated data, I was then able to start visualizing my data.

VISUALIZATION
Based on my calculations, there are 77 different neighborhoods within the Chicago Public School system. I decided that I would pick 10 of the neighborhoods in the Chicago Public System to
visualize since visualizing 77 different neighborhoods would leave my graph crammed and it would be too difficult to see the true distribution of each race. 

I wanted to create a stacked bar chart of each of these 10 neighborhoods and I wanted to give each race a color so that I’d be able to see the proportion of each race in each
neighborhood. To do this I had to evenly space out 10 neighborhoods with my draw_bar and draw_data_bars functions. I also had to create multiple constants at the beginning of my file to
do my graph correctly. One of the biggest challenges I faced was getting the bars to stack on top of one another and getting each bar to have a different color. I was able to solve this
problem by altering my y variable and creating an array(which I got help from my TA). I also had to create a list of my colors and I had to assign a specific color to each race. Lastly,
I created a legend so that the reader would understand the graph better.

Overall I selected an interesting data set and I came up with an interesting question. I was able to clean this data by using my .strip function to remove white space and
I used my other change_int and change_float functions to make sure that all of the data I had was in the correct form. I was also able to perform two different data operations by
using row wise operations and by aggregating my data and filtering my data into a list. I also generated reports, and error checked the data. 


I also created a dictionary (ex.community_areas) and two lists(ex. CPS_data, COLORS, RACES) throughout my code to process my data. 

I created three functions called draw_bar, draw_data_bars, and draw_legend to map data points to visual parameters.

My code was very neat and organized and easy to follow through my use of comments and sectioning.

My graph was also very visually pleasing and aesthetic through my use of color. 

I also went above and beyond through my use of a stacked bar graph.
 
 If you were going to publish your project in a newspaper, what caption would you give it? What story are you trying to tell?


Chicago Public Schools are slightly segregated and we need equal proportions of each race in Chicago Public Schools. 
'''
