import argparse
from .python_yaml_environment_variables import parse_config

# To run this:
# export DB_PASS=very_secret_and_complex
# python use_env_variables_in_config_example.py -c /path/to/yaml
# do stuff with conf, e.g. access the database password like this:
#   conf['database']['DB_PASS']

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="My awesome script")
    parser.add_argument(
        "-c", "--conf", action="store", dest="conf_file", help="Path to config file"
    )
    args = parser.parse_args()
    conf = parse_config(path=args.conf_file)
    print(conf)
