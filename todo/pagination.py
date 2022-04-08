from rest_framework import pagination

class CustomPagination(pagination.PageNumberPagination):
    page_size_query_param = 'count'
    page_size = 5
    max_page_size = 10
    page_query_param = 'p'