
from project.file_writers.default_writer import DefaultWriter
import sys
print(DefaultWriter(url=sys.argv[1]).write_file())
