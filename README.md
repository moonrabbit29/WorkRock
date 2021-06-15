# WorkRock
## After you clone this repo, follow below instruction to run the App

###  requirements : 
1. Makse sure you have allready install python/other python distribution like conda on your machine :
   * run python --version on your teminal
   * if you allready installed python but coouldn't run the above command then make sure you allready put python on your path variable

2. Create python virtual environtment with some list of packaege provided in requirements.txt
   * If you don't use anaconda you can run this following command (make sure u allready install pip) :  
      * open terminal and change its directory to your cloned repo location
      * pip install virtualenv (skip this if you allready installed virtualenv package)
      * actiavate the python environtment (if you are using windows i suggest you to not using powershell use other terminal like cmd or gitbash or anything else) -> command -> . env/scripts/activate or if u use cmd : cd env/scripts -> then write activate
      * after activating your virtual environtment install the required package by using this command :
      pip install -r requirements.txt

### run the server on development mode :
   #### python manage.py runserver

### run the server on production mode :

   ### python manage.py

### additional information
   default url is localhost:5000
   you can change it in manage.py file 
