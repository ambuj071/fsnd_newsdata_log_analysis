#!/usr/bin/env python3
import psycopg2

DBNAME = "news"


def get_results(query):
    db = psycopg2.connect(database=DBNAME)
    c = db.cursor()
    c.execute(query)
    results = c.fetchall()
    db.close()
    return results

if __name__ == '__main__':
    query1 = "select substring(path,10,100) as article, count (*) as views \
                from log where path like '/article/%' group by path order\
                by views desc limit 3;"
    query2 = "select name, count(*) from (select substring(path,10,100) as article, author \
                from log join articles on substring(path,10,100) = slug) \
                as subq join authors on authors.id=subq.author \
                group by name order by count desc;"
    query3 = "select a.day, cast(a.errors*100 as real)/cast(b.total_queries \
                as real) as error_percent from (select cast(time as date) \
                as day,count (*) as errors from log where status!='200 OK' \
                group by day) as a join (select cast(time as date) as day,\
                count (*) as total_queries from log group by day) as b \
                on a.day=b.day where cast(a.errors*100 as real)/cast\
                (b.total_queries as real)>1;"

    print("\n1. What are the most popular three articles of all time? ")
    for record in get_results(query1):
        print(str(record[0])+" with "+str(record[1])+" views")
    print("\n2.Who are the most popular article authors of all time?")
    for record in get_results(query2):
        print(str(record[0])+" with "+str(record[1])+" views")
    print("\n3. On which days did more than 1% of requests lead to errors?")
    for record in get_results(query3):
        print("On "+str(record[0]) +
              " there were "+str(round(record[1], 2))+"% errors")
