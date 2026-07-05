class BookingDAO:
    def __init__(self, cursor):
        self.cursor = cursor

    def get_booking_by_id(self, booking_id: int) -> dict | None:
        self.cursor.execute("SELECT * FROM bookings WHERE BOOKINGID = ?", (booking_id,))
        row = self.cursor.fetchone()
        if row is None:
            return None
        else:
            return {
                "BOOKINGID": row[0],
                "ROOMID": row[1],
                "FIRSTNAME": row[2],
                "LASTNAME": row[3],
                "DEPOSITPAID": row[4],
                "CHECKIN": row[5],
                "CHECKOUT": row[6]
            }