# stocksmart 
<h4><i>Live News and Report from NSE</i></h4>
<!-- TABLE OF CONTENTS -->
<details open="open">
  <summary>Table of Contents</summary>
  <ol>
   <li>
      <a href="#steps-to-run-in-your-machine">Steps to run in your machine</a>
    </li>
    <li>
      <a href="#objective-behind-the-project">Objective behind the Project</a>
    </li>
<!--    <li><a href = "#features">Features</a></li> -->
   <li><a href="#features-description">Features Description</a></li>
      <ul>
        <li><a href="#live-news">NSE Related Live News</a></li>
        <li><a href="#nse-200-constituents">NSE 200 Constituents</a></li>
        <li><a href="#index-level-reporting">Index Level Reporting</a></li>
      </ul>
   <li><a href="#home-page">Home Page</a></li>
      <ul>
        <li><a href="#landing-page">Landing Page</a></li>
        <li><a href="#about-section">About Section</a></li>
      </ul>
    <li><a href="#future-scope">Future Scope</a></li>
  </ol>
</details>

<!-- INSTALLATIONS -->

## Steps to run in your machine
To install and run the project on your local system, follow the given steps:

#### Run the following commands

1. Clone this repository
```
git clone https://github.com/riddhic15/CitiProject.git
```
2. Change directory to safeHome
```
cd CitiProject
```
3. Make sure you have python and pip are installed in your system. Do this with the following commands:
```
python --version
pip --version
```
If they are installed, their version will be displayed. To avoid errors in installing other libraries, upgrade your pip using the following command:
```
pip install --upgrade pip
```
Install all other dependencies that have been used in the project using pip:
```
pip install -r requirements.txt
```
4. Run the app
```
flask run
```

Run the flask run CLI command with debug mode enabled, which will automatically enable the reloader. As of Flask 2.2, you can pass --app and --debug options on the command line.
```
$ flask --app main.py --debug run
```

## Objective Behind the Project

With StockSmart, all the key highlights related to the stock market are now just a click away. Important information related to NSE 200 Index constituents, sectors and index level reporting are delivered to help you analyse the market status. We provide live insights on the current market trends to assist you in wisely trading between stocks.

Thus, our objective is to help sales traders make profitable decisions with the help of the insights delivered at the start of the trading day.

<!-- ## Features
Some of the features included in this app are: -->

## Features Description

### Live News

Extracts live important information for NSE200 Index constituents and any other notable sectoral information at Start of Day for sales traders to make quicker and productive
decision. 
![Screenshot (446)](https://user-images.githubusercontent.com/58457452/210135314-f13f7a75-d1b8-4ef7-8775-fa90952a05fe.png)
![Screenshot (451)](https://user-images.githubusercontent.com/58457452/210135341-deb93a80-d25f-41df-b556-a57402542b9b.png)

### NSE 200 Constituents

List of all stocks in NSE 200 index

![Screenshot (447)](https://user-images.githubusercontent.com/58457452/210135367-99a05479-d819-4344-abf9-c372106de6f8.png)

### Index Level Reporting

![Screenshot 2023-01-02 223802](https://user-images.githubusercontent.com/83594113/210261563-26178de3-b9ee-44ec-9769-ca4fbb366f50.jpg)
![Screenshot 2023-01-02 223836](https://user-images.githubusercontent.com/83594113/210261602-ef9ebf44-2288-4c8a-90f5-fee5f7861497.jpg)
![Screenshot 2023-01-02 223857](https://user-images.githubusercontent.com/83594113/210261614-ef30bd60-997c-421d-b588-4d331c6ded91.jpg)


## Home Page

### Landing Page

![image](https://user-images.githubusercontent.com/58457452/210134933-41cea491-5d1f-4865-b89e-18373b7f8338.png)

### About Section

![about-us](https://user-images.githubusercontent.com/58457452/210272075-60a38d8f-ba9b-41d6-af59-c4a1c89dde24.png)

## Future Scope

1. <u>Implementation of email feature</u>: We can implement the email feature with a input field where the user can enter their email address and upon clicking send the entire report his recieved by them on their email. Presently, the smtp feature by gmail has been disabled, hence we couldn't add this feature. We aim to look at other alternatives and work on it.

2. <u>Fetch and display more data</u>: Additional data can be fetched from the web using advanced scrapping techniques. We tried BeautifulSoup on many websites, but due to the sensitive nature of trading data, we couldn't fetch the data. We aim to work upon it as well.

3. <u> Chatbot-feature</u>: A chatbot integration makes the website user-friendly and gives them a personalized experience. A chatbot can definitely help with basic question and a walk through the web pages.

<h4>Link to the website: <a href="http://stocksmart.pythonanywhere.com/">stocksmart</a></h4>