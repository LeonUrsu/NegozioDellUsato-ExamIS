import os
import pathlib
from Database.PathDatabase import PathDatabase
print('----------')
to_path = pathlib.Path().resolve()
PathDatabase().setup("ciao")

