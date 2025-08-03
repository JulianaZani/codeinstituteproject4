# Volunteer Testimonials - HopeBridge Community

**Volunteer Testimonials** is a full-stack web application built with Django. It allows users to share and read real-life stories about their experiences participating in social and volunteering projects. The name **HopeBridge Community** was not chosen at the beginning of the project.

The site is designed with accessibility and user experience in mind, following modern development practices using HTML, CSS, JavaScript, Python, and Django.  

**Project Journey**  
This project was a real challenge for me. For most of the post-third project period, I had to work longer hours at my job, which left me with very limited time to study. It was only towards the end that my workload at the company decreased, allowing me to dedicate more time to completing the project. There were many moments when I almost gave up. Thank you, and I apologize for any rough edges!

---

## 📑 Table of Contents

1. [Purpose](#purpose)
2. [Target Users](#target-users)
3. [Features](#features)
4. [User Stories](#user-stories)
5. [Wireframes](#wireframes)
6. [Technologies Used](#technologies-used)
7. [Data Schema](#data-schema)
8. [CRUD Functionality](#crud-functionality)
9. [Testing](#testing)
   - [Responsiveness](#responsiveness)
   - [W3C HTML Validator](#w3c-html-validator)
   - [W3C CSS Validator](#w3c-css-validator)
   - [Accessibility](#accessibility)
     - [Wave](#wave)  
     - [Lighthouse](#lighthouse)
10. [Deployment](#deployment)
11. [Credits](#credits)


---

## Purpose
[▲ Back to Top](#volunteer-testimonials---hopebridge-community)

The purpose of this application is to:

- Provide a platform for users to submit testimonials about volunteering experiences
- Allow visitors to read and get inspired by others’ stories
- Enable administrators to manage, approve, or remove testimonials


---

## Target Users  
[▲ Back to Top](#volunteer-testimonials---hopebridge-community)

The project was designed with the following user groups in mind:

### General Visitors:
- Browse published testimonials for inspiration  
- View full details of each story  
- Submit questions through a contact form  

### Registered Users:
- Create an account to share a testimonial  
- Manage (edit or delete) their own testimonial  
- Receive confirmation messages upon actions  

### Admin Users:
- Approve or reject **testimonials**    
- Remove testimonials that do not meet the platform’s guidelines  
- Receive contact form messages via email  


---

## Features  
[▲ Back to Top](#volunteer-testimonials---hopebridge-community)  

On the homepage, visitors are invited to join the community. They can view testimonials, and by clicking Read More, they can read the testimonial details. The Home, Login, Sign Up, and Contact links are clearly located, centered just below the HopeBridge Community header.  

Predominant colors:  

- #ffffff → pure white (RGB 255, 255, 255);  

- #f9f9f9 → a slightly grayish white (RGB 249, 249, 249);  

Colors to contrast:

- #0d1b4c → navy blue (RGB 13, 27, 76);

![navycolor](doc/screenshots/colornavy.png)


- #ffdd57 → yellow (RGB 255, 221, 87); 

![yellowcolor](doc/screenshots/coloryellow.png)


- #555555 → dark grey (RGB 85, 85, 85);  


![initialpage](doc/screenshots/00initialpage.png)

By clicking Read more, the visitor/user continues to view the links to navigate the site. They see the author of the testimonial, the title, the full comment, the image, the post date, and the return link.  

![detailtestimonialpage](doc/screenshots/01detailtestimonialpage.png)  

On the login page, you'll find username and password fields. A "Log In" button takes you to the home page after correct input. Below, you'll find links to change your password and sign up.  

![loginpage](doc/screenshots/02login.png)  

On the Sign Up page, there are fields for creating an account: Username, Email, Password, information for creating a correct password, Password confirmation, a Register button, and a Log in link below (if the user is already registered).

![signuppage](doc/screenshots/03signup.png)  

The Contact page is open to everyone. Anyone can freely contact the HopeBridge Community. The fields to fill out are: Name, Email, and Message. Below is the Send Message button.  
Note: The back link on the right side at the bottom of the Login, Registration, Contact and Testimonial Details pages redirects the visitor/user to the home page.  

![contactpage](doc/screenshots/04contact.png)  

To reset your password, the Reset Password page has a field for entering your email address and below it, the "Send Reset Link" button. On the bottom right, there's a link to return to the login page.  

![resetpasswordpage](doc/screenshots/05resetpassword.png)  

After the visitor/user sends the email to reset their password, a page opens with the message: Password Reset Sent. If an account exists with the email you entered, you will receive a password reset link shortly. Please check your email.  
Below on the right side is the link to the Login page.  

![resetpasswordmsgpage](doc/screenshots/06resetpasswordmsg.png)  

On the password change page, there are the following fields to fill in: _Old password; _New password; _New password confirmation.
Information is provided to correctly enter the password. Below, the user has the "Change Password" button.  

![changepasswordpage](doc/screenshots/07changepassword.png)

Features related to pages accessed by logged-in users, in relation to sending, editing and deleting testimonials, are demonstrated in [CRUD Functionality](#crud-functionality).  


---

## User Stories  
[▲ Back to Top](#volunteer-testimonials---hopebridge-community)

User stories were planned and tracked using the [GitHub Projects Board](<https://github.com/users/JulianaZani/projects/1/views/1?layout=board>).  

Below are the user stories defined for the project:  

![userstories](doc/screenshots/userstories.png)

### MoSCoW Prioritization

| Category         | User Stories                                                                 | Points | % of Total |
|-----------------|-------------------------------------------------------------------------------|--------|-----------|
| **Must Have**   | 1. View Testimonials <br> 2. Register an Account <br> 3. Login to My Account <br> 4. Submit a Testimonial | 4 | 44% |
| **Should Have** | 5. Edit My Testimonial <br> 6. Delete My Testimonial                         | 2 | 22% |
| **Could Have**  | 7. Admin Approval <br> 8. Contact Form <br> 9. Responsive Design              | 3 | 33% |
| **Total**       | **9**                                                                        | **9**  | **100%** |

**Rule:** *Should Have* ≤ 60% 


---

## Wireframes  
[▲ Back to Top](#volunteer-testimonials---hopebridge-community)

![wireframes](doc/screenshots/wireframehomeandaddtestimonial.png)  

![wireframes](doc/screenshots/wireframelogincontact.png)


---

## Technologies Used  
[▲ Back to Top](#volunteer-testimonials---hopebridge-community)

Languages & Frameworks  
- Python 3.x – Main backend programming language

- Django 5.2.4 – Full-stack web framework

- HTML5, CSS3, and JavaScript – Structure, styling, and interactivity for the frontend

Database  
- SQLite – Database used in the development environment

- PostgreSQL – Database used in production (Heroku)

Storage & Media  
- Cloudinary – Image hosting and optimization

- dj3-cloudinary-storage – Integration between Django and Cloudinary

Servers & Deployment  
- Heroku – Hosting for the production environment

- Gunicorn – WSGI server for Django applications

- Whitenoise – Serving static files in production

Dependencies & Utilities  
- Pillow – Image manipulation for Django

- dj-database-url – Simplified database configuration with environment variables

- psycopg2-binary – PostgreSQL driver for Python/Django

- Requests – For making HTTP requests when needed

- asgiref, sqlparse, tzdata – Internal Django dependencies  


---

## Data Schema  
[▲ Back to Top](#volunteer-testimonials---hopebridge-community) 

**ER Diagram**  
```
+--------------------+        1       N  +----------------------+
|       User         |------------------>|     Testimonial      |
+--------------------+                   +----------------------+
| PK id              |                   | PK id                |
| username           |                   | FK user_id           |
| email              |                   | title                |
| password           |                   | content              |
| first_name         |                   | image                |
| last_name          |                   | created_on           |
| is_staff           |                   | approved             |
| is_superuser       |                   +----------------------+
| is_active          |
| date_joined        |
+--------------------+
```


---

## CRUD Functionality  
[▲ Back to Top](#volunteer-testimonials---hopebridge-community) 

The project implements full CRUD functionality for testimonials:  

Create – Users can submit a new testimonial in "Submit Testimonial".  


Read – All testimonials are displayed on the homepage for users to view.  


Update – Logged-in users can edit their testimonials via the "Edit" button.  


Delete – Logged-in users can delete a testimonial they created.  


---

## Testing
[▲ Back to Top](#volunteer-testimonials---hopebridge-community)

### Responsiveness

The HopeBridge community website is fully responsive and adapts to all screen sizes, from mobile devices to large desktops.  

![responsiveness01](doc/screenshots/responsiveness01.png)

**Examples**  

- Screen size - 768x1024:  

![responsiveness768](doc/screenshots/responsiveness02.png)  

- Screen size - 324x726:  

![responsiveness324](doc/screenshots/responsiveness03.png)  

- Screen size - 2000x1347  

![responsiveness04](doc/screenshots/responsiveness04.png)  


### W3C HTML Validator  

Pages checked and approved:  

- Initial page: https://testimonials-aeb7081fc7ea.herokuapp.com/  

![w3c01initialpage](doc/screenshots/w3c01.png)  

- Login page: https://testimonials-aeb7081fc7ea.herokuapp.com/accounts/login/  

![w3c02loginpage](doc/screenshots/w3c02.png)

- Signup page: https://testimonials-aeb7081fc7ea.herokuapp.com/accounts/signup/  

**Errors presented:**  

![w3c03signuppage](doc/screenshots/w3c03.png)

Adjustments made: delete "small" tag and add passwords helptext id in signup.html  
**After fixing the errors:**  

![w3c04signuppage](doc/screenshots/w3c04.png)
 
- Contact page: https://testimonials-aeb7081fc7ea.herokuapp.com/contact/  

![w3c05contactpage](doc/screenshots/w3c05.png)

- Submit testimonial page: https://testimonials-aeb7081fc7ea.herokuapp.com/testimonial/add/  

![w3c06submittestimonialpage](doc/screenshots/w3c06.png)

- Change password page: https://testimonials-aeb7081fc7ea.herokuapp.com/accounts/password_change/  

![w3c07changepasswordpage](doc/screenshots/w3c07.png)

- Testimonial edit page: https://testimonials-aeb7081fc7ea.herokuapp.com/testimonial/13/edit/  

![w3c08testimonialeditpage](doc/screenshots/w3c08.png)

- Testimonial delete page: https://testimonials-aeb7081fc7ea.herokuapp.com/testimonial/13/delete/  

![w3c09testimonialdeletepage](doc/screenshots/w3c09.png)

- Testimonial detail page: https://testimonials-aeb7081fc7ea.herokuapp.com/testimonial/13/  
and https://testimonials-aeb7081fc7ea.herokuapp.com/testimonial/14/ .  

**Errors presented:**  

![w3c10testimonialdetail1before](doc/screenshots/w3c10.png)  

![w3c11testimonialdetail2before](doc/screenshots/w3c11.png)  

Adjustment made: delete {{ testimonial.content|linebreaksbr }} "p" tags in testimonial_detail.html.  
**After fixing the errors:**  

![w3c12testimonialdetail1after](doc/screenshots/w3c12.png)  

![w3c13testimonialdetail2after](doc/screenshots/w3c13.png)  

- Password reset page: https://testimonials-aeb7081fc7ea.herokuapp.com/accounts/password_reset/  

![w3c14passwordresetpage](doc/screenshots/w3c14.png)  

- Done password reset message page: https://testimonials-aeb7081fc7ea.herokuapp.com/accounts/password_reset/done/  

![w3c15passwordresetmessagepage](doc/screenshots/w3c15.png)  


### W3C CSS Validator  

No errors were found when passing through the official (Jigsaw) validator.  

![w3ccss](doc/screenshots/w3ccss.png)


### Accessibility 

I confirmed that the colors and fonts chosen are easy to read and accessible by running it through lighthouse in devtools and Wave Evolution Tool.  

#### Wave  

- Initial page: https://testimonials-aeb7081fc7ea.herokuapp.com/  

![wave01initialpage](doc/screenshots/wave01.png)  

- Login page: https://testimonials-aeb7081fc7ea.herokuapp.com/accounts/login/  

![wave02loginpage](doc/screenshots/wave02.png)

- Signup page: https://testimonials-aeb7081fc7ea.herokuapp.com/accounts/signup/  

![wave03signuppage](doc/screenshots/wave03.png)

- Contact page: https://testimonials-aeb7081fc7ea.herokuapp.com/contact/  

![wave04contactpage](doc/screenshots/wave04.png)

- Submit testimonial page: https://testimonials-aeb7081fc7ea.herokuapp.com/testimonial/add/  

![wave05submittestimonialpage](doc/screenshots/wave05.png)

- Change password page: https://testimonials-aeb7081fc7ea.herokuapp.com/accounts/password_change/  

![wave06changepasswordpage](doc/screenshots/wave06.png)  

- Testimonial detail page: https://testimonials-aeb7081fc7ea.herokuapp.com/testimonial/13/

![wave08testimonialdetailpage](doc/screenshots/wave08.png)

- Testimonial edit page: https://testimonials-aeb7081fc7ea.herokuapp.com/testimonial/13/edit/  

![wave09estimonialeditpage](doc/screenshots/wave09.png)

- Testimonial delete page: https://testimonials-aeb7081fc7ea.herokuapp.com/testimonial/13/delete/  

![wave10testimonialdeletepage](doc/screenshots/wave10.png)  

- Password reset page: https://testimonials-aeb7081fc7ea.herokuapp.com/accounts/password_reset/  

![wave11passwordresetpage](doc/screenshots/wave11.png)  

- Done password reset message page: https://testimonials-aeb7081fc7ea.herokuapp.com/accounts/password_reset/done/  

![wave12passwordresetmessagepage](doc/screenshots/wave12.png)  


#### Lighthouse  

**Pages that had no problems:**  

- Login page: https://testimonials-aeb7081fc7ea.herokuapp.com/accounts/login/  

![lighthouse01loginpage](doc/screenshots/lighthouse01.png)

- Signup page: https://testimonials-aeb7081fc7ea.herokuapp.com/accounts/signup/  

![lighthouse02signuppage](doc/screenshots/lighthouse02.png)

- Contact page: https://testimonials-aeb7081fc7ea.herokuapp.com/contact/  

![lighthouse03contactpage](doc/screenshots/lighthouse03.png)

- Submit testimonial page: https://testimonials-aeb7081fc7ea.herokuapp.com/testimonial/add/  

![lighthouse04submittestimonialpage](doc/screenshots/lighthouse04.png)

- Change password page: https://testimonials-aeb7081fc7ea.herokuapp.com/accounts/password_change/  

![lighthouse05changepasswordpage](doc/screenshots/lighthouse05.png)  

- Testimonial edit page: https://testimonials-aeb7081fc7ea.herokuapp.com/testimonial/13/edit/  

![lighthouse06estimonialeditpage](doc/screenshots/lighthouse06.png)

- Testimonial delete page: https://testimonials-aeb7081fc7ea.herokuapp.com/testimonial/13/delete/  

![lighthouse07testimonialdeletepage](doc/screenshots/lighthouse07.png)  

- Password reset page: https://testimonials-aeb7081fc7ea.herokuapp.com/accounts/password_reset/  

![lighthouse14passwordresetpage](doc/screenshots/lighthouse14.png)  

- Done password reset message page: https://testimonials-aeb7081fc7ea.herokuapp.com/accounts/password_reset/done/  

![lighthouse15passwordresetmessagepage](doc/screenshots/lighthouse15.png)  


**Pages that had problems:**

- Initial page: https://testimonials-aeb7081fc7ea.herokuapp.com/  

**BEFORE**  

![lighthouse08initialpagebefore](doc/screenshots/lighthouse08.png)  

Mixed Content Error.  
To fix the Mixed Content issue and force all Cloudinary images to be uploaded using HTTPS, I set secure=True in cloudinary.config and adjusted the MEDIA_URL (MEDIA_URL = f'https://res.cloudinary.com/{cloudinary.config().cloud_name}/image/upload/').  

Console showing errors:  

![console01](doc/screenshots/console01.png)  

**AFTER**  

![lighthouse09initialpageafter](doc/screenshots/lighthouse09.png) 

**Problems to solve:**  

![lighthouse10initialpage](doc/screenshots/lighthouse10.png)  

![lighthouse11initialpage](doc/screenshots/lighthouse11.png)  


- Testimonial detail page: https://testimonials-aeb7081fc7ea.herokuapp.com/testimonial/13/  

**BEFORE**  

![lighthouse12testimonialdetailpage](doc/screenshots/lighthouse12.png)  

ERRORS:  
![errors01](doc/screenshots/errors01.png)

To fix the error I created templatetags/ cloudinary_filters.py and updated the image tag in testimonial_detail.html (src="{{ testimonial.image.url|cloudinary_optimize }}"
alt="Photo for {{ testimonial.title }}"loading="lazy">).

**AFTER**

![lighthouse13testimonialdetailpage](doc/screenshots/lighthouse13.png) 


---

## Deployment
[▲ Back to Top](#volunteer-testimonials---hopebridge-community)  

- Steps for deployment:

  - Create a new Heroku app
  - Set the buildpack to Python 
  - Link the Heroku app to the Github repository
  - Click on Deploy

---

## Credits
[▲ Back to Top](#volunteer-testimonials---hopebridge-community)

All of Code Institute's classes (from the beginning to the present) have been the foundation of my learning (although I completely forgot about the Django AllAuth classes and did so much manually).
I conducted research using: chatGPT, YouTube, Google, and GitHub.
The content of the testimonials was created by me based on my experiences with some social activities I engaged in throughout my life while living in Brazil.
I found the images on Google Images (I chose the Creative Commons licensed search engine) to complement the testimonials:
images source: 
https://itoldya420.getarchive.net/amp/media/coast-guard-station-crew-visits-nursing-facility-for-valentines-day-dvids1094304-583d1b  
https://www.streetlab.org/2018/08/28/making-a-place-for-learning-at-nyc-play-streets/  
https://cura.org.au/  
https://picryl.com/media/help-child-charity-people-908b3c
https://aserghc.com.br/festa-das-criancas-reune-milhares-de-trabalhadores-e-suas-familias