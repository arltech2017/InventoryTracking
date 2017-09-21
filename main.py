def save_catalog(catalog, fname):
    """Write catalog to json encoded fname file."""
    f = open(fname, 'w')
    catalog = [item.__dict__ for item in catalog]
    f.write(json.dumps(catalog))
    f.close()

