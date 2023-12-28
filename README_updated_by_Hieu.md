## Updated note and install guide - Hieu
1. Create virtual environment with pip or conda for **Python 3.6**
2. Navigate to the project directory and to install dependencies:   
`pip install -r requirements.txt`
3. In terminal, to start, call:  
`python main.py spell 'Hello I am watching TV'` (the string can be replaced with different expression of your use)  
4. Current work:  
- A sigml file is created to express the input string  
- This file is saved in the newly created folder named `temp_files_storage`
- This file is sent to port 8052 for an opening SiGML Player  

### **_The problem now: No SiGML Player is opening and listening on port 8052._**


# thesisNGT
This program was developed and tested using Python 3.6.1 on Ubuntu 16.04.6.
#### Additional packages that must be installed:
 <ul>
  <li>spaCy</li>
  <li>nl_core_news_sm (pertains to spaCy, but needs to be downloaded separately)</li>
</ul>

#### Files included in download:
<ul>
<li><i>main.py</i><br>Signs the input using the JASigning avatar<br></li>
<li><i>sign.py</i><br>Contains functions for creating a Sign object for the provided gloss<br></li>
<li><i>functionsGrammar.py</i><br>Contains functions for pre-processsing the sentence<br></li>
<li><i>functionsMain.py</i><br>Contains functions for processing the sentence<br></li>
<li><i>functionsAux.py</i><br>Contains functions that are used in sign.py or offer extra functionality<br></li>
<li><i>sendsigml.py</i><br>Sends SiGML files to the avatar<br></li>
<li><i>dictFile.py</i><br>Contains the dictionary of encoded NGT signs available to the avtatar<br></li>
<li><i>HamNoSysDict.py</i><br>Contains a dictionary of all known HamNoSys notations and their respectve categories<br></li>
<li><i>SiGML-Player.AppImage</i><br>Contains the JASigning avatar for linux<br></li>
<li><i>SiGML-Player.app/i><br>Contains the JASigning avatar for OSX<br></li>
<li><i>SiGML-Player.exe</i><br>Contains the JASigning avatar for windows<br></li>
</ul>

The program can be used by making a call to main.py with a glossed NGT sentence. The JASigning avatar will sign the sentence in NGT
as long as the SiGML Player is running.

Install the SiGML Player:  
1. https://vh.cmp.uea.ac.uk/index.php/Driving_the_SiGML_Player_App
2. https://vhg.cmp.uea.ac.uk/tech/jas/vhg2020/

#### Possible flags to add to call to main.py:
<ul>
<li><i>spell</i><br>Fingerspells complete input<br><b>Usage: main.py spell 'string'</b></li>
<li><i>explain</i><br>Explains the SiGML-code of the sign<br><b>Usage: main.py explain 'gloss'</b></li>
<li><i>add</i><br>Adds sign to the dictionary<br><b>Usage: main.py add 'gloss' 'HamNoSys-SiGML' 'SAMPA'</b></li>
</ul>
