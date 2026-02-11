from parse_xml import parse_xml
from connect_database import connect_database
from insert_data import insert_data

def main():
    
    xml_file_path = 'sample.xml'

    extracted_data = parse_xml(xml_file_path)
    conn = connect_database()
    success = insert_data(conn, extracted_data)
    if success:
        print('Data loaded!')
    else:
        print('System failed')
    
    conn.close()

if __name__=='__main__':
    main()