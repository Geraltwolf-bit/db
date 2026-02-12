import xml.etree.ElementTree as ET

def parse_xml(file_path):
    
    #create tree and root
    tree = ET.parse(file_path)
    root = tree.getroot()

    #create namespaces
    namespaces = {
        '': "http://zakupki.gov.ru/oos/CPtypes/1",
        "ns2": "http://zakupki.gov.ru/oos/common/1",
        "ns3": "http://zakupki.gov.ru/oos/base/1",
        "ns4": "http://zakupki.gov.ru/oos/types/1",
        "ns5": "http://zakupki.gov.ru/oos/EPtypes/1",
        "ns6": "http://zakupki.gov.ru/oos/printform/1"
    }

    #create data template
    data = {
        'contract_number': None,
        'customer_name': None,
        'customer_inn': None,
        'seller_name': None,
        'seller_inn': None,
        'ktru_code': None,
        'quantity': None,
        'price': None,
        'sum': None
    }

    try:

        #pull data from the xml file

        #pull contract_number from the root:
        contract_number = root.find('.//{http://zakupki.gov.ru/oos/CPtypes/1}contractNumber', namespaces)
        if contract_number is not None:
            data['contract_number'] = contract_number.text
            print(f'Found contract number: {data['contract_number']}')
        else:
            print("Could not find contract number")

        #Set up customerInfo
        customer_info = root.find('.//{http://zakupki.gov.ru/oos/CPtypes/1}customerInfo', namespaces)
        if customer_info is not None:

            #customer_name:
            customer_name = customer_info.find('.//ns2:shortName', namespaces)
            if customer_name is not None:
                data['customer_name'] = customer_name.text
                print(f"Found Customer_name: {data['customer_name']}")
            else:
                print("Could not find Customer name")

            #customer_inn:
            customer_inn = customer_info.find('.//ns2:INN', namespaces)
            if customer_inn is not None:
                data['customer_inn'] = customer_inn.text
                print(f"Found Customer_inn: {data['customer_inn']}")
            else:
                print("Could not find customer inn")

        #Set up participantInfo - which is seller info:
        seller_info = root.find('.//{http://zakupki.gov.ru/oos/CPtypes/1}participantInfo', namespaces)
        if seller_info is not None:

            #seller_name:
            seller_name = seller_info.find('.//shortName', namespaces)
            if seller_name is not None:
                data['seller_name'] = seller_name.text
                print(f"Found Seller name: {data['seller_name']}")
            else:
                print("Could not find Seller name")

            #seller_inn:
            seller_inn = seller_info.find('.//INN', namespaces)
            if seller_inn is not None:
                data['seller_inn'] = seller_inn.text
                print(f"Found seller_inn: {data['seller_inn']}")
            else:
                print("Could not find seller_inn")

        #Set up productsInfo:
        products_info = root.find('.//{http://zakupki.gov.ru/oos/CPtypes/1}productsInfo', namespaces)
        if products_info is not None:
            
            #ktru code:
            ktru_code = products_info.find('.//ns3:code', namespaces)
            if ktru_code is not None:
                data['ktru_code'] = ktru_code.text
                print(f"Found ktru_code: {data['ktru_code']}")
            else:
                print("Could not find ktru_code")

            #quantity:
            quantity = products_info.find('.//quantity', namespaces)
            if quantity is not None:
                data['quantity'] = int(quantity.text)
                print(f"Found quantity: {data['quantity']}")
            else:
                print("Could not find quantity")

            #price:
            price = products_info.find('.//price', namespaces)
            if price is not None:
                data['price'] = float(price.text)
                print(f"Found price: {data['price']}")
            else:
                print("Could not find price")

            #sum:
            sum = products_info.find('.//sum', namespaces)
            if sum is not None:
                data['sum'] = float(sum.text)
                print(f"Found sum: {data['sum']}")
            else:
                print("Could not find sum")
    
        return data


    except Exception as e:
        print(f"Error parsign xml: {e}")
        return None