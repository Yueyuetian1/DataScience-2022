# DataScience-2022

## HW1 Background
*Ernest Hemingway on Writing* is an assemblage on the nature of writing from the great writer Hemingway. In order to create one data visualization about Hemingway text, I drew a word cloud diagram about the book using python, as shown in the figure below.

![wordCloudPic](https://user-images.githubusercontent.com/96498688/151200165-7d246d24-4390-4b58-b50e-884ee52d1b77.png)

Some words appear very frequently in the book, but they do not well represent the main contents of the book, such as "he", "you" and "I". These common words are deleted as stop words.

After deleting the stop words, the word frequency was counted and the word cloud diagram of the book was drawn. As can be seen from the word cloud diagram, the three main keywords of this book are: "write", "writing" and "good". This is also in line with the real theme of the book: **writing**.

On the other hand, it can be seen that the names in this book do not appear frequently, indicating that this book is not a novel or biography. If you want to find the key words and topics of a book or a paragraph of text quickly, you can draw a word cloud diagram.

## HW2 Background
### 1. Scrape all of Hemingway’s writing
Using python, I scraped all of Hemingway's writing from the specified web page.The 6 books are saved in TXT format in the Heimingway TXT folder of the code warehouse. After obtaining the data, exploratory data analysis was carried out. As can be seen from the picture, the number of words in each of the six books is more than two thousand words. *The old man and the sea* are Hemingway's most famous works. The number of words in this book is the least among the six books. It can be seen from Wikipedia that this is a novella.

![wordNums](https://user-images.githubusercontent.com/96498688/153167170-52f0045b-e7d9-47c9-b958-7f54817276ce.png)

### 2. Data Visualization
Next, try to calculate the text similarity to analyze the content of these six books. With the help of Spacy module, the text similarity of pairwise combinations of six books is calculated. The heat map is drawn through the data visualization module, as shown in the figure below.

![heatMap](https://user-images.githubusercontent.com/96498688/153167260-e7bd2544-18a9-4bb4-801c-072f0afdac09.png)

From the figure, we can see the text similarity of the six books. For example, the text similarity between sun also rises and the old man and the sea is 0.9. The text similarity of Hemingway's works is more than 0.9, so the first suggestion is given:

If you want to be a good writer, it may be a good choice to keep your writing style as unchanged as possible.

In addition, emotional analysis is carried out on the text sentences of each book. Compound is the compound result of emotion analysis. The value range is - 1 to 1. The larger the compound, the more positive the sentence is, and the smaller the compound, the more negative the sentence is. Calculate the average value of the compound of all sentences in each book as the emotion of the book and draw a histogram.

![emotionalAnalysis](https://user-images.githubusercontent.com/96498688/153167225-f63eb12e-c326-459e-a5cd-a8c9bf410585.png)

As we all know, Mr. Hemingway died abnormally. Maybe he was a little negative about life, but we got positive results from his excellent works. Therefore, give a conclusion:

No matter how life is, we should face life with a positive attitude.

## HW3 Background
In order to make unsupervised clustering better, a work of Hemingway is selected as the data source. Here, Hemingway's most famous work *the old man and the sea* is used for data visualization.

### 1. Data visualization using an Unsupervised Machine Learning technique
KElbowVisualizer implements the "elbow" method to help data scientists choose the best number of clusters by fitting the model with a series of values of K. The elbow graph of *the old man and the sea* is drawn, and the number of clusters is 4.

![elbow](https://user-images.githubusercontent.com/96498688/154098485-da661762-c063-4ba6-86d3-2c32055d98aa.png)

The LDA(Latent Dirichlet Allocation) in sklearn is used to unsupervised cluster *the elderly and sea* texts, and the number of topics is set to 4. This graph can be viewed dynamically through the "lda.html" file.

![Cluster](https://user-images.githubusercontent.com/96498688/154098475-865e20c8-85cd-4d2e-9256-6baa79719929.jpg)

In order to make the following 3D plot more convenient, select the first three clusters from the four clusters in the figure for topic analysis. As can be seen from the figure, many of the keywords included in the first topic are related to characters, such as: "he", "man" and "boy". The word of this clustering topic is called "human", which is the word related to the description of characters. If I haven't read the book "the old man and the sea", I can draw a conclusion through this analysis:

This book is a story about men and is described in the third person.

This conclusion is just the narrative style and the gender of the protagonist in "the old man and the sea". Through the analysis of clustering words, the second topic is called "place", and the third topic is called "things"

### 2. 3D plot
Based on the data visualization using unsupervised machine learning technology, 3D plot under three topics are drawn.

![3D](https://user-images.githubusercontent.com/96498688/154098465-8b8e3a72-197f-4e6d-ba24-fdcfe38e33ea.jpg)

Due to the limitations of word, this 3D diagram is statically displayed here, which can be viewed dynamically from the code file of homework3. The figure shows a sentence on the X and Z axes: "he went terrace ask coffee". This sentence is the relationship between "human" and "things", which explains the correctness of our previous topic definition to a certain extent. At the same time, we observe that there are many points on the plane of X axis and Y axis in 3D graph, so a suggestion is given:

The cross description of characters and places in the article may help the work to be better.

## HW4 Background
Through the Google search "find all of the locations that Hemingway live", I found an article introducing the place where Hemingway lived.

### 1. the locations that Hemingway lived
Hemingway lived in seven places. He was born in Oak Park. He and his wife lived in Paris and wrote a lot there. From 1923 to 1927, he visited Pamplona, Spain every year. As a war reporter, he lived in Madrid and surrounding areas. Hemingway and his third wife lived in Havana for 22 years and wrote about the old man and the sea in Havana.
The seven places and longitude and latitude are sorted through the Internet. In the "location.py" file in homework 4, you can see the correspondence of 7 cities and longitude and latitude.

### 2. the TSP solution that finds the shortest distance
According to the longitude and latitude of the seven cities, the distance between the seven cities is calculated by pairwise combination, and the distance relationship between the cities is obtained and stored in the "routes.py" file in homework 4.
Through the distance relationship, the TSP solution can be calculated and drawn in HTML, and the web service is provided by the flask framework.
Run the "app.py" file, start the web service, and then visit “ http://127.0.0.1:8080/greedy/1000 ”, you can get and display the map "map.html". "1000" in the web page access address is the number of iterations, which can be adjusted to get a better TSP solution. The screenshot of the map is shown below:

![screenshot](https://user-images.githubusercontent.com/96498688/155317188-dcf98f4b-3e0a-40eb-af7e-13a00c9b5340.jpg)

Through the map, we can see that Hemingway lived on two continents, and Hemingway's life experience is relatively rich.Therefore, a suggestion is given:

Traveling ten thousand miles is as important as reading ten thousand books.

By clicking the red label at the top of the map, you can view the TSP path under the current number of iterations.

Path: KETCHUM, IDAHO, America-->Oak Park, Illinois, America-->Key West, Florida, America-->Havana, Cuba-->MADRID, Spain-->PAMPLONA, Spain


* [article1](https://www.nytimes.com/2015/10/04/travel/places-where-hemingway-lived-or-traveled.html)

## My Notebook

* [Homework1](https://github.com/Yueyuetian1/DataScience-2022/blob/main/HW1/HWEEK1.ipynb)
* [Homework2](https://github.com/Yueyuetian1/DataScience-2022/blob/main/HW2/HWEEK2.ipynb)
* [Homework3](https://github.com/Yueyuetian1/DataScience-2022/blob/main/HW3/HWEEk3.ipynb)
