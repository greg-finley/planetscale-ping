import os

import MySQLdb

mysql_connection = MySQLdb.connect(
    host=os.getenv("MYSQL_HOST"),
    user=os.getenv("MYSQL_USERNAME"),
    passwd=os.getenv("MYSQL_PASSWORD"),
    db=os.getenv("MYSQL_DATABASE"),
    ssl_mode="VERIFY_IDENTITY",
    ssl={"ca": os.environ.get("SSL_CERT_FILE", "/etc/ssl/certs/ca-certificates.crt")},
)
mysql_connection.autocommit(True)


def run(event, context):
    query = "INSERT INTO ping (my_uuid) VALUES (unhex(replace(uuid(), '-', '')))"
    mysql_connection.query(query)
