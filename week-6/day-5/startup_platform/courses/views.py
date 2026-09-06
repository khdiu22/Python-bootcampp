from django.shortcuts import render


def course_list(request):
    return render(request, 'courses/course_list.html')


def course_detail(request, slug):
    return render(request, 'courses/course_detail.html', {
        'slug': slug
    })


def category(request, category_name):
    return render(request, 'courses/category.html', {
        'category_name': category_name
    })