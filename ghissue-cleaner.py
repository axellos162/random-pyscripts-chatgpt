'''a Python script that takes an input of Github issues, 
extracts the natural language text from the issues that use a specific template, 
cleans up the text, and stores the cleaned up issues in a CSV file with one issue per row.'''

import pandas as pd
import regex as re
import nltk
from nltk.corpus import stopwords
from nltk.stem import WordNetLemmatizer
nltk.download('stopwords')
nltk.download('wordnet')

# read the input file with Github issues
input_file = 'github_issues.txt'
with open(input_file, 'r', encoding='utf-8') as f:
    issues = f.readlines()

# create a dataframe to store the cleaned up issues
df = pd.DataFrame(columns=['Issue'])

# define the regular expression pattern for the issue template
pattern = r'\*\*Describe the bug\*\*\n\n(.+?)\n\n'

# define the stopwords and lemmatizer for cleaning the natural language text
stop_words = set(stopwords.words('english'))
lemmatizer = WordNetLemmatizer()

# loop through each issue and clean up the natural language text
for issue in issues:
    # extract the text using the regular expression pattern
    match = re.search(pattern, issue, re.DOTALL)
    if match:
        text = match.group(1)
        # clean up the text
        text = re.sub(r'[^\w\s]', '', text) # remove punctuation
        text = re.sub(r'\d+', '', text) # remove numbers
        text = text.lower() # convert to lowercase
        tokens = nltk.word_tokenize(text) # tokenize
        tokens = [t for t in tokens if t not in stop_words] # remove stopwords
        tokens = [lemmatizer.lemmatize(t) for t in tokens] # lemmatize
        text = ' '.join(tokens)
        # add the cleaned up issue to the dataframe
        df = df.append({'Issue': text}, ignore_index=True)

# write the dataframe to a CSV file
output_file = 'cleaned_github_issues.csv'
df.to_csv(output_file, index=False)


''' This script assumes that the input file github_issues.txt contains the raw Github issues, with each issue separated by a newline character. 
The script also assumes that the issue template starts with the bold text "Describe the bug" and ends with two newline characters.

The cleaned up issues are stored in a dataframe with a single column named "Issue". 
The script loops through each issue, extracts the natural language text using the regular expression pattern, 
and applies several cleaning steps using the NLTK library. The cleaned up issues are then appended to the dataframe.

Finally, the dataframe is written to a CSV file named cleaned_github_issues.csv, 
with one issue per row and no index column.'''