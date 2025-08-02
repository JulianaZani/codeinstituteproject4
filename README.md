# Volunteer Testimonials - HopeBridge Community

**Volunteer Testimonials** is a full-stack web application built with Django. It allows users to share and read real-life stories about their experiences participating in social and volunteering projects. The name **HopeBridge Community** was not chosen at the beginning of the project.

The site is designed with accessibility and user experience in mind, following modern development practices using HTML, CSS, JavaScript, Python, and Django.  

---

## Purpose

The purpose of this application is to:

- Provide a platform for users to submit testimonials about volunteering experiences
- Allow visitors to read and get inspired by others’ stories
- Enable administrators to manage, approve, or remove testimonials

---

## Target Users

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

## User Stories

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

![wireframes](doc/screenshots/wireframehomeandaddtestimonial.png)
![wireframes](doc/screenshots/wireframelogincontact.png)

---

## Technologies Used

- **Python 3**
- **Django 5**
- **HTML5 / CSS3**
- **JavaScript**
- **SQLite (development)**
- **PostgreSQL (production)**
- **Cloudinary**
- **Heroku**
- **Git & GitHub**
- **GitHub Projects**

---

## Data Schema  

**ER Diagram**  

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

---


## CRUD Functionality  

The project implements full CRUD functionality for testimonials:  

Create – Users can submit a new testimonial in "Submit Testimonial".  


Read – All testimonials are displayed on the homepage for users to view.  


Update – Logged-in users can edit their testimonials via the "Edit" button.  


Delete – Logged-in users can delete a testimonial they created.  

---

## Testing

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


### W3C CSS Validator  

No errors were found when passing through the official (Jigsaw) validator.  

![w3ccss](doc/screenshots/w3ccss.png)


### Accessibility 

I confirmed that the colors and fonts chosen are easy to read and accessible by running it through lighthouse in devtools and Wave Evolution Tool.  

**WAVE**  

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


**LIGHTHOUSE**  

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


---

## Credits

images source
https://itoldya420.getarchive.net/amp/media/coast-guard-station-crew-visits-nursing-facility-for-valentines-day-dvids1094304-583d1b
https://www.streetlab.org/2018/08/28/making-a-place-for-learning-at-nyc-play-streets/
https://www.flickr.com/photos/adamthelibrarian/14693926095
https://cura.org.au/
https://picryl.com/media/help-child-charity-people-908b3c
https://aserghc.com.br/festa-das-criancas-reune-milhares-de-trabalhadores-e-suas-familias/