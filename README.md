Closest Match Finder
==
Closest Match Finder is a simple Streamlit app that allows users to find the closest match to a given input text from a predefined array of items. It uses fuzzy string matching algorithms to calculate the similarity between the input text and each item in the array, and returns the closest match along with its similarity score.


Getting Started
===
To run the app locally, make sure you have Python installed. You can install the required dependencies using pip:

```bash
pip install -r requirements.txt
```
Once the dependencies are installed, you can run the app using the following command:

```bash
streamlit run closest_match_app.py
```
Usage
===
+ Enter a text in the text input box.
+ Press Enter or click outside the text input box to trigger the search.
+ The app will display the closest match from the predefined array of items along with its similarity score.

Dependencies
===
+ Streamlit: 0.88.0
+ fuzzywuzzy: 0.18.0
+ python-Levenshtein: 0.12.2
  
Contributing
===
Contributions are welcome! If you have any suggestions, improvements, or feature requests, please open an issue or submit a pull request.

Conclusion
===
Closest Match Finder provides a user-friendly interface for finding the closest match to a given input text. It can be used in various applications such as data cleaning, search functionality, and more. We hope you find it useful and welcome any feedback or contributions to further improve the app.

