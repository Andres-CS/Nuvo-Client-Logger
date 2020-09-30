# **Nuvo Job Register**

------

### Description

Nuvo Job Register (NJR) is a desktop application built to facilitate a Print-Production team workflow. It allows team members to register and store an incoming print job and to calculate the amount of resources needed. 

NJR is built using:

-  Python3, 
- wxPython 4.1 (Phoenix Version)
-  JSON
- SQLite

------

### Visual

<img src="https://raw.githubusercontent.com/Andres-CS/Nuvo-Client-Logger/AppStructure/Media/_DEMO_/Latest_1.PNG" style="zoom: 33%;" />



<img src="https://raw.githubusercontent.com/Andres-CS/Nuvo-Client-Logger/AppStructure/Media/_DEMO_/Latest_2.PNG" style="zoom: 33%;" />



------

### Structure

![](https://raw.githubusercontent.com/Andres-CS/Nuvo-Client-Logger/AppStructure/Media/FolderStructure.PNG)



This project is organized in the following way:

- **Root directory**:

  In it you will find the projects main file, APP.py, which initializes our program by performing a few checks and setups.

- **Client directory**:

  Contains modules that handles client management. 

- **Database directory**:

  Is a package that controls our database. It performs database checks and setups as well as CRUD operations. 

- **GUI directory**:

  This package take care of the entire User Interface.

  - **Form Panel**:

    Handles all related widgets and actions for our input form. 

    This panel is the first panel a user sees when the application is running.

    - **Dialogs**:

      This folders holds all pop-dialogs related to the Form Panel. These will show when data is missing or some action taken may harm the data inputted. 

  - **Records Panel**:

    Its main purpose is to display all stored jobs in the current database.

    It also allows users to search for a specific job according to a set of menus provided.

  - **ConfigGUI**:

    This folder holds JSON files which describe a panels widget organization. 

    These files are used at application start-up to render the application widget layout. 

- **Media:**

  This folder holds static media such as logos and images for UI use.

- **Profiles:**

  This package takes care of managing a resources (printers, type of paper, inks, etc) profile.

------

### Installation

#### Windows

##### Prerequisites:

- Install Python 3.x (https://www.python.org/downloads/)

- Check pip's version and update if necessary

  ```
  > py -m pip --version
  > py -m pip install --upgrade pip
  ```

- Install **virtualenv**

  ```
  > py -m pip install --user virtualenv
  ```

- Go to the directory where your program will reside.

  ```
  > cd C:\path\to\program\folder\
  ```

- Create a virtual environment

  ```
   > virtualenv myenv
  ```

- Activate your venv

  ```
   > myenv\Scripts\activate
  ```

  If you want to know more about Python's Virtual Environment please read https://docs.python.org/3/tutorial/venv.html 

- Now we can install **wxPython**

  ```
  > py -m pip install -U wxPython
  ```

  If you any questions regarding installation of wxPython please read https://wxpython.org/pages/downloads/index.html

##### Clone

- Now that the above has been completed and setup, you can proceed to clone this repo by using any of GitHub's methods:

  HTTPS

  ```
  > https://github.com/Andres-CS/Nuvo-Client-Logger.git
  ```

  SSH

  ```
  > git@github.com:Andres-CS/Nuvo-Client-Logger.git
  ```

  GitHub CLI

  ```
  > gh repo clone Andres-CS/Nuvo-Client-Logger
  ```

------

### Support

Reach out to me at one of the following places!

- Website  at https://japc.me/
- Email at softwareapgm@gmail.com

------

### Licenses 

- **[MIT License](https://opensource.org/licenses/mit-license.php)**
- Copyright 2019-2020 © **[The Nuvo Group](https://thenuvogroup.com/)**

------

### Future Goals

- Integrate [PyInstaller](https://pyinstaller.readthedocs.io/en/stable/#) for executable creation.



