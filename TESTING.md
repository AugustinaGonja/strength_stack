## STRENGTHSTACK - Testing

![Amiresponsive Image showing StrenthStack as displayed on multiple screen sizes](staticfiles/images/README%20images/Responsiveness.png)

[Link to deployed StrengthStack Website](https://strength-stack-e65fe8f9116b.herokuapp.com/)

## Contents
**[Automated Testing](#automated-testing)**
* [W3C Validator](#wc3-html-validator)
* [Python Validator](#wc3-html-validator)
* [Django Testing](#django-testing)


**[Performance Testing](#performance-testing-lighthouse)**
* [Desktop](#desktop)
* [Mobile](#mobile)

**[Performance Results](#performance-results)**

**[Manual Testing](#manual-testing)**
* [Testing User Stories](#testing-user-stories)

**[Full Testing](#full-testing)**
* [Devices Tested On](#devices-tested-on)
* [Page Feature Testing](#page-feature-testing)

**[Solved & Known Bugs ](#solved--known-bugs)**

---
Chrome DevTools was incredibly helpful throughout the testing process, enabling quick troubleshooting. While building the website, I kept track of bugs as they arose.

I also attempted to use Django Testing , to build automated tests for my forms .

## Automated Testing
### WC3 HTML Validator
The W3C Validator was used to check and validate the HTML and CSS for all pages of the website. Validation was performed by directly entering each page’s web link into the tool.

* [Home Page](https://validator.w3.org/nu/?doc=https%3A%2F%2Fstrength-stack-e65fe8f9116b.herokuapp.com%2F) - No errors or warnings.
* [Index Page](https://validator.w3.org/nu/?doc=https%3A%2F%2Fstrength-stack-e65fe8f9116b.herokuapp.com%2F) - No errors or warnings.
* [About Page](https://validator.w3.org/nu/?doc=https%3A%2F%2Fstrength-stack-e65fe8f9116b.herokuapp.com%2Fabout%2F) - No errors or warnings.
* [Login Page](https://validator.w3.org/nu/?doc=https%3A%2F%2Fstrength-stack-e65fe8f9116b.herokuapp.com%2Faccounts%2Flogin%2F) - No errors or warnings.
* [Registration Page](https://validator.w3.org/nu/?doc=https%3A%2F%2Fstrength-stack-e65fe8f9116b.herokuapp.com%2Faccounts%2Fsignup%2F) - No errors or warnings.
* [Profile Page]() - 500 Internal Server Error
* [Update Profile Page]()-  500 Internal Server Error
* [Dashboard](https://validator.w3.org/nu/?doc=https%3A%2F%2Fstrength-stack-e65fe8f9116b.herokuapp.com%2Fdashboard%2F) - No errors or warnings.
* [Update Workout Page](https://validator.w3.org/nu/?doc=https%3A%2F%2Fstrength-stack-e65fe8f9116b.herokuapp.com%2Fupdate_workout%2F16%2F) -No errors or warnings.
* [Create Workout Page](https://validator.w3.org/nu/?doc=https%3A%2F%2Fstrength-stack-e65fe8f9116b.herokuapp.com%2Fcreate%2F) - No errors or warnings.
* [Workout Details Page](https://validator.w3.org/nu/?doc=https%3A%2F%2Fstrength-stack-e65fe8f9116b.herokuapp.com%2Fview%2F16%2F) - No errors or warnings.
* [Update Exercise Page](https://validator.w3.org/nu/?doc=https%3A%2F%2Fstrength-stack-e65fe8f9116b.herokuapp.com%2Fupdate_exercise%2F24%2F) - No errors or warnings.
* [Create Exercise Page](https://validator.w3.org/nu/?doc=https%3A%2F%2Fstrength-stack-e65fe8f9116b.herokuapp.com%2Fadd_exercise%2F13%2F) - No errors or warnings.
* [Logout Page](https://validator.w3.org/nu/?doc=https%3A%2F%2Fstrength-stack-e65fe8f9116b.herokuapp.com%2Faccounts%2Flogout%2F)
* [404 Page](https://validator.w3.org/nu/?doc=https%3A%2F%2Fstrength-stack-e65fe8f9116b.herokuapp.com%2Faccountsss%2Flogout%2F) - There are no other errors; the validator simply identified the 404 page.

* [CSS Validator](https://jigsaw.w3.org/css-validator/validator?uri=https%3A%2F%2Fstrength-stack-e65fe8f9116b.herokuapp.com%2F&profile=css3svg&usermedium=all&warning=1&vextwarning=&lang=en)

### Python Validator
To validate all my Python code, I used the Code Institute [Python Linter](https://pep8ci.herokuapp.com/).<br>
Most of my code passed without issues, except for line length.

**"workouts" App :**

* [admin.py](staticfiles/images/TESTING%20images/admin-workouts-PL.png)
* [forms.py](staticfiles/images/TESTING%20images/forms-workouts-PL.png)
* [models.py](staticfiles/images/TESTING%20images/model-workout-PL.png)
* [test_forms.py](staticfiles/images/TESTING%20images/test-workouts-PL.png)
* [urls.py](staticfiles/images/TESTING%20images/urls-workouts-PL.png)
* [views.py](staticfiles/images/TESTING%20images/views-workouts-PL.png) 
    * **"E231 missing whitespace after '"**<br>
    I don’t understand this error since all unnecessary whitespace has been removed.

**"users" App :**

* [admin.py](staticfiles/images/TESTING%20images/admin-user-PL.png)
* [forms.py](staticfiles/images/TESTING%20images/forms-user-PL.png)
* [models.py](staticfiles/images/TESTING%20images/models-user-PL.png)
* [urls.py](staticfiles/images/TESTING%20images/urls-user-PL.png)
* [views.py](staticfiles/images/TESTING%20images/views-user-PL.png)

### Django Testing
I also tried using Django Testing to create automated tests for my forms.
I wrote a couple of tests for the New Workout and Exercise forms.

However, when I ran python manage.py test, the terminal showed an OperationalError.

<p align ="center">
  <img src="staticfiles/images/TESTING images/operational error.png" alt="New Workout Form">
</p>

Ultimately, I was unable to run these tests successfully. But below is the code I would've test.

**New Workout Form :**

I wrote three tests for the Workout Form to check:

* The form is valid when all fields are filled correctly
* An error is raised if the title is missing
* An error is raised if the description is missing



<p align ="center">
  <img src="staticfiles/images/TESTING images/neworkoutform - test.png" alt="New Workout Form">
</p>

**Exercise Form :**

I wrote two tests for the Workout Form to verify:

* The form is valid when all fields are filled correctly
* An error is raised if the integer fields for reps, sets, and weight are left empty

<p align ="center">
  <img src="staticfiles/images/TESTING images/exerciseform - test.png" alt="Exercise Form">
</p>

# Performance Testing ( Wave & Lighthouse )
**Wave Contrast Checker**

I used the WAVE Contrast Checker to verify if my webpages passed accessibility standards.

The only factor affected was when elements on the page had filters applied - for example, the hero image on the homepage. Otherwise, all pages pass the color contrast checker, ensuring accessibility and readability for all users.

## Performace Results 
I used Lighthouse on ChromeDevTools to test perfomance of my website on desktop - page by page.
<br>The results are as shown below.

### Desktop
* [Home Page](staticfiles/images/TESTING%20images/home-%20lighthouse.png)
* [Index Page](staticfiles/images/TESTING%20images/index-%20lighthouse.png)
* [About Page](staticfiles/images/TESTING%20images/about-lighthouse.png)
* [Login Page](staticfiles/images/TESTING%20images/login-%20lighthouse.png)
* [Registration Page](staticfiles/images/TESTING%20images/signup-%20lighthouse.png)
* [Profile Page](staticfiles/images/TESTING%20images/profile%20-%20lighthouse.png)
* [Update Profile Page](staticfiles/images/TESTING%20images/profile-edit%20-%20lighthouse.png)
* [Dashboard](staticfiles/images/TESTING%20images/dash-%20lighthouse.png)
* [Update Workout Page](staticfiles/images/TESTING%20images/edit-workout-%20lighthouse.png)
* [Create Workout Page](staticfiles/images/TESTING%20images/create-workout-%20lighthouse.png)
* [Workout Details Page](staticfiles/images/TESTING%20images/view-workout-%20lighthouse.png)
* [Update Exercise Page](staticfiles/images/TESTING%20images/edit-ex-%20lighthouse.png)
* [Create Exercise Page](staticfiles/images/TESTING%20images/create-ex-%20lighthouse.png)
* [Logout Page](staticfiles/images/TESTING%20images/logout%20-%20lighthouse.png)
* [404 Page](staticfiles/images/TESTING%20images/404-lighthouse.png)

**To summarise :**  
Performance scores for the Index, Home, and 404 pages were the lowest at 73, which is below the desired level but passable.
I suspect that Chrome extensions may have impacted these results. 
Aside from that, most performance metrics were in the green.

SEO only dropped into the orange range on the 404 page.

Accessibility scores ranged from approximately 85 to the 90s.

Best Practices consistently scored 100, with only a few instances ranging between 90-100.

## Manual Testing
### Testing User Stories

| **User Story** | **How are they achieved?** | **Image** |
| :--- | :--- | :--- |
|`First Time Visitor`<br>" As a first-time visitor, I can register and log in using my email and password , so that I can securely access my account and track my workouts "|The website features full authentication, allowing users to create an account using a valid username and password.<br><br>Users can access their accounts anytime by logging in and viewing their personal dashboard.|![Login](staticfiles/images/README%20images/LoginPage.png) ![Register](staticfiles/images/README%20images/RegistrationPage.png)|
| `Returning Visitor`<br>" As a returning visitor, I can see a list of my previous workouts on the dashboard when I log in so that I can quickly access and review past sessions." |Upon logging in, you can access your dashboard through the welcome page.<br><br>After navigating to the dashboard, the user is presented with a list of previous workouts, if any exist.|![Welcome Page](staticfiles/images/README%20images/Index.png)<br>![Dashbboard](staticfiles/images/README%20images/Dash.png) |
| `Returning Visitor`<br>" As a returning visitor, I can create a new workout entry so that I can log my routine and begin tracking my progress." |The Create Workout button on the dashboard directs the user to a form where they can enter all relevant information. |![Create Workout Form](staticfiles/images/README%20images/create%20workout.png)|
| `Returning Visitor`<br>" As a returning visitor, I can view the full details of a selected workout so that I can review the exercises, sets, and reps involved" |Users can click the View Details button on any workout card they have created to see the full details of the exercises and other information involved.|![View Workout](staticfiles/images/README%20images/view.png)|
| `Returning Visitor`<br>" As a returning visitor, I can update or delete workout entries so that I can keep my records accurate and remove outdated information." |Each workout and exercise in the includes Update and Delete buttons.<br><br>The user can click the Update button to open a form where they can modify the details and save the changes.<br><br>Clicking the Delete button will prompt a confirmation alert to ensure the user wants to proceed.|![Edit](staticfiles/images/README%20images/edit%20exercise.png)<br><br>![Delete](staticfiles/images/README%20images/delete%20alert.png)|
|`Frequent Visitor`<br> "As a frequent visitor, I can see a visual representation of my workout history so that I can easily track my progress over time."|**This feature was not implemented due to time constraints, but the plan was to use Chart.js for its development in future.**| No Image |
|`Site Admin`<br> "As site admin I can create, read, update, and delete site information so that I can manage site content effectively.|Logged-in admins can create, view, update existing posts and delete them.| ![Admin](staticfiles/images/README%20images/admin.png) |
## Full Testing
### Devices Tested On

I tested the website across the following devices and browsers, and it displayed correctly on all of them.<br>The site was fully responsive and loaded properly in each case.

* **Laptop**
    * Lenovo Legion 5 15.6 in
---
* **Mobile**
    * Iphone 14 SE - Safari
    * Iphone 12
---
* **Browser**
    * Google Chrome
    * Microsoft Edge
    * Safari
    * Firefox

### Page Feature Testing
**Logged Out**

`Home Page`
| Feature | Expected Outcome | Testing Performed | Result | Pass/Fail |
| --- | --- | --- | --- | --- |
| StrengthStack Title | Link redirects the user back to the Home page | Title Clicked | Redirected to Homepage | Pass |
| Home Link | Link directs the user to the Home Page | Home Link Clicked | Redirected to Home Page | Pass |
| About Link | Link directs the user to the About Page| About Link Clicked |Redirected to About Page| Pass |
| Login Link | Link directs the user to the Login Page | Login Link Clicked | Redirected to Login Page| Pass |
| Get Started Buttons | Link directs the user to the Registration Page | Clicked on button | Redirected to Registration Page | Pass |
| All buttons hover effect| Button brightness reduces on hover| Hover over button | Button brightness reduces on hover | Pass |
| Social Media Icons Footer | Link directs the user to facebook , instagram , X or Gmail , depending on which icon clicked.| Click social media Icon | Redirected to the home page of social platform clicked. | Pass |
---
---
`Login & Registration`
| Feature | Expected Outcome | Testing Performed | Result | Pass/Fail |
| --- | --- | --- | --- | --- |
| Login Functionality| Sign in button redirects user to thier account if correct details entered | Entered correct username and password | User redirected to thier accont Home Page | Pass |
| Registration Functionality| Register button redirects user to thier account if correct details entered | Created a valid username and password | User redirected to thier accont Home Page | Pass |
| Username Field | Message prompting that username Field must not be empty | Field not filled out | User Presented with message , "This field is required." | Pass |
| Password Field|Message prompting that password Field must not be empty | Field not filled out | User Presented with a small popup "Please Fill In This Field." | Pass |
| Incorrect Entry of both Fields | Message prompting that username and Password must be correct | Entered correct username and password|User Presented with a "The username and/or password you specified are not correct."| Pass |
| Password (again)* Field | Throws error message if Passwords dont match | Unidentical password entered | User Presented with message , "You must type the same password each time."| Pass |
---
---
**Logged In**

`Index Page`
| Feature | Expected Outcome | Testing Performed | Result | Pass/Fail |
| --- | --- | --- | --- | --- |
| Dashboard Link | Link directs the user to the Dashboard | Dashboard Link Clicked | Redirected to Dashboard Page | Pass |
| Profile Link| Link directs the user to the Profile Page| Profile Link Clicked |Redirected to Profile Page| Pass |
| Signout Link | Link directs the user to the Signout Page | Signout Link Clicked | Redirected to Signout Page| Pass |
---
---
`Profile & Update Profile Page`
| Feature | Expected Outcome | Testing Performed | Result | Pass/Fail |
| --- | --- | --- | --- | --- |
| Edit Profile Button | Button directs the user to the Edit Profile Form | Button Clicked | Redirected to Edit Profile Form | Pass |
| Upload Profile Image| Clicking "Choose File" opens your file explorer, allowing you to select and upload an image.| Choose File clicked | Choose File opens the file explorer. | Pass |
| Save Button |Displays a confirmation message, and if confirmed, saves the changes. |Save button clicked | Changes saved after confirmed | Pass |
---
---
`Dashboard`
| Feature | Expected Outcome | Testing Performed | Result | Pass/Fail |
| --- | --- | --- | --- | --- |
| No Workouts | On first visit to the Dashboard page after creating a new account, display a message stating no workouts are posted yet. | Dashboard Button Clicked | User Presented with message on page , "No Workouts Added yet" | Pass |
| Create New Workout Button | Button directs the user to the Create Workout Form | Button Clicked | Redirected to Create Workout Form | Pass |
| View Workout Button| Button directs the user to the Workout Details Page | Button Clicked | Redirected to Create Workout Details Page | Pass |
| Delete Workout Button|Displays a confirmation message, and if confirmed, deletes the workout. |Button Clicked | Workout Deleted | Pass |
| Edit Workout Button|Button directs the user to the Edit Workout Form |Button Clicked | Redirected to Edit Workout Form | Pass |
---
---
`Create & Update Workout Pages `
| Feature | Expected Outcome | Testing Performed | Result | Pass/Fail |
| --- | --- | --- | --- | --- |
| Asterisked Fields| All these fields must be filled out or message prompted | Save Button Clicked | User Presented with message , "This field is required."| Pass |
| Save Workout Button| The button redirects the user to the Dashboard, where they can view the new workout at the top of the list. | Button Clicked | Redirects to the Dashboard, with the new workout displayed as the first item on the list. | Pass |
| Fields Prepopulated on Edit Form|Displays form with previously entered information |Button Clicked | Displays a form with the previously entered information, which can be edited.| Pass |
---
---
`Workout Details Page `
| Feature | Expected Outcome | Testing Performed | Result | Pass/Fail |
| --- | --- | --- | --- | --- |
| No Exercises | On first visit to the Workout Details page after creating a workout, display a message stating no exercises are posted yet. | New workout Created & View Workout Button Clicked | User Presented with message on page , "No Exercises Added yet ! Add New Exercises Below." | Pass |
| Add Exercise Button | Button directs the user to the Add Exercise Form | Button Clicked | Redirected to Add Exercise Form | Pass |
| Delete Exercise Button|Displays a confirmation message, and if confirmed, deletes the exercise. |Button Clicked | Exercise Deleted | Pass |
| Edit Exercise Button|Button directs the user to the Edit Exercise Form |Button Clicked | Redirected to Edit Exercise Form | Pass |
---
---
`Create & Update Exercise Pages`
| Feature | Expected Outcome | Testing Performed | Result | Pass/Fail |
| --- | --- | --- | --- | --- |
| Asterisked Fields| All these fields must be filled out or message prompted | Save Button Clicked | User Presented with message , "This field is required."| Pass |
| Save Exercise Button| The button redirects the user to the Workout Details, where they can view the new exercise. | Button Clicked | Redirects to the Workout Details, with the new exercise displayed on the list. | Pass |
| Fields Prepopulated on Edit Form |Displays form with previously entered information |Button Clicked | Displays a form with the previously entered information, which can be edited.| Pass |
---
---
`Logout Page`
| Feature | Expected Outcome | Testing Performed | Result | Pass/Fail |
| --- | --- | --- | --- | --- |
| Sign Out Button | Sign Out button redirects user back to the home page and signs them out of thier account| Sign Out button clicked | User signed out | Pass |

# Solved & Known Bugs  

| No | Bug | How I solved the issue |
| :--- | :--- | :--- |
| 1| When creating and logging into a new account, the dashboard isn’t reset and still displays the superuser’s information.| I referred to the discussion board below to determine the necessary changes. I needed to ensure that the information retrieved from the database matched the currently logged-in user. Adding **.filter(user=request.user)** to the relevant views resolved the issue. <br><br>[Fix](https://stackoverflow.com/questions/64802240/django-how-to-only-display-content-made-by-a-user-to-that-same-user) |
| 2 | When zooming out in the browser, the background/hero image doesn’t resize properly, leaving a white space between it and the footer.|The issue was caused by a fixed height in my CSS that ignored the viewport size. I fixed it by making the height viewport-relative.|
| 3| When creating and logging into a new account , clicking the profile page will result in a Server 500 Error.<br><br>[Server Error](staticfiles/images/TESTING%20images/500%20error.png)| Resolved in the same way as the bug in row 2, by filtering the profile view with **.filter(user=request.user)**.|

## Known Bugs 

| No | Bug | Issue |
| :--- | :--- | :--- |
| 1 | On the login page, if you refresh after receiving an invalid username or password error, the error message should disappear - but currently, it remains displayed.<br>[Login](staticfiles/images/TESTING%20images/Login%20Error.png)| X |
| 2 | The "Remember me" on the Login and Registration page box does not save account details.| X |
---
[Back to the Top](#strengthstack---testing)
