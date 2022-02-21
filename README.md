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


#### 5. Creating and extending base template

        modified:   README.md
        new file:   templates/base.html
        modified:   templates/products/index.html
        new file:   templates/shared/back_to_top.html
        new file:   templates/shared/footer.html
        new file:   templates/shared/head.html
        new file:   templates/shared/header.html
        new file:   templates/shared/offcanvas1.html
        new file:   templates/shared/offcanvas2.html
        new file:   templates/shared/preloader.html
        new file:   templates/shared/scripts.html