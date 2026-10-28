# Pet Oasis

> "Care for every paw, home for every heart"

Pet Oasis is a Django web application for a fictional chain of pet hotels and shelters. Visitors can browse the hotel locations, create an account, and register their pets; the site also has an about page and a blog/news page.

![Screenshot](docs/home.png)

## Features

Derived from the models, views, URLs and templates in `PetOasis/`:

**Accounts** (`accounts`)
- Registration with username, email, first/last name and age; users under 18 are rejected, and the new user is logged in automatically.
- Login and logout.
- Profile page showing the user's picture and registered pets.
- Edit account: change username, email, profile picture and password (current password required).
- Delete account with password confirmation; the profile and the user's pets are deleted with it.
- Custom user model (`AppUser`, username-based login) with a one-to-one `Profile`.

**Pets** (`pets`)
- Logged-in users can register a pet: name, species (dog / cat / bird), optional breed, age, weight and optional photo.
- Delete a pet through a confirmation page. There is no edit view for pets.

**Facilities** (`facilities`)
- List of pet hotels (`PetHotel`: city, address, contact details, description, image URL) and a detail page per city.
- A `Shelter` model (dog / cat section per hotel) exists, but I could not find a view that lists it (verify).

**Home, Blog & News, About us**
- Home page shows the first three hotels and up to seven `PawPost` "customer feedback" cards.
- The Blog & News and About us pages appear to be static templates with hard-coded content (verify).

**Admin**
- Only the user model (with a profile inline) is registered in the Django admin. Hotels, shelters and paw posts have no admin registration yet, so they must be created from the shell (verify).

**Operations**
- `PetOasis/scripts/backup_db.sh`: dumps the PostgreSQL database with `pg_dump` to a gzipped file in `~/petoasis-backups` (override with `BACKUP_DIR`) and keeps the 5 newest backups.

## Tech stack

- Python 3 (3.12 used in development; other versions: verify), Django 5.2
- PostgreSQL via `psycopg2-binary`
- Pillow for image uploads
- `python-dotenv` for loading a local `.env`
- `gunicorn` is listed in `requirements.txt` for deployment; no deployment config is in the repo (verify)
- `django-crispy-forms` / `crispy-bootstrap4` are listed in `requirements.txt` but are commented out in `INSTALLED_APPS`, so they appear unused (verify)
- Django templates, Bootstrap 5.3 and custom CSS/JS in `PetOasis/static/`

## Run locally

Prerequisites: Python 3, and a running PostgreSQL server.

**1. Create the database and role** (the defaults below match the settings; use your own password):

```sql
CREATE USER petoasis WITH PASSWORD 'choose-a-password';
CREATE DATABASE pet_oasis_db OWNER petoasis;
```

**2. Install and configure**

```bash
git clone https://github.com/HristiyanIliev06/Pet-Oasis.git
cd Pet-Oasis

python -m venv venv
# Windows: venv\Scripts\activate      macOS/Linux: source venv/bin/activate
pip install -r requirements.txt
```

Create a file named `.env` inside `PetOasis/` (next to `manage.py`). It is git-ignored. `load_dotenv()` searches upwards from `settings.py`, so one in the repository root also works.

```
DB_PASSWORD=the-password-you-chose
# Optional - these are the defaults:
# DB_NAME=pet_oasis_db
# DB_USER=petoasis
# DB_HOST=127.0.0.1
# DB_PORT=5432
```

`DB_PASSWORD` is required: Django will fail with a `KeyError` without it.

**3. Migrate and run**

```bash
cd PetOasis
python manage.py migrate
python manage.py createsuperuser
python manage.py runserver
```

Open http://127.0.0.1:8000/.

The facilities pages need `PetHotel` rows; the admin does not expose them yet, so add some through `python manage.py shell` (verify).

### Database backup

```bash
# needs bash and pg_dump on PATH; reads the same DB_* variables (DB_PASSWORD required)
DB_PASSWORD=... bash PetOasis/scripts/backup_db.sh
```

## Project structure

```
Pet-Oasis/
├── requirements.txt
└── PetOasis/                 # Django project root (manage.py lives here)
    ├── PetOasis/             # settings, root URLconf, wsgi/asgi
    ├── accounts/             # AppUser, Profile, auth + account views/forms
    ├── pets/                 # Pet model, register/delete views
    ├── facilities/           # PetHotel, Shelter, facility pages
    ├── blog_and_news/        # PawPost model, blog page
    ├── index/                # home page
    ├── about_us/             # about page
    ├── core/                 # shared validators
    ├── scripts/              # backup_db.sh
    ├── templates/            # project-wide HTML templates
    ├── static/               # CSS, JS, Bootstrap, images
    └── media/                # user uploads (git-ignored)
```

## Status and next steps

Work in progress, built as a learning/portfolio project.

**Configuration**
- Only the database settings come from the environment. `SECRET_KEY`, `DEBUG = True` and `ALLOWED_HOSTS = ['*']` are still hard-coded in `PetOasis/PetOasis/settings.py`, so the project is **not production-ready** yet. Move them to environment variables and rotate the secret key, since the old one is in git history.
- Add a `.env.example` documenting the variables.

**Product**
- No booking flow: a `Booking` model was removed in an earlier migration, although the profile page still says pets are registered "for future booking".
- The profile page contains placeholder content ("Your Offers", "Your Discount Cards", sample pets) (verify).
- The `PawPost` create form/view is commented out and the Blog & News page is not driven by the database.
- Register `PetHotel`, `Shelter` and `PawPost` in the admin.

**Quality**
- There are no automated tests yet: every app's `tests.py` is the empty default stub.
- Known issues found while reading the code (verify before fixing):
  - The hotel-name validator in `core/validators.py` calls `isalpha()` on the whole name, so it rejects every name containing a space.
  - `show_profile` has `@login_required` commented out, and `PetDeleteView` does not check that the pet belongs to the logged-in user.
  - `LOGIN_URL` is not set, so login-required redirects go to `/accounts/login/` instead of the project's `/account/login/`.
  - Visiting a facility URL for an unknown city raises an unhandled `DoesNotExist` instead of a 404.
- Replace the placeholder screenshot: add `docs/home.png`.
