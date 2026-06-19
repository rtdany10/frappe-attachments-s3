from frappe.core.doctype.file.file import File

S3_GENERATE_FILE_PREFIX = "/api/method/frappe_s3_attachment.controller.generate_file"


class CustomFile(File):
    @property
    def is_remote_file(self):
        if self.file_url and self.file_url.startswith(S3_GENERATE_FILE_PREFIX):
            return True

        return super().is_remote_file

    def get_full_path(self):
        """Return file path using the set file name."""
        file_path = self.file_url or self.file_name

        if file_path.startswith(S3_GENERATE_FILE_PREFIX):
            return file_path

        return super().get_full_path()

    def validate_file_on_disk(self):
        """Validates existence file"""
        full_path = self.get_full_path()

        if full_path.startswith(S3_GENERATE_FILE_PREFIX):
            return True

        return super().validate_file_on_disk()
