HOW TO USE
==========
1. Put the "courses" folder inside your Django app folder (or rename your
   existing app to "courses" and merge these files in).
2. Copy the contents of project_urls.py into your project's main urls.py
   (the one next to settings.py) — just the "include" line matters.
3. Make sure your settings.py has "courses" in INSTALLED_APPS and
   STATIC_URL = "static/" is set (default in new projects).

IMAGES YOU STILL NEED TO ADD
=============================
Save these 5 images into: courses/static/courses/images/
Use these exact filenames (the templates already reference them):

  python.jpg       -> for "Python for Beginners"
  django.jpg        -> for "Django Web Development"
  dsa.jpg            -> for "Data Structures and Algorithms"
  webdesign.jpg   -> for "Web Design with HTML and CSS"
  database.jpg    -> for "Database Systems"

Recommended size: roughly 400x250px (landscape), JPG or PNG, each under ~300KB
so the pages load fast.
