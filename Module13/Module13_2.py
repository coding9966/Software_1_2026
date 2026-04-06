from flask import Flask, jsonify
import mysql.connector

app = Flask(__name__)

# Database connection function
def get_connection():
    return mysql.connector.connect(
        host="127.0.0.1",
        port=3306,
        database="flight_game",
        user="root",
        password="1234", 
        autocommit=True
    )

@app.route('/airport/<icao>', methods=['GET'])
def get_airport(icao):
    connection = get_connection()
    cursor = connection.cursor(dictionary=True)

    sql = """
        SELECT ident, name, municipality
        FROM airport
        WHERE ident = %s
    """

    cursor.execute(sql, (icao,))
    result = cursor.fetchone()

    cursor.close()
    connection.close()

    if result:
        response = {
            "ICAO": result["ident"],
            "Name": result["name"],
            "Location": result["municipality"]
        }
        return jsonify(response)
    else:
        return jsonify({"error": "Airport not found"}), 404


if __name__ == '__main__':
    app.run(debug=True)