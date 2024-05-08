import pandas as pd
import matplotlib.pyplot as plt

# Method for adding labels for the vertical Bar graph
def verticalAddLabels(x, y):
    for i, val in enumerate(y):
        plt.text(i, val + 2, val, fontsize=9, ha='center', va='center', color="black",
                 bbox=dict(facecolor='white', alpha=1, pad=2))

# Method for adding labels for the horizontal Bar graph
def horizontalAddLabels(x, y):
    for i, val in enumerate(y):
        plt.text(val + 1.5, i, val, fontsize=9, ha='center', va='center', color="black",
                 bbox=dict(facecolor='white', alpha=1, pad=2))

# Method for creating vertical bar graph
def verticalBarGraph(label, df):
    data = df[label].value_counts()
    plt.bar(data.index, data.values, color="gray", align='center', alpha=0.5)
    verticalAddLabels(data.index, data.values)
    plt.ylabel("# of People")
    plt.title(label)
    plt.ylim(0, 100)
    plt.show()

# Method for creating horizontal bar graph
def horizontalBarGraph(label, df):
    data = df[label].value_counts()
    plt.barh(data.index, data.values, color="gray", align='center', alpha=0.5)
    horizontalAddLabels(data.index, data.values)
    plt.xlabel("# of People")
    plt.title(label)
    plt.xlim(0, 100)
    plt.show()

# Method for creating pie chart
def pieChart(label, df):
    data = df[label].value_counts()
    plt.title(label)
    plt.pie(data.values, autopct='%1.1f%%', startangle=15, textprops={'fontsize': 10})
    if len(data) > 5:
        plt.legend(data.index, loc='lower center', bbox_to_anchor=(0.52, -0.125), fontsize='medium')
    else:
        plt.legend(data.index, loc='center right', bbox_to_anchor=(1.60, 0.5), fontsize='large')
    plt.show()

if __name__ == "__main__":
    df = pd.read_csv("chatGPTSurveyGroup_64.csv")
    pd.options.display.max_rows = 9999
    pd.options.display.max_columns = 9999

    # Graphs
    verticalBarGraph("Which age group do you fall in?", df)
    verticalBarGraph("What do you identify as (gender)?", df)
    pieChart("What path of education are you pursuing currently?", df)
    pieChart("Which of the following best describes your current field of study or profession?", df)
    pieChart("Which of the following best describes your ethnicity?", df)
    horizontalBarGraph("Have you used ChatGPT before?", df)
    verticalBarGraph("In the event that 'Yes' was your response to the previous question, how would you evaluate your ChatGPT experience?", df)
    horizontalBarGraph("Should ChatGPT be permitted for use in academic settings?", df)
    pieChart("If 'Yes,' choose the option(s) which gives the best explanation for why.", df)
    pieChart("If 'No,' choose the option(s) which gives the best explanation for why.", df)
    verticalBarGraph("Do you think ChatGPT is beneficial in most fields of study?", df)
    pieChart("How do you think ChatGPT will impact society?", df)
    pieChart("Do you believe that the use of ChatGPT and other AI tools would harm Academia?", df)
