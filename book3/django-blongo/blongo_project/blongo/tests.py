import pymongo


def get_collection(conn):

    databases = conn.database_names()

    if 'blongo' in databases:

        db = conn.blongo

        collections = db.collection_names()

        print "Collections"
        print "-----------"
        for collection in collections:
            print collection

        col = raw_input(
            '\nInput a collection name to show its field names: '
        )
        if col in collections:
            get_items(db[col].find())
        else:
            print "Sorry. The '{}' collection does not exist.".format(col)
    else:
        print "Sorry. The 'blongo' database does not exist."

    conn.close()


def get_items(collection_name):

    for items in collection_name:
        print items


if __name__ == '__main__':
    conn = pymongo.Connection('mongodb://localhost:27017')
    get_collection(conn)