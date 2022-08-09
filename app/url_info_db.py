from app.db_conn import db


valid_malware_infos = {"MALWARE", "NOT_MALWARE"}

def get_url_info(url):
    cursor = db.cursor()
    query = "SELECT malware_info from mysql.url_infos where url = %s"
    cursor.execute(query, (url,))

    result = cursor.fetchone()

    if (not result):
        return None

    malware_info = result[0]
    print("Got malware_info : "+malware_info +" , for url : "+url)
    try:
        cursor.close()
    except:
        pass
    return malware_info

def update_url_info(url, malware_info):
    cursor = db.cursor()
    update_query = "UPDATE mysql.url_infos SET malware_info=%s WHERE url = %s ;"
    res = cursor.execute(update_query, (malware_info, url, ) )
    db.commit()
    cursor.close()
    return res

def insert_url_info(url, malware_info):
    if malware_info not in valid_malware_infos:
        raise Exception("Invalid value of malware_info found : "+malware_info+". Allowed Values  :"+valid_malware_infos)
    cursor = db.cursor()
    insert_query = "INSERT INTO mysql.url_infos (url, malware_info) VALUES (%s, %s)"
    try:
        cursor.execute(insert_query, (url, malware_info,))
    except _mysql_exceptions.IntegrityError as e:
        print("Entry for url : "+url+" already exists. Updating the same.")
        update_res = update_url_info(url, malware_info)
        print("Updated "+str(update_res)+" records")

    db.commit()
    try:
        cursor.close()
    except:
        pass
    return "SUCCESS"
