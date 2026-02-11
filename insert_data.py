import traceback

def insert_data(conn, data):
    if conn is None or data is None:
        return False
    try:
        cursor = conn.cursor()

        insert_query = """
                        INSERT INTO contracts(
                        contract_number,
                        customer_inn
                        )
                        VALUES(%s, %s)
                        """
        data_tuple = (data['contract_number'],
                      data['customer_inn']
                      )

        cursor.execute(insert_query, data_tuple)

        conn.commit()

        print('Data inserted!')

        cursor.close()

        return True
    
    except Exception as e:
        print(f'Error inserting data: {e}')
        print(f'Error type: {type(e).__name__}')
        traceback.print_exc()
        return False