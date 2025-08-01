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

---

## Credits

images source
https://itoldya420.getarchive.net/amp/media/coast-guard-station-crew-visits-nursing-facility-for-valentines-day-dvids1094304-583d1b
https://www.streetlab.org/2018/08/28/making-a-place-for-learning-at-nyc-play-streets/
https://www.flickr.com/photos/adamthelibrarian/14693926095
https://cura.org.au/
https://picryl.com/media/help-child-charity-people-908b3c
https://aserghc.com.br/festa-das-criancas-reune-milhares-de-trabalhadores-e-suas-familias/