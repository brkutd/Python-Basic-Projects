# ASA (v1.0) 
**Automatic Sentiment Analyser** allows to investigate any kind of text in terms of its emotional markedness.
This program calculates the sentiment of a given text and presents it to the user along with a pie chart.

## Downloading _ASA_
_Automatic Sentiment Analyser_ is available to download from [THIS](https://github.com/brkutd/Python-Basic-Projects/tree/main/Automatic-Sentiment-Analyser)
GitHub repository. Before you run the main program, make sure all the downloaded files are in the same folder.  

Files needed to run _ASA_ properly:
* <i>asa_project.py</i> (main file)
* <i>data_words.json</i> (file with crucial lists for analysis)

## Preparing to run _ASA_
To run the program, you should prepare a _txt_ file with the text you want tto analyse. [Project Gutenberg](https://gutenberg.org/)
might be a good place to look for books with no copyrights. The file might be also a scraped text from a webpage, 
open the [<i>asa_for_html.ipynb</i>](https://github.com/brkutd/Python-Basic-Projects/blob/main/Automatic-Sentiment-Analyser/asa_for_html.ipynb) file to see an example of such usage.

**1. Open the folder where you store two previously mentioned files**  

![](https://i.ibb.co/jHM5S8y/1.png)
   
**2. Paste your _txt_ file into the same folder** 

![](https://i.ibb.co/KzgLF4n/2.png)
   
**3. You are ready to open the <i>asa_project.py</i> file. The file can be opened via terminal command line or
manually with the use of a Python IDE like [_PyCharm_](https://www.jetbrains.com/pycharm/)** 

![](https://i.ibb.co/9WV6tkr/3.png)

## Running _ASA_
Assuming that _PyCharm_ was used to open the file. The main screen should contain the code of the program.  

![](https://i.ibb.co/ngN8SjF/4.png)

**1. Right-click on the tab called <i>asa_project.py</i>**

![](https://i.ibb.co/nPKKCMB/4.png)  
   

**2. Click on <i>Run 'asa_project'</i>**  

![](https://i.ibb.co/gSf7jNq/5.png)  
   
## Working with _ASA_
When the program is running, a run tool window should appear at the bottom of the main screen.  

![](https://i.ibb.co/6Z1jSDH/6.png)  
**Now, you are in _ASA_!**
   
The program asks now for an input of the file we have pasted into the main folder. Let's write the name of the file: _dracula_.
Use the **ENTER** key to input a written text to the program.

![](https://i.ibb.co/KwqzFxz/7.png)  

After this, the program will ask two questions. If we want to analyse the text with the use of a keyword and if
we want to include stopwords. This time, we will use a keyword _Dracula_ and not include stopwords as usually they
slow down the process.  

![](https://i.ibb.co/WW3s6sM/8.png)  


As the text is quite long, it might take a second to prepare the analysis. The output should look like this:  
![](https://i.ibb.co/RQ69cB7/9.png)  

Now, you can close the program by writing _'n'_ and get access to two new files in the main folder of the program.  

![](https://i.ibb.co/D5x17Jm/10.png)  

The file _analysis_ includes the output from the run tool, the _plot_ file is a image of two plots with some statistics. The same plots should
also appear in the main _PyCharm_ window automatically.

![](https://i.ibb.co/3Rcy8Gs/plot.png)


## FINISHED
That is all! Using _ASA_ is fairly simple and should not cause any problems.
