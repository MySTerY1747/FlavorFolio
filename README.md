# 🍽️ FlavorFolio: The Ultimate Recipe Sharing Platform  

_"Where Culinary Creativity Meets Community Connection"_  

## 🚀 About FlavorFolio  

See the live version at [FlavorFolio](https://stefanosmyt.pythonanywhere.com/)
  
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

### Prerequisites

- Python 3.x
- pip (Python package manager)
- Git

### Project Setup

1. Clone the repository:

```bash
git clone https://github.com/MySTerY1747/FlavorFolio
cd FlavorFolio
```

2. Create and activate a virtual environment (recommended):

```bash
python -m venv venv
source venv/bin/activate  # On Windows use `venv\Scripts\activate`
```

3. Install required packages:

```bash
pip install -r requirements.txt
```

### Database Setup

1. Initialize the database:

```bash
python manage.py makemigrations recipes
python manage.py migrate
```

2. Populate initial data:

```bash
python population_script.py
```

3. Optinally create a superuser for admin access:

```bash
python manage.py createsuperuser
```

- Access the admin panel at `http://127.0.0.1:8000/admin/`

### Development Workflow

1. Make your changes to the code

2. Add, commit, and push your changes:

```bash
git add .
git commit -m "Your commit message"
git push
```

3. Periodically pull changes from the main branch:

```bash
git pull origin main
```
