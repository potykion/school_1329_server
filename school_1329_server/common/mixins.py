from rest_framework.response import Response


class SuccessDestroyMixin:
    def destroy(self, request, *args, **kwargs):
        """
        Delete object with {pk}.
        :return: Response with success flag.
        """
        super(SuccessDestroyMixin, self).destroy(request, *args, **kwargs)
        return Response({'success': True})
