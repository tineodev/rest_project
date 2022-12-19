from rest_framework.pagination import PageNumberPagination

class Paginacion(PageNumberPagination):
    page_size = 10
    page_query_param = 'page_size'