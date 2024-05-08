#Python file for graphs of data

import pandas as pd
import matplotlib.pyplot as plt
from matplotlib import pyplot

# Method for adding labels for the vertical Bar graph that takes parameters data.index and data.values
def verticalAddLabels(x,y):
    
    # Run a for loop through data.index, AKA the label names
    for i in range(len(x)):

        # Plot text, at x-cord, y-cord, value of text
        # set the fontsize, position and color of the label
        # Set some styling options for the label's box
        plt.text(i, y[i] + 2, y[i], fontsize = 9, ha = 'center', va = 'center', color = "black",
                 bbox = dict(facecolor = 'white', alpha = 1, pad = 2))
        

# Method for adding labels for the horizontal Bar graph that takes parameters data.index and data.values
def horizontalAddLabels(x,y):
    
    # Run a for loop through data.index, AKA the label names
    for i in range(len(x)):
        
        # Plot text, at x-cord, y-cord, value of text
        # set the fontsize, position and color of the label
        # Set some styling options for the label's box
        plt.text(y[i] + 1.5, i , y[i], fontsize = 9, ha = 'center', va = 'center', color = "black",
                 bbox = dict(facecolor = 'white', alpha = 1, pad = 2))

# Method for creating vertical bar graph
def verticalBarGraph(label):
    
    # Get the count of each category in the column specified by the label
    data = df[label].value_counts()

    
    # Plot a bar graph using the count of each category as the height
    plt.bar(data.index, data.values ,color = "gray", align ='center', alpha=0.5)
    
    # Call add the appropriate method to add label to this graph
    verticalAddLabels(data.index, data.values)  

    # set the Y label, to "# of People"
    plt.ylabel("# of People")   
    
    # set title of the graph to variable label
    plt.title(label)  
    
    # set the y-limit of the bar from 0,100           
    plt.ylim(0,100)           


    # Maximize the window size of the graph
    manager = plt.get_current_fig_manager()
    manager.window.state('zoomed')

    # Display graph
    plt.show()
    
    
# Method for creating horizontal bar graph
def horizontalBarGraph(label):

    # Get the count of each category in the column specified by the label
    data = df[label].value_counts()


    # Plot a bar graph using the count of each category as the height
    plt.barh(data.index, data.values, color="gray", align='center', alpha=0.5)
    
    # Call add the appropriate method to add label to this graph
    horizontalAddLabels(data.index, data.values) 

    # set the Y label, to "# of People"
    plt.xlabel(" # of People")

    # set title of the graph to variable label
    plt.title(label)
    
    # set the x-limit of the bar from 0,100 
    plt.xlim(0,100)    
    
    # Maximize the window size of the graph
    manager = plt.get_current_fig_manager()
    manager.window.state('zoomed')

    # Display graph
    plt.show()


#pi graph code
def pieChart(label):
    
    # Get the count of each category in the column specified by the label
    data = df[label].value_counts()
    
    # set title of the graph to variable label
    plt.title(label)


    # Plot a pie graph using the count of each category as the height
    plt.pie(data.values, autopct='%1.1f%%', startangle=15, textprops={'fontsize': 10})

    total = sum([len(i) for i in data.index])
    average = total/len(data)
    
    #If statment to check where place legend box. If legends are too big it placed under the pie chart, if not then place to the right of the pie chart
    if average > 30:
        plt.legend(data.index, loc='lower center', bbox_to_anchor=(0.52,-0.125), fontsize='medium')
    else:
        plt.legend(data.index, loc='center right', bbox_to_anchor=(1.60, 0.5), fontsize='large')

   
    # Maximize the window size of the graph
    manager = plt.get_current_fig_manager()
    manager.window.state('zoomed')
    
    # Display graph
    plt.show()


if __name__ == "__main__":
    
    
    #setup the graph properties
    pd.options.display.max_rows = 9999
    pd.options.display.max_columns = 9999
    df = pd.read_csv("chatGPTSurveyGroup.csv") 

    print(df.info())
    
    #pieChart("Which of the following best describes your ethnicity?")
    verticalBarGraph("Which age group do you fall in?")
    verticalBarGraph("What do you identify as (gender)?")
    pieChart("What path of education are you pursuing currently?")
    pieChart("Which of the following best describes your current field of study or profession?")
    pieChart("Which of the following best describes your ethnicity?")
    horizontalBarGraph("Have you used ChatGPT before?")
    verticalBarGraph("In the event that \"Yes\" was your response to the previous question, how would you evaluate your ChatGPT experience?")

    horizontalBarGraph("Should ChatGPT be permitted for use in academic settings?")

    pieChart("If \"Yes,\" choose the option(s) which gives the best explanation for why.")
    pieChart("If \"No,\" choose the option(s) which gives the best explanation for why.")

    verticalBarGraph("Do you think ChatGPT is beneficial in most fields of study?")

    pieChart("How do you think ChatGPT will impact society?")
    pieChart("Do you believe that the use of ChatGPT and other AI tools would harm Academia?")

    
