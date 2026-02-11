import xml.etree.ElementTree as ET

def parse_xml(file_path):
    namespaces = {
        '': 'http://zakupki.gov.ru/oos/CPtypes/1',  # Default namespace
        'ns2': 'http://zakupki.gov.ru/oos/common/1',
        'ns3': 'http://zakupki.gov.ru/oos/base/1',
        'ns4': 'http://zakupki.gov.ru/oos/types/1',
        'ns5': 'http://zakupki.gov.ru/oos/EPtypes/1',
        'ns6': 'http://zakupki.gov.ru/oos/printform/1'
    }

    tree = ET.parse(file_path)
    root = tree.getroot()

    data = {
        'customer_inn': None,
        'contract_number': None
        }
    
    try:
        customer_info = root.find('.//{http://zakupki.gov.ru/oos/CPtypes/1}customerInfo')
        if customer_info is not None:
            print('Found customerInfo element')

            contract_number = root.find('.//{http://zakupki.gov.ru/oos/CPtypes/1}contractNumber', namespaces)
            if contract_number is not None:
                data['contract_number'] = contract_number.text
                print(f'found Contract Number: {data['contract_number']}')
            else:
                print('Could not find Contract Number')

            customer_inn = customer_info.find('.//ns2:INN', namespaces)
            if customer_inn is not None:
                data['customer_inn'] = customer_inn.text
                print(f"found INN: {data['customer_inn']}")
            else:
                print('Could not find ns2:INN')
        
        return data
    
    except Exception as e:
        print(f'Error parsing xml: {e}')
        return None