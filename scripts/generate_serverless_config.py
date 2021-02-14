import csv
from jinja2 import Template
import os 

SIZES = [
  128,
  3008,
  3009,
  5307,
  5308,
  7076,
  7077,
  8845,
  8846,
  10240
]

if __name__ == "__main__":
  dir_path = os.path.dirname(os.path.realpath(__file__))
  with open(os.path.join(dir_path, "serverless.yml.j2")) as raw_file:
    template = Template(raw_file.read())

  with open("serverless.yml", "w") as sls_file:
    sls_file.write(template.render(sizes=SIZES))