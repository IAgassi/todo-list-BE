TNS = ""
MAX_RETRIES = 3
GET_QUERY = """SELECT * FROM TODO;"""
INSERT_QUERY ="""INSERT INTO TODO (ID, TASK) VALUES ({0}, {1});"""
DELETE_QUERY = """DELETE FROM TODO WHERE ID = {0};"""