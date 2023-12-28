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
Install the SiGML Player (according to search results):  
1. https://vh.cmp.uea.ac.uk/index.php/Driving_the_SiGML_Player_App
2. https://vhg.cmp.uea.ac.uk/tech/jas/vhg2020/

#### Notes from original author:
The program can be used by making a call to main.py with a glossed NGT sentence. The JASigning avatar will sign the sentence in NGT
as long as the SiGML Player is running.

#### Possible flags to add to call to main.py:
- spell  
Fingerspells complete input  
Usage: `main.py spell 'string'`
- explain  
Explains the SiGML-code of the sign  
Usage: `main.py explain 'gloss'`  
- add  
Adds sign to the dictionary  
Usage: `main.py add 'gloss' 'HamNoSys-SiGML' 'SAMPA'`
