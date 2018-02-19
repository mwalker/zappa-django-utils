from django.contrib.gis.db.backends.spatialite.base import DatabaseWrapper

from zappa_django_utils.db.s3_database_backer import S3DatabaseBacker

class DatabaseWrapper(DatabaseWrapper, S3DatabaseBacker):
    """
    Wraps the normal Django Spatialite DB engine in an S3 backer!

    """

    def __init__(self, *args, **kwargs):
        super(DatabaseWrapper, self).__init__(*args, **kwargs)
        self.db_hash = None
        self.load_remote_db()

    def close(self, *args, **kwargs):
        super(DatabaseWrapper, self).close(*args, **kwargs)
        self.close_remote_db()
