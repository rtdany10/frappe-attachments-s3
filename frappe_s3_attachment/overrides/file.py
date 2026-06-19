from frappe.core.doctype.file.file import File

S3_GENERATE_FILE_PREFIX = "/api/method/frappe_s3_attachment.controller.generate_file"


class CustomFile(File):
    def validate_file_on_disk(self):
        """Validates existence file"""
        full_path = self.get_full_path()

        if full_path.startswith(S3_GENERATE_FILE_PREFIX):
            return True

        return super().validate_file_on_disk()
