import os
import json

import MySQLdb

mysql_config = json.loads(os.environ["MYSQL_CONFIG"])
mysql_connection = MySQLdb.connect(
    host=mysql_config["MYSQL_HOST"],
    user=mysql_config["MYSQL_USERNAME"],
    passwd=mysql_config["MYSQL_PASSWORD"],
    db=mysql_config["MYSQL_DATABASE"],
    ssl_mode="VERIFY_IDENTITY",
    ssl={"ca": os.environ.get("SSL_CERT_FILE", "/etc/ssl/certs/ca-certificates.crt")},
)
mysql_connection.autocommit(True)


def run(event, context):
    query = "INSERT INTO ping (my_uuid) VALUES (unhex(replace(uuid(), '-', '')))"
    mysql_connection.query(query)
