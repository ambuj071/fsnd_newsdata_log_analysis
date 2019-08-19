#!/usr/bin/env python3
import psycopg2

DBNAME = "news"


def get_results(query):
    try:
        db = psycopg2.connect(database=DBNAME)
    except Exception as e:
        print("Encountered following error in connecting to database: %s" % e)
        return
    c = db.cursor()
    c.execute(query)
    results = c.fetchall()
    db.close()
    return results


if __name__ == '__main__':
    query1 = "select slug as article, count (*) as views \
                from log join articles on substring(path,10,100) = slug\
                group by slug order by views desc limit 3;"
    query2 = "select name, count(*) from (select slug as article, author \
                from log join articles on substring(path,10,100) = slug) \
                as subq join authors on authors.id=subq.author \
                group by name order by count desc;"
    query3 = "select a.day, round((a.errors*100.0)/b.total_queries,2) as \
                error_percent from (select cast(time as date) \
                as day,count (*) as errors from log where status!='200 OK' \
                group by day) as a join (select cast(time as date) as day,\
                count (*) as total_queries from log group by day) as b \
                on a.day=b.day where (a.errors*100.0)/b.total_queries>1;"

    print("\n1. What are the most popular three articles of all time? ")
    for article, views in get_results(query1):
        print("{} with {} views".format(article, views))
    print("\n2.Who are the most popular article authors of all time?")
    for author, views in get_results(query2):
        print("{} with {} views".format(author, views))
    print("\n3. On which days did more than 1% of requests lead to errors?")
    for date, errors in get_results(query3):
        print("On {} there were {}% errors".format(date, errors))
