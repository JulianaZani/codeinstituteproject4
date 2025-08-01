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


## Credits

images source
https://itoldya420.getarchive.net/amp/media/coast-guard-station-crew-visits-nursing-facility-for-valentines-day-dvids1094304-583d1b
https://www.streetlab.org/2018/08/28/making-a-place-for-learning-at-nyc-play-streets/
https://www.flickr.com/photos/adamthelibrarian/14693926095
https://cura.org.au/
https://picryl.com/media/help-child-charity-people-908b3c
https://aserghc.com.br/festa-das-criancas-reune-milhares-de-trabalhadores-e-suas-familias/