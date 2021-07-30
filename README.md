<h1 align="center">Welcome to American_Job_Center_Scraper 👋</h1>
<p>
  <img alt="Version" src="https://img.shields.io/badge/version-2.0-blue.svg?cacheSeconds=2592000" />
  <a href="https://github.com/mitkotak/American_Job_Center_Scraper" target="_blank">
    <img alt="Documentation" src="https://img.shields.io/badge/documentation-yes-brightgreen.svg" />
  </a>
  <a href="https://github.com/mitkotak/American_Job_Center_Scraper/blob/main/LICENSE" target="_blank">
    <img alt="License: MIT " src="https://img.shields.io/badge/License-MIT -yellow.svg" />
  </a>
</p>

> Webscraper for https://www.careeronestop.org/LocalHelp/AmericanJobCenters/find-american-job-centers.aspx

### 🏠 [Youtube](https://www.youtube.com/embed/JMZxeZKDPZA)

[![Watch the video](https://img.youtube.com/vi/JMZxeZKDPZA/hqdefault.jpg)](https://www.youtube.com/embed/JMZxeZKDPZA)

### ✨ [Demo](https://github.com/mitkotak/American_Job_Center_Scraper)

<p align="center">
  <a href="https://gifyu.com/image/O9F0"><img src="https://s6.gifyu.com/images/in3c8af0db72e17241.gif" alt="in3c8af0db72e17241.gif" border="0" /></a>
</p>

## Usage

Install [Firefox](https://www.mozilla.org/en-US/) if you don't have that already on your computer. If you want to use chrome then uncomment these [lines](https://github.com/mitkotak/American_Job_Center_Scraper/blob/50400031a18cc47afcaa740a48a9ca3c418fac17/webscraper_v3.py#L34). Remember to comment out the Firefoc lines.
  

Fire up your terminal/command prompt, navigate to the repo folder and install all of the requirements.

```sh
pip install -r requirements.txt
```

  
Set the correct input csv file. E.g test_zipcode.csv in Line 10 [webscraper_v3.py](https://github.com/mitkotak/American_Job_Center_Scraper/blob/1c4cbd0d1f07c1da18f1d02d7c8f775e2bf726c1/webscraper_v3.py#L10)

```sh
vim webscraper_v3.py
```

  
Set the correct driver in Line 23 [webscraper_v3.py](https://github.com/mitkotak/American_Job_Center_Scraper/blob/1c4cbd0d1f07c1da18f1d02d7c8f775e2bf726c1/webscraper_v3.py#L23)

```sh
vim webscraper_v3.py
```

Firefox
<ul>
  <li>Mac     : ./drivers/geckodriver</li>
  <li>Windows : .\drivers\geckodriver.exe</li>
</ul>


Firefox
<ul>
  <li>Mac     : ./drivers/chromedriver</li>
  <li>Windows : .\drivers\chromedriver.exe</li>
</ul>


Now just run the geckodriver/geckodriver.exe | chromedriver/chromedriver.exe once by double-clicking on it. Install the latest version from [here](https://github.com/mozilla/geckodriver/releases) or [here](https://chromedriver.chromium.org)
if things don't work 


Just run the following command after this:

```sh
python3 webscraper_v2.py
```
Or 

```sh
python webscraper_v2.py
``` 


### Let the scrapping begin !!

<p align="center">
  <img width="500" align="center" src="https://media.giphy.com/media/d8PjnRdlAP52F1CImb/giphy.gif" alt="demo"/>
</p>

## Author

👤 **Mit Kotak**

* Github: [@mitkotak](https://github.com/mitkotak)

## 🤝 Contributing

Contributions, issues and feature requests are welcome!<br />Feel free to check [issues page](https://github.com/mitkotak/American_Job_Center_Scraper/issues). 

## Show your support

Give a ⭐️ if this project helped you!

## 📝 License

Copyright © 2021 [Mit Kotak](https://github.com/mitkotak).<br />
This project is [MIT ](https://github.com/mitkotak/American_Job_Center_Scraper/blob/main/LICENSE) licensed.

***
_This README was generated with ❤️ by [readme-md-generator](https://github.com/kefranabg/readme-md-generator)_
