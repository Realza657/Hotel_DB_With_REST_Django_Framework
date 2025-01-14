ALLOWED_QUERIES = {
    "update_accommodation_account": """
        UPDATE hotel_accountaccommodation
        SET amount = (
            SELECT hotel_room.surcharges + hotel_roomtype.price
            FROM hotel_room
            INNER JOIN hotel_roomtype ON hotel_room.room_type_id = hotel_roomtype.id
            WHERE hotel_accountaccommodation.number_id = hotel_room.id
        )
        WHERE agreement_id = %s;
    """,

    "update_agreement_total": """
        UPDATE hotel_agreement
        SET total = (
            SELECT COALESCE(SUM(hotel_serviceaccount.amount), 0) + COALESCE(SUM(hotel_accountaccommodation.amount), 0)
            FROM hotel_serviceaccount
            LEFT JOIN hotel_accountaccommodation ON hotel_serviceaccount.agreement_id = hotel_accountaccommodation.agreement_id
            WHERE hotel_serviceaccount.agreement_id = hotel_agreement.id
        )
        WHERE id = %s;
    """,

    "add_service_account_amount": """
        UPDATE hotel_serviceaccount
        SET amount = amount + 100
        WHERE agreement_id = %s;
    """,

    "get_employees_with_high_awards": """
        SELECT hotel_employee.full_name, hotel_award.bonus
        FROM hotel_employee
        INNER JOIN hotel_award ON hotel_employee.id = hotel_award.employee_id
        WHERE hotel_award.bonus > 15000;
    """,

    "get_total_by_client": """
        SELECT SUM(total)
        FROM hotel_agreement
        WHERE client_id = %s;
    """,

    "get_employees_by_date_range": """
        SELECT hotel_employee.full_name, hotel_schedule.start_date, hotel_schedule.end_date
        FROM hotel_employee
        INNER JOIN hotel_schedule ON hotel_employee.id = hotel_schedule.employee_id
        WHERE hotel_schedule.start_date BETWEEN %s AND %s
           OR hotel_schedule.end_date BETWEEN %s AND %s;
    """,

    "count_rooms_below_price": """
        SELECT COUNT(*)
        FROM hotel_room
        INNER JOIN hotel_roomtype ON hotel_room.room_type_id = hotel_roomtype.id
        WHERE (hotel_room.surcharges + hotel_roomtype.price) < 15000;
    """,

    "get_most_frequent_client": """
        SELECT hotel_client.full_name, COUNT(hotel_agreement.id) AS num_agreements
        FROM hotel_client
        INNER JOIN hotel_agreement ON hotel_client.id = hotel_agreement.client_id
        GROUP BY hotel_client.id
        ORDER BY num_agreements DESC
        LIMIT 1;
    """,

    "get_fired_employees": """
        SELECT hotel_employee.full_name
        FROM hotel_employee
        INNER JOIN hotel_orderofemployment ON hotel_employee.id = hotel_orderofemployment.employee_id
        WHERE hotel_orderofemployment.date_fired IS NOT NULL;
    """,

    "update_needs_by_position": """
        UPDATE hotel_needsbyposition
        SET quantity = (
            SELECT hotel_position.staff - COUNT(hotel_orderofemployment.position_id)
            FROM hotel_position
            LEFT JOIN hotel_orderofemployment ON hotel_position.id = hotel_orderofemployment.position_id
            WHERE hotel_needsbyposition.position_id = hotel_position.id
        )
        WHERE position_id = %s;
    """,

    "get_current_guests": """
        SELECT hotel_client.full_name
        FROM hotel_client
        INNER JOIN hotel_agreement ON hotel_client.id = hotel_agreement.client_id
        WHERE CURRENT_DATE BETWEEN hotel_agreement.check_in_date AND hotel_agreement.check_out_date;
    """,

    "get_top_3_highest_paid_employees": """
        SELECT hotel_employee.full_name, hotel_position.salary
        FROM hotel_employee
        INNER JOIN hotel_orderofemployment ON hotel_employee.id = hotel_orderofemployment.employee_id
        INNER JOIN hotel_position ON hotel_orderofemployment.position_id = hotel_position.id
        WHERE hotel_orderofemployment.date_fired IS NULL
        ORDER BY hotel_position.salary DESC
        LIMIT 3;
    """
}
