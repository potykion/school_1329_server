from django.http import HttpResponse


def response_content_to_str(response: HttpResponse) -> str:
    """
    Convert response content to utf-8 string.
    :param response: HttpResponse.
    :return: UTF-8 string.
    """
    return response.content.decode('utf-8')
