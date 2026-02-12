import os
import glob
from parse_xml import parse_xml
from connect_db import connect_db
from insert import insert

def main():

    data_folder = "data_normal"
    xml_files = glob.glob(os.path.join(data_folder, '*.xml'))

    conn = connect_db()

    for file_path in xml_files:
        filename = os.path.basename(file_path)
        data = parse_xml(file_path)

        success = insert(conn, data)

        if success:
            print("Data loaded!")
        else:
            print("System failed...")

    conn.close()

if __name__=="__main__":
    main()