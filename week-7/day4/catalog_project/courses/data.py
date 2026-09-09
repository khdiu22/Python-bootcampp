"""
Step 1: Mock course list.

In a real app this would come from the database (a Course model).
For this guided lab we keep it as a simple in-memory list of dicts so we
can focus on request.GET, filtering, templates, and pagination.
"""

COURSES = [
    {
        "id": 1,
        "title": "Python for Beginners",
        "category": "programming",
        "difficulty": "beginner",
        "instructor": "Sarah ",
        "syllabus": "Week 1: Syntax & variables. Week 2: Control flow. "
                     "Week 3: Functions. Week 4: Mini project.",
        "description": "A gentle introduction to Python programming from scratch.",
    },
    {
        "id": 2,
        "title": "Django Web Development",
        "category": "programming",
        "difficulty": "intermediate",
        "instructor": "Omar",
        "syllabus": "Week 1: Models & migrations. Week 2: Views & URLs. "
                     "Week 3: Templates. Week 4: Deployment.",
        "description": "Build full web applications using the Django framework.",
    },
    {
        "id": 3,
        "title": "Advanced Algorithms",
        "category": "programming",
        "difficulty": "advanced",
        "instructor": "Layla ",
        "syllabus": "Week 1: Graphs. Week 2: Dynamic programming. "
                     "Week 3: Greedy algorithms. Week 4: NP-completeness.",
        "description": "Deep dive into algorithmic problem solving for technical interviews.",
    },
    {
        "id": 4,
        "title": "UI/UX Design Fundamentals",
        "category": "design",
        "difficulty": "beginner",
        "instructor": "Nora",
        "syllabus": "Week 1: Design principles. Week 2: Wireframing. "
                     "Week 3: Prototyping. Week 4: User testing.",
        "description": "Learn the basics of designing usable, attractive interfaces.",
    },
    {
        "id": 5,
        "title": "Advanced Motion Design",
        "category": "design",
        "difficulty": "advanced",
        "instructor": "Fahad",
        "syllabus": "Week 1: Easing & timing. Week 2: After Effects. "
                     "Week 3: Micro-interactions. Week 4: Portfolio piece.",
        "description": "Create polished animations and micro-interactions for products.",
    },
    {
        "id": 6,
        "title": "Design Systems in Practice",
        "category": "design",
        "difficulty": "intermediate",
        "instructor": "Nora",
        "syllabus": "Week 1: Tokens. Week 2: Components. "
                     "Week 3: Documentation. Week 4: Governance.",
        "description": "Build and maintain a scalable design system for a product team.",
    },
    {
        "id": 7,
        "title": "Digital Marketing Basics",
        "category": "marketing",
        "difficulty": "beginner",
        "instructor": "Huda ",
        "syllabus": "Week 1: Channels overview. Week 2: SEO basics. "
                     "Week 3: Social media. Week 4: Analytics.",
        "description": "An overview of how digital marketing channels work together.",
    },
    {
        "id": 8,
        "title": "Growth Marketing Strategy",
        "category": "marketing",
        "difficulty": "intermediate",
        "instructor": "Turki ",
        "syllabus": "Week 1: Funnels. Week 2: A/B testing. "
                     "Week 3: Retention. Week 4: Growth loops.",
        "description": "Design experiments and funnels that grow a product sustainably.",
    },
    {
        "id": 9,
        "title": "Performance Ad Campaigns",
        "category": "marketing",
        "difficulty": "advanced",
        "instructor": "Huda ",
        "syllabus": "Week 1: Bidding strategy. Week 2: Attribution. "
                     "Week 3: Creative testing. Week 4: Budget scaling.",
        "description": "Run and optimize high-budget paid acquisition campaigns.",
    },
    {
        "id": 10,
        "title": "Business Data Analysis",
        "category": "data",
        "difficulty": "beginner",
        "instructor": "Mohammed ",
        "syllabus": "Week 1: Excel & spreadsheets. Week 2: SQL basics. "
                     "Week 3: Dashboards. Week 4: Reporting.",
        "description": "Learn to read, clean, and present business data clearly.",
    },
    {
        "id": 11,
        "title": "Applied Machine Learning",
        "category": "data",
        "difficulty": "intermediate",
        "instructor": "Reem ",
        "syllabus": "Week 1: Regression. Week 2: Classification. "
                     "Week 3: Model evaluation. Week 4: Deployment.",
        "description": "Train and evaluate practical machine learning models.",
    },
    {
        "id": 12,
        "title": "Deep Learning for NLP",
        "category": "data",
        "difficulty": "advanced",
        "instructor": "Reem ",
        "syllabus": "Week 1: Embeddings. Week 2: Transformers. "
                     "Week 3: Fine-tuning. Week 4: Evaluation.",
        "description": "Understand and apply modern deep learning to text data.",
    },
    {
        "id": 13,
        "title": "Product Management 101",
        "category": "business",
        "difficulty": "beginner",
        "instructor": "Khalid ",
        "syllabus": "Week 1: Discovery. Week 2: Roadmaps. "
                     "Week 3: Metrics. Week 4: Launch.",
        "description": "The fundamentals of managing a product from idea to launch.",
    },
    {
        "id": 14,
        "title": "Financial Modeling",
        "category": "business",
        "difficulty": "intermediate",
        "instructor": "Amal",
        "syllabus": "Week 1: Statements. Week 2: Forecasting. "
                     "Week 3: Valuation. Week 4: Scenario analysis.",
        "description": "Build financial models to support real business decisions.",
    },
    {
        "id": 15,
        "title": "Startup Fundraising Strategy",
        "category": "business",
        "difficulty": "advanced",
        "instructor": "Khalid ",
        "syllabus": "Week 1: Cap tables. Week 2: Term sheets. "
                     "Week 3: Investor pitching. Week 4: Negotiation.",
        "description": "Navigate the fundraising process for an early-stage startup.",
    },
    {
        "id": 16,
        "title": "Frontend Development with React",
        "category": "programming",
        "difficulty": "intermediate",
        "instructor": "Omar ",
        "syllabus": "Week 1: Components. Week 2: State & props. "
                     "Week 3: Hooks. Week 4: Routing.",
        "description": "Build interactive single-page applications using React.",
    },
    {
        "id": 17,
        "title": "Brand Identity Design",
        "category": "design",
        "difficulty": "beginner",
        "instructor": "Fahad",
        "syllabus": "Week 1: Logo design. Week 2: Color & type. "
                     "Week 3: Brand guidelines. Week 4: Applications.",
        "description": "Create a cohesive visual identity for a brand from scratch.",
    },
    {
        "id": 18,
        "title": "SQL for Data Analysts",
        "category": "data",
        "difficulty": "beginner",
        "instructor": "khdijah",
        "syllabus": "Week 1: SELECT & WHERE. Week 2: JOINs. "
                     "Week 3: Aggregation. Week 4: Window functions.",
        "description": "Query and analyze relational databases confidently with SQL.",
    },
]


def get_all_courses():
    """Return the full mock course list."""
    return COURSES


def get_course_by_id(course_id):
    """Return a single course dict by id, or None if not found."""
    for course in COURSES:
        if course["id"] == course_id:
            return course
    return None
