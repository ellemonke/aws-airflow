from airflow.contrib.hooks.aws_hook import AwsHook
from airflow.hooks.postgres_hook import PostgresHook
from airflow.models import BaseOperator
from airflow.utils.decorators import apply_defaults

class StageToRedshiftOperator(BaseOperator):
    ui_color = '#358140'
    template_fields = ("s3_key",)
    copy_sql = """
        COPY {}
        FROM '{}'
        ACCESS_KEY_ID '{}'
        SECRET_ACCESS_KEY '{}'
        IGNOREHEADER {}
        DELIMITER '{}'
    """

    @apply_defaults
    def __init__(self,
                 redshift_conn_id="",
                 aws_credentials_id="",
                 table="",
                 s3_bucket="",
                 s3_key="",
                 delimiter=",",
                 ignore_headers=1,
                 *args, **kwargs):

        super(StageToRedshiftOperator, self).__init__(*args, **kwargs)
        self.table = table
        self.redshift_conn_id = redshift_conn_id
        self.s3_bucket = s3_bucket
        self.s3_key = s3_key
        self.delimiter = delimiter
        self.ignore_headers = ignore_headers
        self.aws_credentials_id = aws_credentials_id

    def execute(self, context):
        aws_hook = AwsHook(self.aws_credentials_id)
        credentials = aws_hook.get_credentials()
        self.log.info("AWS S3 connection successful")
        redshift = PostgresHook(postgres_conn_id=self.redshift_conn_id)
        self.log.info("Redshift connection successful")
        self.log.info(self.s3_bucket)
        self.log.info(self.s3_key)

        self.log.info("Clearing data from destination Redshift table")
        redshift.run("DROP TABLE IF EXISTS {}".format(self.table))
        self.log.info("Data cleared")

#         self.log.info("Copying data from S3 to Redshift")
#         rendered_key = self.s3_key.format(**context)
#         s3_path = "s3://{}/{}".format(self.s3_bucket, rendered_key)
#         formatted_sql = S3ToRedshiftOperator.copy_sql.format(
#             self.table,
#             s3_path,
#             credentials.access_key,
#             credentials.secret_key,
#             self.ignore_headers,
#             self.delimiter
#         )
#         redshift.run(formatted_sql)
#         self.log.info("Data copied")

