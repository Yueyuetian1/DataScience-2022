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

## My Notebook

* [Homework1](https://github.com/Yueyuetian1/DataScience-2022/blob/main/HW1/HWEEK1.ipynb)
* [Homework2](https://github.com/Yueyuetian1/DataScience-2022/blob/main/HW2/HWEEK2.ipynb)
