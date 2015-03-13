# -*- coding: utf-8 -*-

""" ZIP archive extractor via executable."""

from mcomix import process
from mcomix.archive import archive_base

# Filled on-demand by ZipExecArchive
_zip_executable = -1

class ZipExecArchive(archive_base.ExternalExecutableArchive):
    """ ZIP file extractor using unzip executable. """

    def _get_executable(self):
        return ZipExecArchive._find_unzip_executable()

    def _get_list_arguments(self):
        return [u'-Z1']

    def _get_extract_arguments(self):
        return [u'-p']

    @staticmethod
    def _find_unzip_executable():
        """ Tries to run unzip, and returns 'unzip' on success.
        Returns None on failure. """
        global _zip_executable
        if -1 == _zip_executable:
            _zip_executable = process.find_executable((u'unzip',))
        return _zip_executable

    @staticmethod
    def is_available():
        return bool(ZipExecArchive._find_unzip_executable())

# vim: expandtab:sw=4:ts=4
