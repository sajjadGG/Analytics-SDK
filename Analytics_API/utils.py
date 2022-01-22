def parse_config(path="config.yaml"):
    import ruamel.yaml

    yaml = ruamel.yaml.YAML()
    with open(file_name) as fp:
        data = yaml.load(fp)
    return data
