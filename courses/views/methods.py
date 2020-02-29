from rest_framework.response import Response


def custom_list(obj, request, *args, **kwargs):
    queryset = obj.filter_queryset(obj.get_queryset(*args, **kwargs))
    page = obj.paginate_queryset(queryset)
    if page is not None:
        serializer = obj.get_serializer(page, many=True)
        return obj.get_paginated_response(serializer.data)

    serializer = obj.get_serializer(queryset, many=True)
    return Response(serializer.data)
