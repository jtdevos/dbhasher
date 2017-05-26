import psycopg2
import xxhash
import logging
import pickle

logging.basicConfig(level=logging.DEBUG)

# CON_STRING = "dbname='ezproxytest' user='jtdevos' host='localhost' password='dbpass'"
CON_STRING = "dbname='ezproxytest' user='jtdevos' host='localhost'"



def sample():
    logging.info("this is a test")
    conn = psycopg2.connect(CON_STRING)
    cur = conn.cursor()
    cur.execute("select * from ezconfig_ezproxy_stanza ")
    rows = cur.fetchall()
    crc = xxhash.xxh64(seed=7)
    rownum = 0
    for row in rows:
        rownum += 1
        for col in row:
            crc.update(pickle.dumps(col))
        digest = crc.hexdigest()
        logging.debug("row: %s\t hash: %s", rownum, digest)
    conn.close()
    logging.debug("connection closed")










sample()
