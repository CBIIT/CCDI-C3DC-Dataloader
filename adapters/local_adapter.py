#!/usr/bin/env python3
import os

from bento.common.utils import get_logger, get_md5


class BentoLocal:
    """
    This adapter assumes all data files are in same folder as the pre-manifest
    Following methods are required:
        - filter_fields
        - get_fields
        - load_file_info
        - clear_file_info
        - get_org_url
        - get_file_name
        - get_org_md5
    """

    def __init__(self, working_dir, name_field='file_name', md5_field='md5sum', size_field=None, verify=True):
        """

        :param working_dir: location of pre-manifest and files
        :param name_field: field name used to store file name
        :param md5_field: field name used to store original MD5
        :param size_field: field name used to store original file size
        :param verify: whether or not to verify MD5 and size
        """
        self.log = get_logger('Local_adapter')
        if not os.path.isdir(working_dir):
            raise ValueError(f'"{working_dir}" is not a directory!')
        self.working_dir = working_dir
        self.name_field = name_field
        self.md5_field = md5_field
        self.cleanup_fields = [name_field, md5_field]
        self.size_field = size_field
        if size_field is not None:
            self.cleanup_fields.append(size_field)
        self.verify = verify

    def _assert_file_info(self):
        if not hasattr(self, 'file_info') or not self.file_info:
            raise Exception('file_info is empty, call load_file_info() method first!')

    def load_file_info(self, file_info):
        """
        Load new file information
        :param file_info:
        :return: None
        """
        self.file_info = file_info

    def clear_file_info(self):
        """
        Clear last file information loaded
        :return: None
        """
        self.file_info = {}

    def get_org_url(self):
        """
        Get file's URL in original location
        :return: URL: str, will be in file:// scheme if it's local file
        """
        self._assert_file_info()
        return f'file://{self._get_local_path()}'

    def _get_local_path(self):
        return f'{self.working_dir}/{self.get_file_name()}'

    def get_org_md5(self):
        """
        Get file's original MD5,
        If original file's MD5 is given in column named in self.md5_field, then it will be used to verify file content
        If original file's size is given in column named in self.size_field, then file size will be verified also
        :return: MD5: str, None if not available in self.file_info
        """
        self._assert_file_info()
        org_md5 = self.file_info.get(self.md5_field)
        if not org_md5 or self.verify:
            real_md5 = get_md5(self._get_local_path())

            if not org_md5:
                return real_md5
            else:
                if org_md5 != real_md5:
                    self.log.error(f'File content does NOT match given MD5: {self.get_file_name()}!')
                    raise ValueError(f'MD5 verification failed!')
        if not self._check_file_size():
            self.log.error(f'File size does NOT match given size: {self.get_file_name()}!')
            raise ValueError(f'File size verification failed!')

        return org_md5

    def _check_file_size(self):
        """
        Verify local file size
        :return: bool
        """
        if self.size_field and self.verify:
            org_size = int(self.file_info.get(self.size_field))
            real_size = os.path.getsize(self._get_local_path())
            return org_size == real_size
        else:
            return True

    def get_file_name(self):
        """
        Get file name, without any path
        :return: file name: str
        """
        self._assert_file_info()
        file_name = self.file_info.get(self.name_field)
        if file_name is None:
            raise ValueError(f'Can NOT find file name in {self.name_field} field')
        return file_name

    def get_fields(self):
        """
        Get available fields exclude the ones in self.cleanup_fields in self.file_info
        :return:
        """
        obj = {}
        for key, val in self.file_info.items():
            if key in self.cleanup_fields:
                continue
            else:
                obj[key] = val

        return obj

    def filter_fields(self, fields):
        """
        Remove all fields that's in self.cleanup_fields from input field list
        :param fields: list
        :return: field list with unwanted fields removed
        """
        return list(filter(lambda f: f not in self.cleanup_fields, fields))


