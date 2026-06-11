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

def best_deals(limit=10):
    conn = connection()
    cursor = conn.cursor()
    
    cursor.execute("""
        SELECT isbn, store, price
        FROM Prices
        ORDER BY price ASC
        LIMIT ?
    """, (limit,))
    
    results = cursor.fetchall()
    conn.close()
    return results

def price_history(isbn):
    conn = connection()
    cursor = conn.cursor()
    
    cursor.execute("""
        SELECT date, retailer, price
        FROM Prices
        WHERE isbn = ?
        ORDER BY date ASC
    """, (isbn,))
    
    results = cursor.fetchall()
    conn.close()
    return results