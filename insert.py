import traceback

def insert(conn, data):
    if conn is None or data is None:
        return False
    try:
        cursor = conn.cursor()

        insert_query = """
                        INSERT INTO contract(
                        contract_number,
                        customer_name,
                        customer_inn,
                        seller_name,
                        seller_inn,
                        ktru_code,
                        quantity,
                        price,
                        sum
                        )

                        VALUES(
                        %s, %s, %s, %s, %s, %s, %s, %s, %s
                        )
                        """
        data_tuple = (
            data['contract_number'],
            data['customer_name'],
            data['customer_inn'],
            data['seller_name'],
            data['seller_inn'],
            data['ktru_code'],
            data['quantity'],
            data['price'],
            data['sum']
        )

        cursor.execute(insert_query, data_tuple)

        conn.commit()

        print("Data inserted!")

        cursor.close()

        return True
    
    except Exception as e:
        print(f"Error inserting data: {e}")
        print(f"Error: type: {type(e).__name}")
        traceback.print_exc()
        return False