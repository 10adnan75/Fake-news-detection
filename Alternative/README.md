# Fake News Detection using Scikit-learn

Using the sci-kit package from Python, several natural language processing techniques and machine learning algorithms were employed to classify false news stories in this research.

### Getting Started

For development and testing reasons, follow these instructions to get a copy of the project up and running on your local system. Notes on how to deploy the project on a live system can be found in the deployment section.

### Prerequisites

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

### Dataset 

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
