import semantic_version
from django.db import models

from firmware_release_server import settings


def build_firmware_path(instance, _):
    return f"{settings.FIRMWARE_UPLOAD_DIR_NAME}/{instance.version}/firmware.bin"


def build_bootloader_path(instance, _):
    return f"{settings.FIRMWARE_UPLOAD_DIR_NAME}/{instance.version}/bootloader.bin"


def build_partitions_path(instance, _):
    return f"{settings.FIRMWARE_UPLOAD_DIR_NAME}/{instance.version}/partitions.bin"


class FirmwareUploadQuerySet(models.QuerySet):
    def higher_version_than(self, semver: semantic_version.Version):
        # try getting objects with higher "major" version
        filter_qs = self.filter(major_version__gt=semver.major)

        if not filter_qs.exists():
            # try getting objects with same "major" version, but higher "minor" version.
            filter_qs = self.filter(
                major_version__gte=semver.major, minor_version__gt=semver.minor
            )

        if not filter_qs.exists():
            # try getting objects with same "major" and "minor" version, but higher "patch" version.
            filter_qs = self.filter(
                major_version__gte=semver.major,
                minor_version__gte=semver.minor,
                patch_version__gt=semver.patch,
            )

        return filter_qs


SEMVER_ORDER = ("major_version", "minor_version", "patch_version")


class FirmwareUpload(models.Model):
    major_version = models.IntegerField()
    minor_version = models.IntegerField()
    patch_version = models.IntegerField()
././
    firmware_bin = models.FileField(upload_to=build_firmware_path)
    bootloader_bin = models.FileField(upload_to=build_bootloader_path)
    partitions_bin = models.FileField(upload_to=build_partitions_path)

    comments = models.CharField(max_length=1000, default="")
    uploaded_at = models.DateTimeField(auto_now_add=True)
    deferred = models.BooleanField(default=False)

    objects = FirmwareUploadQuerySet.as_manager()

    class Meta:
        get_latest_by = SEMVER_ORDER
        unique_together = SEMVER_ORDER

    @property
    def version(self):
        return f"{self.major_version}.{self.minor_version}.{self.patch_version}"

    def __str__(self):
        return self.version

    def __repr__(self):
        return f"<{self.__class__.__qualname__} {self.version} {self.uploaded_at}>"
