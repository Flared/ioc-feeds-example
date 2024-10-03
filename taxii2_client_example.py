import datetime
import os

from taxii2client.v21 import Server
from taxii2client.v21 import as_pages


def main() -> None:
    server = Server(
        "https://api.flare.io/taxii2/",
        user="api-key",
        password=os.environ["FLARE_API_KEY"],
    )

    print(server.title)

    api_root = server.api_roots[0]

    start_date: datetime.datetime = datetime.datetime.now() - datetime.timedelta(
        hours=2
    )

    # Iterate through the available collections and print new items
    for collection in api_root.collections:
        print(collection.title)

        # No pagination request
        print(collection.get_objects(added_after=start_date))

        # Pagination request.
        for envelope in as_pages(
            collection.get_objects,
            per_request=50,
            added_after=start_date,
        ):
            print(envelope)


if __name__ == "__main__":
    main()
