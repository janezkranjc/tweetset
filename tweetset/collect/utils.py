from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage

def pagination_helper(object_list,page,per_page=10,allow_empty_first_page=True):
    paginator = Paginator(object_list=object_list, per_page=per_page, allow_empty_first_page=allow_empty_first_page)
    try:
        appcontacts = paginator.page(page)
    except PageNotAnInteger:
        appcontacts = paginator.page(1)
    except EmptyPage:
        appcontacts = paginator.page(paginator.num_pages)

    adjacent_pages=2

    startPage = max(appcontacts.number - adjacent_pages, 1)
    if startPage <= 3: startPage = 1
    endPage = appcontacts.number + adjacent_pages + 1
    if endPage >= paginator.num_pages - 1: endPage = paginator.num_pages + 1
    page_numbers = [n for n in range(startPage, endPage) \
            if n > 0 and n <= paginator.num_pages]

    show_first = 1 not in page_numbers
    show_last = paginator.num_pages not in page_numbers
    return (appcontacts, show_first, show_last, page_numbers)