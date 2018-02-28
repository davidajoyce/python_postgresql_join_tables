import psycopg2



def create_tables():
    """ create tables in the PostgreSQL database"""
    commands = (
        """
        CREATE TABLE higher_than_comp (
            product_id SERIAL PRIMARY KEY,
            store_id VARCHAR(255) ,
	    store_code VARCHAR(255),
	    description VARCHAR(255) ,
	    barcode VARCHAR(255),
	    retail_price DECIMAL,
	    sold_price DECIMAL,
	    last_sold VARCHAR(255),
	    avg_weekly DECIMAL,
	    competitor VARCHAR(255),
	    price_check VARCHAR(255),
	    competitor_price DECIMAL,
	    diff DECIMAL,
	    diff_perc DECIMAL,
	    match_cost_pw DECIMAL,
	    offer VARCHAR(255),
	    details VARCHAR(255)
	         		
        )
        """,
        
       )
    conn = None
    try:
        
        # connect to the PostgreSQL server   
	conn = psycopg2.connect(host="localhost",database="JoycesData", user="postgres", password="postgres")
        cur = conn.cursor()
        # create table one by one
        for command in commands:
            cur.execute(command)
        # close communication with the PostgreSQL database server
        cur.close()
        # commit the changes
        conn.commit()
    except (Exception, psycopg2.DatabaseError) as error:
        print(error)
    finally:
        if conn is not None:
            conn.close()

def insert_news_list(news_list):
    """ insert multiple newsapi info from newsapi response  """
    sql = "INSERT INTO higher_than_comp(store_id, store_code, description, barcode, retail_price, sold_price, last_sold, avg_weekly, competitor, price_check, competitor_price, diff, diff_perc, match_cost_pw, offer, details) VALUES(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)"
    conn = None
    try:
      
        # connect to the PostgreSQL database
        conn = psycopg2.connect(host="localhost",database="JoycesData", user="postgres", password="postgres")
        # create a new cursor
        cur = conn.cursor()
        # execute the INSERT statement
        cur.executemany(sql,news_list)
        # commit the changes to the database
        conn.commit()
        # close communication with the database
        cur.close()
    except (Exception, psycopg2.DatabaseError) as error:
        print(error)
    finally:
        if conn is not None:
            conn.close()
 
if __name__ == '__main__':
    	
	create_tables()

	
