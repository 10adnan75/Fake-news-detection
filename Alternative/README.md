# Fake News Detection using Scikit-learn

Using the sci-kit package from Python, several natural language processing techniques and machine learning algorithms were employed to classify false news stories in this research.

## I. Getting Started

For development and testing reasons, follow these instructions to get a copy of the project up and running on your local system. Notes on how to deploy the project on a live system can be found in the deployment section.

### A. Prerequisites

What you'll need to install the software, and how to do it:

1. Python 3.9 
   - This setup requires that you have Python 3.9 installed on your PC. To get Python, go to https://www.python.org/downloads/. Once you've downloaded and installed Python, you'll need to set up PATH variables (if you want to run a Script directly, see the *how to run software section* for more information). See https://www.pythoncentral.io/add-python-to-path-python-is-not-recognized-as-an-internal-or-external-command/ for more information.
   - Setting up the PATH variable is optional; you can run the application without it, and more information is provided below.
2. The second and more convenient way is to download Anaconda and run the commands using its anaconda prompt. To get Anaconda, go to https://www.anaconda.com/download/.
3. After you've installed python or anaconda using the procedures above, you'll need to download and install the following three packages.
   - Sklearn (scikit-learn)
   - numpy
   - scipy
   
  - If you want to install Python 3.9, use the command prompt/terminal to run the commands listed below.
   ```
   pip install -U scikit-learn
   pip install numpy
   pip install scipy
   ```
   - If you've decided to use Anaconda, use the instructions below in the Anaconda prompt to install these packages.
   ```
   conda install -c scikit-learn
   conda install -c anaconda numpy
   conda install -c anaconda scipy
   ```  

### B. Dataset 

The LIAR dataset was used for this project, and it consists of three .tsv files for test, train, and validation. The data files utilised in this study are described in the following sections.
	
LIAR: A BENCHMARK DATASET FOR FAKE NEWS DETECTION

William Yang Wang, "Liar, Liar Pants on Fire": A New Benchmark Dataset for Fake News Detection, to appear in Proceedings of the 55th Annual Meeting of the Association for Computational Linguistics (ACL 2017), short paper, Vancouver, BC, Canada, July 30-August 4, ACL.

The original dataset had the following 13 variables/columns for the train, test, and validation sets:

* Col 1: the ID of the statement ([ID].json)
* Col 2: the label (Label class contains: True, Mostly-true, Half-true, Barely-true, FALSE, Pants-fire)
* Col 3: the statement
* Col 4: the subject(s)
* Col 5: the speaker
* Col 6: the speaker's job title
* Col 7: the state info
* Col 8: the party affiliation
* Cols 9-13: the total credit history count, including the current statement
* Col 9: barely true counts
* Col 10: false counts
* Col 11: half true counts
* Col 12: mostly true counts
* Col 13: pants on fire counts
* Col 14: the context (venue / location of the speech or statement)

Only two variables from the original dataset were considered for this categorization to keep things simple. The additional variables can be added later to add more complexity and improve the features.

The columns used to build three datasets that were used in this study are listed below.

* Col 1: Statement (News headline or text)
* Col 2: Label (Label class contains: True, False)
 
You'll see that the newly formed dataset only includes two classes, compared to six in the original dataset. The method for lowering the number of classes is shown below.

* Original    --  New
* True	     --	True
* Mostly-true -- 	True
* Half-true	  -- 	True
* Barely-true -- 	False
* False		  -- 	False
* Pants-fire  -- 	False

The datasets used in this project are named train.csv, test.csv, and valid.csv and are available in the repository. The original datasets in tsv format can be found in the "liar" folder.

## II. File Description

#### DataPrep.py
All of the routines required to process all of the input documents and texts are contained in this file. After reading the train, test, and validation data files, tokenizing and stemming were performed. Some exploratory analysis was done, including response variable distribution and data quality checks like null or missing values, among other things.

#### FeatureSelection.py
This file made use of feature extraction and selection methods from the sci-kit learn python packages. For feature selection, a straightforward bag-of-words and n-grams approach was used, followed by tf-tdf weighting for term frequency. The characteristics were extracted using word2vec and POS tagging, albeit POS tagging and word2vec aren't being used right now.

#### classifier.py
All of the classifiers for predicting the detection of bogus news have been built here. Different classifiers are fed the extracted features. From sklearn, Naive Bayes, Logistic Regression, Linear SVM, Stochastic gradient descent, and Random forest classifiers were employed. All of the classifiers utilised each of the extracted features. The f1 score was compared and the confusion matrix was evaluated after fitting the model. After fitting all of the classifiers, the two best-performing models were chosen as candidate models for detecting fake news. GridSearchCV methods were used to undertake parameter tuning on these candidate models and the best performing parameters for these classifiers were identified. Finally, the chosen model was utilized to detect bogus news using the likelihood of truth. The top 50 characteristics were taken from the term-frequency tfidf vectorizer to determine which terms are the most common and essential in each class. Precision-Recall and learning curves have also been utilized to see how the training and test sets perform as the amount of data in the classifiers grows.

#### prediction.py
```Logistic Regression``` was the final and highest performing classifier, and it was saved on disk as ```final_model.sav```. This model will be copied to the user's machine and utilized by the prediction.py file to classify bogus news once you close this repository. It takes a user-supplied news story as input, then applies the model to produce a final categorization output, which is displayed to the user along with the likelihood of truth.

## III. Performance

The learning curves for our candidate models are shown here.

**Logistic Regression Classifier**

<p align="center"><img width="550" height="450" src="https://github.com/nishitpatel01/Fake_News_Detection/blob/master/images/LR_LCurve.PNG"></p>

**Random Forest Classifier**

<p align="center"><img width="550" height="450" src="https://github.com/nishitpatel01/Fake_News_Detection/blob/master/images/RF_LCurve.png"></p>

## IV. Installation

A collection of examples that show you how to set up a development environment step by step.

1. The first step is to clone this repository and save it to a folder on your local machine. To do so, type the following command on the command prompt or git bash.

```
$ git clone https://github.com/10adnan75/Fake-news-detection.git
```

2. This will replicate your machine's data source file, application files, and model.

3. If you've decided to install Anaconda, follow the steps below.

     - All of the files are then saved in a folder on your computer. If you followed the steps in the ```Prerequisites``` section to install Anaconda, then open the conda prompt, change the directory to the folder where this project is saved on your machine, then type the command below and hit enter.

	```
	cd C:/your cloned project folder path goes here/
	```
	
     - Once inside the directory, enter the command below in anaconda prompt to open the ```prediction.py``` file.
     
	```
	python prediction.py
	```
	
     - After pressing enter, the application will prompt you for an input, such as a piece of information or a news headline that you want to double-check. After you've pasted or typed a news headline, hit enter.

     - Once you press enter, the program will take user input (a news headline) and classify it into one of two categories: "True" or "False". In addition to identifying the news title, the model will assign a probability of truth to it.

4. Follow the procedures below if you choose to install Python (and did not set up a PATH variable for it).

    - Meanwhile, you should clone the project to a folder on your computer. By typing the following command in the command prompt, you can change the directory to the project directory.
    
    ```
    cd C:/your cloned project folder path goes here/
    ```
    
    - Find ```python.exe``` on your computer. This can be found using the search bar in Windows Explorer.
    
    - Once you've found the ```python.exe``` path, write the complete path of it, followed by the entire path of the project folder, ending with ```prediction.py```. If your ```python.exe``` is at ```c:/Python39/python.exe``` and your project folder is at ```c:/users/user_name/desktop/fake news detection/```, then your command to launch the program will be as follows.
    
    ```
    c:/Python39/python.exe C:/users/user_name/desktop/fake_news_detection/prediction.py
    ```
   
    - After pressing enter, the application will prompt you for an input, such as a piece of information or a news headline that you want to double-check. After you've pasted or typed a news headline, hit enter.

    - Once you press enter, the application will take user input (a news headline) and classify it into one of two categories: "True" or "False". In addition to identifying the news title, the model will assign a probability of truth to it. Wait for the model to classify the given statement, which may take a few seconds.

5.  If you've decided to install Python (and have already established the PATH variable for ```python.exe```), then follow these steps.

    - Open a command prompt and perform the following command to change the directory to the project folder as specified earlier.
    
    ```
    cd C:/your cloned project folder path goes here/
    ```
    
    - Run the command shown below
   
    ```
    python.exe C:/your cloned project folder path goes here/
    ```
    
    - After pressing enter, the application will prompt you for an input, such as a piece of information or a news headline that you want to double-check. After you've pasted or typed a news headline, hit enter.

    - Once you press enter, the program will take user input (a news headline) and classify it into one of two categories: "True" or "False". In addition to identifying the news title, the model will assign a probability of truth to it.

## V. Scope

As can be seen, the best-performing models had a f1 score in the 70's. This is due to the small amount of data which was utilized for training and the simplicity of the models. More feature selection approaches, such as POS tagging, word2vec, and topic modeling, could be added in future iterations.  The size of the training data could be increased as well. In the future, this research could be expanded to include these approaches in order to improve the accuracy and performance of the models.
