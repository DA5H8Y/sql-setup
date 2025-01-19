import os
import math
import pandas as pd
import numpy as np

for file in os.listdir("."):
    f = file.split(".")
    fName = ".".join(f[0:-1])
    ext   = f[-1]

    if ext in ("xlsx", "xls"):
        xl = pd.ExcelFile(file)

        if xl:
            # Create schema file
            with open(fName + "_scheme.sql", "w") as sql_file:
            
                sql_file.write("CREATE DATABASE " + fName + ";\n")

                tbls = xl.sheet_names

                for tbl in tbls:
                    df = xl.parse(tbl)
                    fields = df.columns
                    sql_file.write("CREATE TABLE " + tbl + " (\n")

                    for i, field in enumerate(fields):
                        parts = field.split(":")
                        if i > 0:
                            sql_file.write(",\n")
                        sql_file.write("    " + parts[0] + " " + parts[1])

                    sql_file.write("\n);\n")

            print("Created: " + fName + "_scheme.sql")

            # Create base data file
            with open(fName + "_base.sql", "w") as sql_file:
                tbls = xl.sheet_names

                for tbl in tbls:
                    df = xl.parse(tbl)
                    fields = df.columns
                    for row in df.values:
                        sql_file.write("INSERT INTO " + tbl + " (")

                        for i, field in enumerate(fields):
                            parts = field.split(":")
                            if i > 0:
                                sql_file.write(", ")
                            sql_file.write(parts[0])

                        sql_file.write( ") VALUES (")

                        for i, col in enumerate(row):
                            if i > 0:
                                sql_file.write(", ")

                            if isinstance(col, (int, float)):
                                if math.isnan(col):
                                    sql_file.write("NULL")
                                else:
                                    sql_file.write( str(col))
                            elif isinstance(col, str):
                                sql_file.write( "'" + col + "'" )
                            elif isinstance(col, pd.Timestamp):
                                sql_file.write( "'" + col._repr_base + "'" )
                            else:
                                if pd.isnull(col):
                                    sql_file.write("NULL")
                                else:
                                    print(type(col))

                        sql_file.write(");\n")

            print("Created: " + fName + "_base.sql")
