from db import connection

def get_prices_for_book(isbn):
    conn = connection()
    cursor = conn.cursor()

    cursor.execute("""
        SELECT *
        FROM Prices
        WHERE isbn = ?
        ORDER BY price ASC
    """, (isbn,))

    results = cursor.fetchall()
    conn.close()

    return results