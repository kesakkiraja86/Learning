import pandas as pd
from databricks import sql
from databricks.sdk.core import Config

WAREHOUSE_HTTP_PATH = "/sql/1.0/warehouses/5400928200e01a56"


def get_data():
    cfg = Config()
    server_hostname = cfg.host
    if server_hostname.startswith("https://"):
        server_hostname = server_hostname.replace("https://", "")
    elif server_hostname.startswith("http://"):
        server_hostname = server_hostname.replace("http://", "")

    with sql.connect(
        server_hostname=server_hostname,
        http_path=WAREHOUSE_HTTP_PATH,
        credentials_provider=lambda: cfg.authenticate,
    ) as conn:
        with conn.cursor() as cursor:
            cursor.execute("""
                SELECT product,
                       SUM(amount) sales
                FROM demo_cat.demo_schema.sales_demo
                GROUP BY product
            """)
            return cursor.fetchall_arrow().to_pandas()