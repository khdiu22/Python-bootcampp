from django.core.paginator import Paginator
from django.shortcuts import render
from django.http import Http404

from .data import get_all_courses, get_course_by_id

# Valid choices used to build the filter <select> boxes and to validate
# whatever comes in through request.GET.
CATEGORY_CHOICES = ["programming", "design", "marketing", "data", "business"]
DIFFICULTY_CHOICES = ["beginner", "intermediate", "advanced"]

# Which tabs are allowed on the detail page (step 6).
VALID_TABS = ["details", "syllabus", "instructor"]

PAGE_SIZE = 6


def course_list(request):
    """
    /courses/

    Step 3: read category and difficulty from request.GET
    Step 4: filter the list and handle missing/invalid values gracefully
    Step 5: search field (?q=) using method="get"
    Step 8: basic pagination using the "page" query parameter
    """
    all_courses = get_all_courses()

    # --- Step 3 & 5: read filters + search term from request.GET -----
    # .get(..., "") means a missing key never raises a KeyError - it just
    # behaves as "no filter applied".
    category = request.GET.get("category", "").strip()
    difficulty = request.GET.get("difficulty", "").strip()
    query = request.GET.get("q", "").strip()

    # --- Step 4: handle missing/invalid values gracefully -------------
    # If someone hand-types ?category=doesnt-exist in the URL, we don't
    # want a crash or a confusing empty page - we simply treat it as
    # "not a real filter" and ignore it.
    if category not in CATEGORY_CHOICES:
        category = ""
    if difficulty not in DIFFICULTY_CHOICES:
        difficulty = ""

    filtered_courses = all_courses

    if category:
        filtered_courses = [c for c in filtered_courses if c["category"] == category]

    if difficulty:
        filtered_courses = [c for c in filtered_courses if c["difficulty"] == difficulty]

    if query:
        query_lower = query.lower()
        filtered_courses = [
            c for c in filtered_courses if query_lower in c["title"].lower()
        ]

    # --- Step 8: basic pagination using ?page= ------------------------
    paginator = Paginator(filtered_courses, PAGE_SIZE)
    page_number = request.GET.get("page", "1")
    page_obj = paginator.get_page(page_number)  # get_page() never crashes
    # on a bad/missing page number - it gracefully falls back to page 1
    # (or the last page if the number is too high).

    # Build the current filters as a querystring WITHOUT "page", so
    # pagination links can carry the active filters along with them.
    # e.g. category=programming&difficulty=beginner&q=python
    querystring_params = request.GET.copy()
    querystring_params.pop("page", None)
    base_querystring = querystring_params.urlencode()

    context = {
        "page_obj": page_obj,
        "courses": page_obj.object_list,
        "category": category,
        "difficulty": difficulty,
        "query": query,
        "category_choices": CATEGORY_CHOICES,
        "difficulty_choices": DIFFICULTY_CHOICES,
        "base_querystring": base_querystring,
        "total_count": len(filtered_courses),
    }
    return render(request, "courses/course_list.html", context)


def course_detail(request, course_id):
    """
    /courses/<int:course_id>/

    Step 6: detail tabs using ?tab=details|syllabus|instructor
    Step 7: the list page links here using {% url %} with parameters
    """
    course = get_course_by_id(course_id)
    if course is None:
        raise Http404("This course does not exist.")

    # --- Step 6: read + validate the tab, gracefully falling back -----
    tab = request.GET.get("tab", "details").strip()
    if tab not in VALID_TABS:
        tab = "details"

    context = {
        "course": course,
        "active_tab": tab,
        "tabs": VALID_TABS,
    }
    return render(request, "courses/course_detail.html", context)
