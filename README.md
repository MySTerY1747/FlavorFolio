# 🍽️ FlavorFolio: The Ultimate Recipe Sharing Platform  

_"Where Culinary Creativity Meets Community Connection"_  

## 🚀 About FlavorFolio  
  
FlavorFolio is a sleek, user-friendly, and community-driven platform where food lovers can explore, share, and connect through recipes. Whether you're a home cook or a seasoned chef, FlavorFolio makes it easy to discover new dishes, showcase your culinary creations, and engage with a vibrant community.  
  
## ✨ Features  
  
- 🔍 **Explore Recipes** – Search, filter, and discover dishes by cuisine, diet, and more.  
  
- 🍳 **Share Your Creations** – Upload and showcase your recipes with ease.  
  
- 💬 **Engage & Connect** – Comment on and save your favorite recipes.  
  
- 🏷️ **Tagging System** – Categorize recipes with tags (e.g., cuisine, dietary preferences).  
  
- 🔐 **User Management** – Secure account creation, login, and profile customization.  
  
- ⭐ **Save & Rate** _(Planned)_ – Bookmark your favorite recipes and leave reviews.  
  
- 🔧 **Admin Controls** – Moderation tools for managing users and content.  

## 🌟 Why FlavorFolio?  

- **📱 Intuitive & Modern** – A clean, easy-to-use interface for a seamless experience.  

- **📈 Scalable & Future-Ready** – Designed to grow with an expanding user base.  

- **💡 Community-Driven** – Built to foster engagement and shared culinary creativity.  
  
## 🛠️ Tech Stack  

FlavorFolio is powered by:  

- **Frontend:** Standard CSS,
- **Backend:** Python Django
- **Database:** SQLite database
- **Version Control:** Git & GitHub  

## Development

### Project setup

1. Clone the repository:

```bash
git clone https://github.com/MySTerY1747/FlavorFolio
```

2. Make your changes

3. Add, commit, and push your changes:

```bash
git add .
git commit -m "Your commit message"
git push
```

4. Periodically pull changes from the main branch:

```bash
git pull origin main
```

### Requirements

To install the required packages, run the following command:

```bash
pip install -r requirements.txt
```

### Database setup

- To setup the database, run the following commands:

```bash
python manage.py makemigrations recipes
python manage.py migrate
```

- Then use the auto-populate script to populate the database with some initial data:

```bash
python population_script.py
```

- Consider adding a superuser to access the Django admin panel:

```bash
python manage.py createsuperuser
```

- You can then access the admin panel at `http://127.0.0.1:8000/admin/`

---  

# 🏗️ Project Roadmap  

Whenever you commit your chnages, make sure to update the project roadmap below.

## 1. Project Setup & Repository Management  ✅ - Completed on 07/03 by Stefanos

- **Environment & Version Control:**
  - Initialize a Git repository and set up a virtual environment.
  - Create a new Django project (e.g., “flavorfolio”) with a basic structure.
  - Generate a `requirements.txt` file using `pip freeze` and add it to the repository.
  - Exclude sensitive files (like your database) from version control.

## 2. Define Apps & Project Structure ✅ - Completed on 07/03 by Stefanos

- **Modular Design:**  
  - Create separate apps for different functionalities, for example:
    - **recipes:** Handles recipe uploads, management, and display.
    - **users:** Manages user authentication and profiles.
- **Directory Organization:**  
  - Establish clear folder structures for templates (using Django template inheritance), static assets (CSS, JavaScript), and media files (for recipe images).

## 3. Django Settings & Asset Configuration ✅ - Completed on 07/03 by Stefanos

- **Static Files Configuration:**  
  - In your `settings.py`, define `STATIC_URL` (e.g., `/static/`) and set up `STATICFILES_DIRS` to include your project’s static assets.
  - For production (PythonAnywhere), ensure you configure the static file serving settings as per their documentation.
- **Media Files Setup:**  
  - Define `MEDIA_URL` (e.g., `/media/`) and `MEDIA_ROOT` (a directory to store uploaded images) in `settings.py`.
  - Create the media directory structure on your file system.
- **Database Setup:**  
  - Configure your database settings (using SQLite for development, or another database for production) and apply initial migrations.

## 4. Database & Model Design ✅ - Completed on 08/03 by Stefanos

- **Model Creation:**  
  - Define your models in the respective apps. For example:
    - **Recipe Model:** Fields like title, ingredients, instructions, image, and relationships (e.g., many-to-many with tags).
    - **Tag Model:** For categorizing recipes.
    - **UserProfile Model:** Extend Django’s User model to include bio and profile image.
- **Migrations:**  
  - Create and apply migrations to generate the corresponding database tables.

## 5. Population Script Development ✅ - Completed on 09/03 by Stefanos

- **Script Purpose:**  
  - Write a Python script (e.g., `population_script.py`) that uses Django’s ORM to seed your database with sample data.
- **Implementation Details:**  
  - Import your models and create several instances (recipes, tags, user profiles) with realistic sample data.
  - Consider adding the script as a custom Django management command for easier execution.
- **Testing the Script:**  
  - Run the script using `python manage.py shell` or your custom command to verify that the sample data is correctly inserted.

## 6. User Authentication & Access Control

- **Built-in Auth System:**  
  - Leverage Django’s authentication system for user registration, login, logout, and account management.
- **Profile Management:**  
  - Create views and templates that allow users to update their profiles and view their uploaded recipes.
- **Admin Setup:**  
  - Configure the Django admin to enable administrators to manage users and moderate content.

## 7. Core Functionality Implementation

- **Recipe Management:**  
  - Develop views, forms, and templates for uploading, editing, deleting, and displaying recipes (e.g., detail pages at `/recipes/<recipe_id>`).
- **Tagging & Search:**  
  - Implement a tagging system to categorize recipes.
  - Build search functionality (supporting `/search` and `/search/<query>`) to filter recipes by keywords and tags.
- **Dynamic Interactions:**  
  - Integrate JavaScript, JQuery, and AJAX for features like live search suggestions and dynamic content updates.

## 8. Front-end Design & Look and Feel

- **UI/UX Improvements:**  
  - Use a responsive CSS framework (such as Bootstrap) to create an intuitive, polished interface.
  - Apply Django’s template inheritance to ensure consistent design across pages.
- **Asset Management:**  
  - Ensure CSS and JavaScript files are kept separate from your HTML templates for maintainability.
- **Navigation & Layout:**  
  - Develop navigation elements (e.g., homepage with top recipes, profile pages) following your project’s sitemap and wireframes.

## 9. Testing & Code Quality

- **Unit Testing:**  
  - Write tests for models, views, and forms to verify that each component works as expected.
- **Code Practices:**  
  - Keep your code clean and DRY (Don’t Repeat Yourself), using helper functions and comments where needed.
  - Use relative URLs in templates (with the `{% url %}` tag) to maintain flexibility in your URL structure.

## 10. Final Checks & Deployment

- **Comprehensive Review:**  
  - Ensure that all core functionalities (user authentication, recipe management, search, etc.) are bug-free and meet the design specifications.
- **Deployment Preparation:**  
  - Finalize your production settings (static file handling, security settings, etc.) for PythonAnywhere.
  - Deploy your application on PythonAnywhere and test thoroughly in both local and production environments.
- **Documentation & Submission:**  
  - Prepare a one-page document with project details (name, team info, GitHub URL, PythonAnywhere URL, external sources used) for submission.
