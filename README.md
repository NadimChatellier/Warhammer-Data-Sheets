Warhammer 40k Data Sheets Web Application
Welcome to the Warhammer 40k Data Sheets Web Application! This project is a comprehensive platform designed for Warhammer 40k enthusiasts to create, download, and share custom datasheets, develop strategies, and organize albums. Our advanced filtering systems allow users to easily navigate and find the content they need. This is my first real project so please be nice :).

for those unfamiliar this is what a datasheet would look like:
https://preview.redd.it/has-anyone-made-a-blank-template-for-the-new-datasheet-v0-5bdxapvgu8sa1.jpg?width=640&crop=smart&auto=webp&s=a79b70d7795fef55f119b6a01be36f7b56d6eb0e

the general idea and ultimate goal of the application is to present data to the user while keeping what's necessary to the user during a game only when it is required, the exercise is primarily to present quite dense information in as clear a manner as possible.

Features
Create Custom Datasheets: Design and personalize datasheets for your Warhammer 40k units.
Download & Share: Easily download datasheets or share them with the community.
Strategy Creation: Develop and manage strategies, specifying which abilities affect which units.
Albums: Organize your datasheets and strategies into albums for easy access.
Advanced Filtering:
Faction Filtration: Filter datasheets by faction.
Strategy Filtration: Find strategies based on unit abilities and effects.

Prerequisites
Python 3.x
Flask and other dependencies 
Installation


Clone the Repository:
git clone https://github.com/Mithrildagger/Warhammer-Data-Sheets.git
cd WH40k


Set Up Virtual Environment:
python -m venv venv
Activate Virtual Environment:

On Windows:
venv\Scripts\activate


On macOS/Linux:
source venv/bin/activate


Set Up Environment Variables:
Create a .env file in the root directory:

makefile
FLASK_APP=app.py
FLASK_ENV=development
SECRET_KEY=your_secret_key


Run the Application:
flask run
The application will be available at http://127.0.0.1:5000.

Usage
Once the application is running, you can:

Create Datasheets: Navigate to the datasheets section and use the form to create new datasheets.
Explore Strategies: Check out the strategies section to see and create new strategies.
Organize Albums: Use the albums feature to categorize and manage your datasheets and strategies.


TODO:
-Certain changes have to be made to how the form handles data to allow for more flexible data cards
-Aestetics
Setup database to save units 
