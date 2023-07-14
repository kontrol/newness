import sqlite3

class DBHelper:
    def __init__(self, db_name):
        self.db_name = db_name
        # self.conn = sqlite3.connect(db_name)
        self.cursor = None

    def connect(self):
        self.conn = sqlite3.connect(self.db_name)

    def close(self):
        if self.conn:
            self.conn.close()
            self.conn = None

    def execute_query(self, query, params=None):
        self.connect()
        cursor = self.conn.cursor()
    
        try:
            if params:
                cursor.execute(query, params)
            else:
                cursor.execute(query)

            last_inserted_id = cursor.lastrowid
            results = cursor.fetchall()

            self.conn.commit()

        except Exception as e:
            print(e)
            results = None
            last_inserted_id = None

        # cursor.close()
        # self.close()

        return results, last_inserted_id
    
    def execute_many(self, query, params=None):
        self.connect()
        cursor = self.conn.cursor()
    
        if params:
            cursor.executemany(query, params)
        else:
            cursor.executemany(query)

        self.conn.commit()

        results = cursor.fetchall()

        self.close()

        return results
    
    # def get_all(self, table_name):
    #     query = f"SELECT * FROM {table_name}"
    #     return self.execute_query(query)
    
    def get_brand_list(self):
        query = f'SELECT name, brand_list_url FROM Company'
        results, _ = self.execute_query(query)

        if results:   
           company_brand_list_urls = {row[0]: row[1] for row in results}
           return company_brand_list_urls
        else:
            return None
        
    # def get_company_id(self, company_name):
    #     query = f'SELECT id FROM Company WHERE name = ?'
    #     params = (company_name,)
    #     results = self.execute_query(query, params)
    #     return results[0][0]
    
    def get_company_info(self, company_name):
        try:
            query = f'SELECT id, url, brand_list_url FROM Company WHERE name = ?'
            params = (company_name,)
            results, _ = self.execute_query(query, params) 
            if results:
                id, url, brand_list_url = results[0]
                return id, url, brand_list_url
        except IndexError:
            return None, None, None
            
    def get_company_brand_list_url(self, company_name):
        try:
            query = f'SELECT brand_list_url FROM Company WHERE name = ?'
            params = (company_name,)
            results, _ = self.execute_query(query, params)
            if results:
                return results[0][0]
        except IndexError:
            return None
    
    def get_brand_id_by_name(self, brand_name):
        try:
            query = f'SELECT id FROM Brand WHERE name = ?'
            params = (brand_name,)
            results, _ = self.execute_query(query, params)
            if results:
                return results[0][0]
        except IndexError:
            return None
    
    def insert_company(self, name, url, brand_list_url):
        query = f"INSERT INTO Company (name, url, brand_list_url) VALUES (?, ?, ?) RETURNING id"
        params = (name, url, brand_list_url)
        _, company_id = self.execute_query(query, params)
        # company_id = self.get_last_inserted_id()
        return company_id

    def insert_brand(self,brand_name):
        try:

            query = f"INSERT INTO Brand (name) VALUES (?) RETURNING id"
            params = (brand_name,)
            _, brand_id =self.execute_query(query, params)
            
            # brand_id = self.get_last_inserted_id()
            return brand_id
        except sqlite3.IntegrityError:
            return None
        
    def insert_company_brand(self, company_id, brand_id, company_brand_url):
        query = f"INSERT INTO CompanyBrand (company_id, brand_id, company_brand_url) VALUES (?, ?, ?)"
        params = (company_id, brand_id, company_brand_url)
        _, company_brand_id = self.execute_query(query, params)

        # brand_id = self.get_last_inserted_id()
        return company_brand_id
    
    def insert_company_product(self, company_id, product_id, price, product_url):
        query = f"INSERT INTO CompanyProduct (company_id, product_id, price, product_url) VALUES (?, ?, ?, ?)"
        params = (company_id, product_id, price, product_url)
        _, company_product_id = self.execute_query(query, params)

        return company_product_id
    
    def insert_image(self, image_url, prod_id):
        query = f"INSERT INTO Image (url, product_id) VALUES (?, ?)"
        params = (image_url, prod_id)
        _, image_id = self.execute_query(query, params)

        return image_id
    
    def insert_product_ingredient(self, product_id, ingredient_id):
        query = f"INSERT INTO ProductIngredient (product_id, ingredient_id) VALUES (?, ?)"
        params = (product_id, ingredient_id)
        _, product_ingredient_id = self.execute_query(query, params)

        return product_ingredient_id
    
    def insert_ingredient(self, ingredient_name):
        query = f"INSERT INTO Ingredient (name) VALUES (?)"
        params = (ingredient_name,)
        _, ingredient_id = self.execute_query(query, params)

        return ingredient_id
    
    def insert_product(self, brand_id, product_name):
        query = f"INSERT INTO Product (brand_id, name) VALUES (?, ?)"
        params = (brand_id, product_name)
        _, product_id = self.execute_query(query, params)

        return product_id
        
    def get_all_company_brand_url_random(self, company_id):
        query = f"SELECT company_brand_url FROM CompanyBrand WHERE company_id = ? ORDER BY RANDOM()"
        params = (company_id,)
        results, _ = self.execute_query(query, params)
        return results
    
    # def get_last_inserted_id(self):
    #     query = "SELECT last_insert_rowid()"
    #     result = self.execute_query(query)
    #     last_inserted_id = result[0][0]
    #     return last_inserted_id