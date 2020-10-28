# NCR BurgersUnlimited
The NCR Burger Demo serves as an example of how a la carte BSP APIs can be brought together to build a functional product. Inside this repository, you will find sample code for a fictitious burger chain. The burger chain uses BSP APIs to mimic a traditional hospitality ordering experience.

Alternatively, this repository can be used to understand the BSP HMAC algorithm.

In future updates, we hope to capture the API calls made by the server visually, capture errors if requests made to the APIs fail, link the user registration system and order system together, and implement a customer loyalty system.


## Table of Contents
* __[Installation](#installation)__
* __[Setting up the Developer Environment](#setting-up-the-developer-environment)__
* __[Usage](#usage)__
* __[Notes](#notes)__
* __[License](#license)__

## Installation
You will need to have the following:
1. Python 3.0 version or [higher](https://www.python.org/downloads/).
2. A Python IDE, we chose [Pycharm](https://www.jetbrains.com/pycharm/download/#section=mac).
3. Django latest version.
   * Open Pycharm terminal and type ```$ python3 -m pip install Django```
4. Python Requests Library
   * Open Pycharm terminal and type ```$ python3 -m install requests```
5. Crispy Forms
   * Open Pycharm terminal and type ```$ pip install django-crispy-forms```
6. Django Rest Framework
   * Open Pycharm terminal and type ```$ pip -m install djangorestframework```
   
## Setting up the Developer Environment   
 
Ensure that you have access to your Shared Key, Secret Key, NEP Application Key and NEP Organzation. Inside of the settings file, ( found in /ncr-burgers-demo/code/BugersUnlimited) fill in those values with your credientials. Once you have filled in those values you will need to create your sites and catalog.
 
1. Creating your Sites
   * As part of your initial configuration, you will need to set up at least two sites; for instructions as to how to create a site, see the [site documentation](https://developer.ncr.com/portals/dev-portal/api-explorer/details/15/documentation?version=1.99&path=post_sites_import), or the section about sites on the [documentation page](https://burgersdemo.ncrcloud.com/burger/documentation#Sites_Quick_Start) within the application.
2. Creating your Catalog 
   * As part of your initial configuration, you will need to set up your catalog, which will serve as your menu; for instructions as to how to create a catalog, see the [catalog documentation](https://developer.ncr.com/portals/dev-portal/api-explorer/details/8/documentation?version=2.99), or the section about catalogs on the [documentation page](https://burgersdemo.ncrcloud.com/burger/documentation#Tutorial_Catalog) within the application.
   
Once you have completed the installation and configuration of the developer enviroment, you are ready to use the sample app.

## Usage
To run the sample app navigate into the /ncr-burger-demo/code folder and type ```$ python3 manage.py runserver ```

The sample app should open up to the main page. The user can input an address into the search box and choose a search radius. {Note: the search radius is in miles}. 

* If results are found, the user will be able to select a restaurant.
  - If no results are found, the user will be prompted to return to the home screen. 

* If the user selects a restaurant, they will be taken to that restaurant's menu. The user can then add items to their cart. 
- Once the user is done adding items to the cart or wants to edit their cart, they can click the view cart | edit cart button. 
* They will then be taken to a page to update their cart. 
* Once they are satisfied, they are checkout by clicking the checkout button. 
* The payment page is disabled for safety reasons.
* Users should then navigate to the documentation page to discover what APIs were used and how they were implemented.

## Notes
 NCR API's used in the NCR Burger Demo are:<br/>
- Sites
- Catalog
- Order <br/>

!! If you do not set up your sites and catalog, the sample app will not function correctly.

If you are using the sample app to learn more about the BSP HMAC algorithm, see the [HMAC](https://burgersdemo.ncrcloud.com/burger/documentation#Authentication_HMAC) section of the documentation within the application and check out the HMACAuth file in the /ncr-burger-demo/code folder.

## License
This sample app project is released under the Apache 2.0 license. The license's full text can be found [here](https://github.com/NCR-Corporation/sample-app-burgers/blob/main/LICENSE).
