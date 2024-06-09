# Teodora
Teodora is a rule-based chatbot with the purpose of helping tourists discover Ravenna. Teodora allows you to find out everything you want to know about the history, traditions, monuments and more generally everything that may be useful if you want to explore the magnificent Ravenna.

<html>
<body>
    <div style="display: table; width: 100%; height: 100vh; text-align: center;">
        <div style="display: table-cell; vertical-align: middle;">
            <img src="https://github.com/annavignoli/Teodora/assets/172110774/2ca52610-a4e6-410d-8055-27a29ce425b70" width="613" height="500" alt="Descrizione dell'immagine">
        </div>
    </div>
</body>
</html>

The chatbot rules were developed from an interview with more than 100 people in order to collect many possible questions that a tourist might ask with as many conversational nuances as possible. 
The software has a graphical user interface to make the user experience as natural and user-friendly as possible. Chats between Teodora and users are also saved locally so that conversations can be reviewed and information is not lost. 

### How to install and run Teodora on Windows
To run Teodora locally, a few steps are required. Download the folder containing all the files and save it wherever you like on your PC. In order to run the program you need to install the libraries necessary for its operation. These are collected in the requirements.txt file. To install them, open the terminal in the downloaded folder and type the command:

```
pip install -r requirements.txt
```

Once you have finished this operation and every other time you want to run the program, simply open the terminal in the folder and run the command:

```
python Teodora.py
```

Once you have finished using the program, the chats are saved locally within the *Chat* folder.
