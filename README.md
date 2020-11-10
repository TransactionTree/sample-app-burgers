# NCR BurgersUnlimited
The NCR Burger Demo serves as an example of how a la carte BSP APIs can be brought together to build a functional product. Inside this repository, you will find sample code for a fictitious burger chain. The burger chain uses BSP APIs to mimic a traditional hospitality ordering experience.

Alternatively, this repository can be used to understand the BSP HMAC algorithm.

In future updates, we hope to capture the API calls made by the server visually, capture errors if requests made to the APIs fail, link the user registration system and order system together, and implement a customer loyalty system.


## Table of Contents
* __[Installation](#installation)__
* __[Setting up the Developer Environment](#setting-up-the-developer-environment)__
* __[Usage](#usage)__
* __[Notes](#notes)__
* __[Troubleshooting](#troubleshooting)__
* __[License](#license)__

## Installation
You will need to have the following:
1. Python 3.0 version or [higher](https://www.python.org/downloads/).
2. A Python IDE, we chose [PyCharm](https://www.jetbrains.com/pycharm/download/#section=mac).
3. Django latest version.
   * Open PyCharm terminal and type ```$ python3 -m pip install Django```
4. Python Requests module.
   * Open PyCharm terminal and type ```$ python3 -m pip install requests```
5. Django packages. Run the following commands in PyCharm terminal.
   * [Django Compressor](https://django-compressor.readthedocs.io/en/stable/) ```$ python3 -m pip install django_compressor```
   * [Django REST framework](https://www.django-rest-framework.org/) ```$ python3 -m pip install djangorestframework```
   * [Django Debug Toolbar](https://django-debug-toolbar.readthedocs.io/en/latest/) ```$ python3 -m pip install django-debug-toolbar```
   * [django-requests-debug-toolbar](https://github.com/marceltschoppch/django-requests-debug-toolbar) ```$ python3 -m pip install django-requests-debug-toolbar```
   * [django-crispy-forms](https://django-crispy-forms.readthedocs.io/en/latest/) ```$ python3 -m pip install django-crispy-forms```
   * [django-web-profiler](https://github.com/MicroPyramid/django-web-profiler) ```$ python3 -m pip install django-web-profiler```
   
## Setting up the Developer Environment
Ensure that you have access to your Shared Key, Secret Key, NEP Application Key and NEP Organzation. Inside of the settings file, ( found in /ncr-burgers-demo/code/BugersUnlimited) fill in those values with your credientials. Once you have filled in those values you will need to create your sites and catalog.
 
1. Creating your Sites
   * As part of your initial configuration, you will need to set up at least two sites; for instructions as to how to create a site, see the [site documentation](https://developer.ncr.com/portals/dev-portal/api-explorer/details/15/documentation?version=1.99&path=post_sites_import), or the section about sites on the [documentation page](https://burgersdemo.ncrcloud.com/burger/documentation#Sites_Quick_Start) within the application.
2. Creating your Catalog 
   * As part of your initial configuration, you will need to set up your catalog, which will serve as your menu; for instructions as to how to create a catalog, see the [catalog documentation](https://developer.ncr.com/portals/dev-portal/api-explorer/details/8/documentation?version=2.99), or the section about catalogs on the [documentation page](https://burgersdemo.ncrcloud.com/burger/documentation#Tutorial_Catalog) within the application.
   
Once you have completed the installation and configuration of the developer enviroment, you are ready to use the sample app.

## Usage
To run the sample app, enter the following commands from the root directory in Terminal:
```bash
$ cd code
$ pip install -r requirements.txt
$ python3 manage.py migrate
$ python3 manage.py runserver
```

The sample app should open up to the main page. The user can input an address into the search box and choose a search radius. {Note: the search radius is in miles}. 

* If results are found, the user will be able to select a restaurant.
    * If no results are found, the user will be prompted to return to the home screen. 
* If the user selects a restaurant, they will be taken to that restaurant's menu. The user can then add items to their cart. 
    * Once the user is done adding items to the cart or wants to edit their cart, they can click the view cart | edit cart button. 
* They will then be taken to a page to update their cart. 
* Once they are satisfied, they are checkout by clicking the checkout button. 
* The payment page is disabled for safety reasons.
* Users should then navigate to the documentation page to discover what APIs were used and how they were implemented.

## Notes
 NCR API's used in the NCR Burger Demo are:<br/>
- Sites
- Catalog
- Order <br/>

> If you do not set up your sites and catalog, the sample app will not function correctly.

If you are using the sample app to learn more about the BSP HMAC algorithm, see the [HMAC](https://burgersdemo.ncrcloud.com/burger/documentation#Authentication_HMAC) section of the documentation within the application and check out the [HMACAuth](code/HMACAuth.py) file in the /ncr-burger-demo/code folder.

## Troubleshooting
If the **Profiler** tab is missing in the application, check the browser inspector for a console error about, "*Failure to load module script: The server responded with a non JavaScript MIME type..."* This issue may be caused by improper content mapping with Django's ```runserver``` command. Please refer to [these docs](https://django-debug-toolbar.readthedocs.io/en/latest/installation.html#troubleshooting) for more information on troubleshooting this issue.

## License
This sample app project is released under the Apache 2.0 license. The license's full text can be found [here](https://github.com/NCR-Corporation/sample-app-burgers/blob/main/LICENSE).
