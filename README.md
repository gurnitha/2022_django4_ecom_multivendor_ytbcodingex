# 2022_django4_ecom_multivendor_ytbcodingex
BUILDING MULTIVENDOR ECOMMERCE USING DJANGO 4


#### 1. Create a new django project 'config'


#### 2. Create a new app 'app/main'


#### 3. Creating paths for templates, static and media files

        modified:   config/settings.py
        modified:   config/urls.py


#### 4. Adding home page template and loading static and media files

        modified:   .gitignore
        modified:   README.md
        deleted:    app/main/views.py
        renamed:    app/main/__init__.py -> app/products/__init__.py
        renamed:    app/main/admin.py -> app/products/admin.py
        renamed:    app/main/apps.py -> app/products/apps.py
        renamed:    app/main/migrations/__init__.py -> app/products/migrations/__init__.py
        renamed:    app/main/models.py -> app/products/models.py
        renamed:    app/main/tests.py -> app/products/tests.py
        new file:   app/products/urls.py
        new file:   app/products/views.py
        modified:   config/settings.py
        modified:   config/urls.py
        new file:   templates/products/index.html