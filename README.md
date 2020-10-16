<!--
*** Thanks for checking out this README Template. If you have a suggestion that would
*** make this better, please fork the repo and create a pull request or simply open
*** an issue with the tag "enhancement".
*** Thanks again! Now go create something AMAZING! :D
***
***
***
*** To avoid retyping too much info. Do a search and replace for the following:
*** github_username, IRIS_RECTASK_LIB, twitter_handle, addhyanmalhotra@gmail.com
-->





<!-- PROJECT SHIELDS -->
<!--
*** I'm using markdown "reference style" links for readability.
*** Reference links are enclosed in brackets [ ] instead of parentheses ( ).
*** See the bottom of this document for the declaration of the reference variables
*** for contributors-url, forks-url, etc. This is an optional, concise syntax you may use.
*** https://www.markdownguide.org/basic-syntax/#reference-style-links
-->
[![Contributors][contributors-shield]][contributors-url]
[![Forks][forks-shield]][forks-url]
[![Stargazers][stars-shield]][stars-url]
[![Issues][issues-shield]][issues-url]
[![MIT License][license-shield]][license-url]
[![LinkedIn][linkedin-shield]][linkedin-url]



<!-- PROJECT LOGO -->
<br />
<p align="center">
  <a href="https://github.com/addhyanmalhotra/IRIS_RECTASK_LIB">
    <img src="images/logo.png" alt="Logo" width="80" height="80">
  </a>

  <h3 align="center">YOUR_TITLE</h3>

  <p align="center">
    A library management application, developed as recruitment task for iris nitk
    <br />
    <a href="https://github.com/addhyanmalhotra/IRIS_RECTASK_LIB"><strong>Explore the docs »</strong></a>
    <br />
    <br />
    <a href="https://github.com/addhyanmalhotra/IRIS_RECTASK_LIB">View Demo</a>
    ·
    <a href="https://github.com/addhyanmalhotra/IRIS_RECTASK_LIB/issues">Report Bug</a>
    ·
    <a href="https://github.com/addhyanmalhotra/IRIS_RECTASK_LIB/issues">Request Feature</a>
  </p>
</p>



<!-- TABLE OF CONTENTS -->
## Table of Contents

* [About the Project](#about-the-project)
  * [Built With](#built-with)
* [Getting Started](#getting-started)
  * [Prerequisites](#prerequisites)
  * [Installation](#installation)
* [Usage](#usage)
* [License](#license)
* [Contact](#contact)



<!-- ABOUT THE PROJECT -->
## About The Project

[![Product Name Screen Shot][product-screenshot]](https://iris-rec-task.herokuapp.com/)
The project is a library management system built using Django and deployed on heroku.
It allows management of resouces and is primarily divided into two sections
1. Member Portal
2. User Portal


### Built With

* [Django]()
* [Heroku]()
* [Bootstrap4]()



<!-- GETTING STARTED -->
## Getting Started (install is optional you can access the website here [Deployed Demo](https://iris-rec-task.herokuapp.com/)

To get a local copy up and running follow these simple steps.

### Prerequisites

This is an example of how to list things you need to use the software and how to install them.
* python
* Django
* Pip
* Virtual Env

### Installation

1. Clone the repo
```sh
git clone https://github.com/addhyanmalhotra/IRIS_RECTASK_LIB.git
```
2. Activate Virtual Env
  * Windows 
    ```sh
    .\venv\Scripts\activate
    ```
  * Linux MacOS
    ```sh
    source venv/bin/activate
    ```
3. Install Requirements
```sh
pip install -r requirements.txt
```
4. Runserver
```sh
python manage.py runserver
```
5. Open in browser
  



<!-- USAGE EXAMPLES -->
## Usage

### Member
The landing page leads you to the member dashboard, this shows basic project information like UML structure and has menu options loging in gives you access to
* Request Borrowing
* Check Active Requests
* View available books

### Librarian
From landing page navigate to admin site
#### User Management
* You can add users (members) from user section
* You can change user info
* You can delete existing Users
#### Resouce managment
* Library recources can be managed from LMS section
* New books to be uploaded under Book Instance
* Issue requests show you existing requests along with appropriate filters you can aprove reject and delete reques
once approved a new transaction will be created
* Transactions list the Book transactions made
 (Each of the above resouces can be exported to CSSV from respective dashboards)

_For more examples, please refer to the [Documentation](https://example.com)_






<!-- LICENSE -->
## License

Distributed under the MIT License. See `LICENSE` for more information.



<!-- CONTACT -->
## Contact

Addhyan Malhotra - [@twitter_handle](https://twitter.com/twitter_handle) - addhyanmalhotra@gmail.com

Project Link: [https://github.com/addhyanmalhotra/IRIS_RECTASK_LIB](https://github.com/addhyanmalhotra/IRIS_RECTASK_LIB)







<!-- MARKDOWN LINKS & IMAGES -->
<!-- https://www.markdownguide.org/basic-syntax/#reference-style-links -->
[contributors-shield]: https://img.shields.io/github/contributors/addhyanmalhotra/repo.svg?style=flat-square
[contributors-url]: https://github.com/addhyanmalhotra/repo/graphs/contributors
[forks-shield]: https://img.shields.io/github/forks/addhyanmalhotra/repo.svg?style=flat-square
[forks-url]: https://github.com/addhyanmalhotra/repo/network/members
[stars-shield]: https://img.shields.io/github/stars/addhyanmalhotra/repo.svg?style=flat-square
[stars-url]: https://github.com/addhyanmalhotra/repo/stargazers
[issues-shield]: https://img.shields.io/github/issues/addhyanmalhotra/repo.svg?style=flat-square
[issues-url]: https://github.com/addhyanmalhotra/repo/issues
[license-shield]: https://img.shields.io/github/license/addhyanmalhotra/repo.svg?style=flat-square
[license-url]: https://github.com/addhyanmalhotra/repo/blob/master/LICENSE.txt
[linkedin-shield]: https://img.shields.io/badge/-LinkedIn-black.svg?style=flat-square&logo=linkedin&colorB=555
[linkedin-url]: https://linkedin.com/in/addhyanmalhotra
[product-screenshot]: images/screenshot.png
