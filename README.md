
# Linkedin Web Scraper

### Description:

A python script based web scraper that scrapes the headcount growth insights from a linkedin profile and exports this data as a csv file called 'IndustryTrends.csv',The script requires the file 'links.csv' in to be in the same folder and the file must contain the names and links of the accounts data is to be collected from. When the script is run selenium will open the browser using chrome driver, login using the credentials provided, open the links, extract the data, export the data and then close the browser. As of the script is limited to Google Chrome hence it is neccessary to have it installed.

### Project Files

- linkedinwebscraper3,2.py
- README.md
- Requirements.txt
- links.txt
- Chromedriver.exe
- IndustryTrends.csv (Output of the script)

it is important that 'links.csv','Chromedriver.exe' are in the same directory as linkedinwebscraper3,2.py

### Usage

To intialise the code before using the script for the first time certain steps need to me completed. It is only neccessary to do these the first time the code is run:

Install the required libraries

```
pip install -r requirements.txt
```

Add your linkedin username and password instead of the placeholder text in

```
username = wait.until(EC.presence_of_element_located((By.ID, "username")))
username.send_keys("Insert username here")
pword = wait.until(EC.presence_of_element_located((By.ID, "password")))
pword.send_keys("Insert password here")
```

Insert the names and links of the accounts to be scraped in the file "links.csv".
Names in the first coloumn and links in the second.

Once these steps are complete the script can be run. A high speed network connection is recommended but not neccesary. Using the script too many times within a day can trigger linkedin's captcha test.

### Functioning

The script consists of four functions.

The login function is responsible for launching the browser and logging into google chrome. If a valid username and password is not inserted in the placeholder text the script will raise an exception and quit. This function takes the driver as a parameter. returns no value.

The openprofile function is responsible for loading the accounts and scrolling to the bottom of the page. It takes the driver and profile url as a parameter. The openprofile function is called in the storedata function. returns no value. This function is carried out in the main body of the file. Raises an exception if it fails to load the page.

The extract function is responsible for looking at the page source code, parsing the html, identifying the required text and extracting the headcount growth value. It returns this value as a positive number if theres an increase in growth and a negative number if theres a decerease in growth. It takes the driver as a parameter. This function is called in the storedata function. An exception is raised and the script is exited if an error occurs during the extraction.

The storedata function is resposible for calling the openprofile and extract functions. The function also is responsible for reading the links from 'links.csv' and appending the gathered data to 'IndustryTrends.csv'. If the 'IndustryTrends.csv' is not found a newfile will be created with the company names in the first row and the growth values in the rows below them. Names and Trend are both stored in their seperate lists. It takes the driver as a parameter. This function is carried out in the main body of the file. This function returns no values. An exception is raised if 'links.csv' is not found in the directory.

### Libraries

- selenium        4.19.0
- beautifulsoup4  4.12.2
- time
- os
- csv

### Author

Arnav Pilankar






