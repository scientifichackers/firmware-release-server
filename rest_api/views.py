import semantic_version
from django.http import HttpResponseBadRequest, HttpResponse
from rest_framework.generics import RetrieveAPIView
from rest_framework.response import Response

from firmware_uploads.models import FirmwareUpload
from rest_api.serializers import FirmwareUploadSerializer


class HttpResponseNoContent(HttpResponse):
    status_code = 204


class LatestFirmwareView(RetrieveAPIView):
    queryset = FirmwareUpload.objects.all()
    serializer_class = FirmwareUploadSerializer
    lookup_field = "pk"

    def retrieve(self, request, *args, **kwargs):
        qs = self.get_queryset()

        try:
            version = kwargs["version"]
        except KeyError:
            pass
        else:
            try:
                semver = semantic_version.Version(version)
            except ValueError:
                return HttpResponseBadRequest(
                    f'Invalid semantic version string: "{version}".'
                )
            qs = qs.higher_version_than(semver)

        if not qs.exists():
            return HttpResponseNoContent()

        latest = qs.latest()
        serializer = self.get_serializer(latest)
        response = Response(serializer.data)

        return response
