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
