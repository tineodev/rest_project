from rest_framework.pagination import PageNumberPagination

class Pagination_own(PageNumberPagination):
    page_size = 15
    page_query_param = 'page_size'