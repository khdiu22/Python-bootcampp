# Guided Lab: Parameter-Aware Catalog

A small Django project that implements every step of the lab as **one
connected app** instead of disconnected examples.

## How the 8 steps map to the code

| # | Requirement | Where |
|---|---|---|
| 1 | Create `courses` app and a mock course list | `courses/data.py` (`COURSES` list) |
| 2 | `/courses/` list route and `/courses/<int:id>/` detail route | `courses/urls.py` |
| 3 | Read `category` and `difficulty` from `request.GET` | `views.course_list` |
| 4 | Filter the list, handle missing values gracefully | `views.course_list` (falls back to "no filter" / "no results" instead of crashing) |
| 5 | Search field with `method="get"` | `templates/courses/course_list.html` (`<form method="get">`) |
| 6 | Detail tabs using `?tab=details/syllabus/instructor` | `views.course_detail` + `templates/courses/course_detail.html` |
| 7 | `{% url %}` with parameters for detail links | used throughout the list/detail templates |
| 8 | Basic pagination using the `page` query parameter | `views.course_list` (Django `Paginator`) |

## Run it

```bash
python -m venv venv
source venv/bin/activate      # on Windows: venv\Scripts\activate
pip install -r requirements.txt
python manage.py migrate      # creates the (unused-by-this-lab) admin tables
python manage.py runserver
```

Then open **http://127.0.0.1:8000/courses/**

## Exit ticket — 3 working URLs

1. **Filtered URL**
   `http://127.0.0.1:8000/courses/?category=programming&difficulty=beginner`

2. **Detail URL**
   `http://127.0.0.1:8000/courses/2/`

3. **Tab URL**
   `http://127.0.0.1:8000/courses/2/?tab=syllabus`

You can also combine search + filters + pagination, e.g.:
`http://127.0.0.1:8000/courses/?q=design&category=design&page=2`

## Notes on the "graceful handling" in step 4

- An unknown/garbage value in `?category=` or `?difficulty=` is simply
  ignored (treated as "no filter"), instead of raising an error.
- If a filter combination matches zero courses, the list page shows a
  friendly "No courses match your filters" message rather than a blank
  page.
- Pagination uses `Paginator.get_page()`, which never raises on a
  missing, non-numeric, or out-of-range `page` value — it quietly falls
  back to page 1 (or the last valid page).
- Visiting a course id that doesn't exist (e.g. `/courses/999/`) raises
  a normal Django 404 instead of a server error.
- An invalid `?tab=` value quietly falls back to the `details` tab.
