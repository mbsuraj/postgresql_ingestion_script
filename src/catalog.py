"""Provide a simple data catalog to act as
the single point of truth for the location of
data.

This catalog assumes the data lake is filesystem based.
In realistic situations, it does not have to be.

TODO: improve by making an abstraction of the
 type of the data (database, file: csv/parquet/…, …)
"""

from config import DATA


def _resource(zone, key):
    return str(DATA / zone / key)


catalog = {
    "to_ingest/event_finance_customer_order_line_items": _resource("to_ingest", "event_finance_customer_order_line_items.csv")
}
