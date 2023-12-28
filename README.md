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
