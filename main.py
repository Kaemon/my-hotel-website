from flask import Flask, render_template, request, jsonify

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/cleansign')
def sign():
    return render_template('cleansign.html')

@app.route('/clean', methods = ['POST'])
def clean():
    roomid = request.form.get('roomid')
    return render_template('clean.html',roomid = roomid)

@app.route('/book_cleaning', methods=['POST'])
def book_cleaning():
    return render_template('bookclean.html')

@app.route('/availability')
def availability():
    return render_template('availability.html')

@app.route('/events')
def events():
    return render_template('event.html')

@app.route('/rooms')
def rooms():
    checkin = request.args.get('checkin')
    checkout = request.args.get('checkout')
    adults = request.args.get('adults')
    children = request.args.get('children')

    # Dummy data, replace with actual data retrieval from your database
    available_rooms = [
        {'type': 'Deluxe Room','details':'Non-smoke', 'price': 150, 'capacity': 2, 'images': ['static/room1_1.jpg','static/room1_2.jpg']},
        {'type': 'Common Room', 'details':'Non-smoke','price': 100, 'capacity': 2, 'images': ['static/room2_1.jpg','static/room2_2.jpg']},
        {'type': 'Deluxe Room', 'details':'Sea views','price': 200, 'capacity': 2, 'images': ['static/room3_1.jpg','static/room3_2.jpg']},
        {'type': 'Suite', 'details': 'Sea views, Non-Smoke', 'price': 500, 'capacity': 4,'images': ['static/room4_1.jpg', 'static/room4_2.jpg']},
        {'type': 'Suite', 'details': 'Non-Smoke', 'price': 400, 'capacity': 4,'images': ['static/room5_1.jpg', 'static/room5_2.jpg']},
        {'type': 'Deluxe Room', 'details': 'King-size bed', 'price': 300, 'capacity': 3,'images': ['static/room6_1.jpg', 'static/room6_2.jpg']},
        {'type': 'Common Room', 'details': 'Non-smoke', 'price': 100, 'capacity': 2,'images': ['static/room7_1.jpg', 'static/room7_2.jpg']},
        {'type': 'Common Room', 'details': 'Non-smoke', 'price': 170, 'capacity': 3,'images': ['static/room8_1.jpg', 'static/room8_2.jpg']},
        {'type': 'Suite', 'details': 'Best-views', 'price': 450, 'capacity': 4,'images': ['static/room9_1.jpg', 'static/room9_2.jpg']},
    ]

    # Filter rooms based on the number of adults (capacity)
    filtered_rooms = [room for room in available_rooms if room['capacity'] >= (int(adults)+int(children))]

    return render_template('rooms.html', checkin=checkin, checkout=checkout, adults=adults, children=children,rooms=filtered_rooms)
@app.route('/payment')
def pay():
    return render_template('payment.html')

@app.route('/success')
def succeed():
    return render_template('successpay.html')

@app.route('/direction', methods=['GET', 'POST'])
def directions():
    gif_map = {
        # dining
        "dining_area_to_wing-a": "static/dining_to_a.gif",
        "dining_area_to_wing-b": "static/dining_to_b.gif",
        "dining_area_to_wing-c": "static/dining_to_c.gif",
        "dining_area_to_wing-d": "static/dining_to_d.gif",
        "dining_area_to_table_tennis_court": "static/dining_to_tennis.gif",
        "dining_area_to_spa": "static/dining_to_spa.gif",
        "dining_area_to_sauna": "static/dining_to_sauna.gif",
        "dining_area_to_park": "static/dining_to_park.gif",
        "dining_area_to_jacuzzi": "static/dining_to_jacuzzi.gif",
        "dining_area_to_golf_course": "static/dining_to_golf.gif",
        "dining_area_to_swimming_pool": "static/dining_to_swim.gif",
        "dining_area_to_garden": "static/dining_to_garden.gif",
        # tennis
        "table_tennis_court_to_dining_area": "static/tennis_to_dining.gif",
        "table_tennis_court_to_wing-a": "static/tennis_to_a.gif",
        "table_tennis_court_to_wing-b": "static/tennis_to_b.gif",
        "table_tennis_court_to_wing-c": "static/tennis_to_c.gif",
        "table_tennis_court_to_wing-d": "static/tennis_to_d.gif",
        "table_tennis_court_to_spa": "static/tennis_to_spa.gif",
        "table_tennis_court_to_sauna": "static/tennis_to_sauna.gif",
        "table_tennis_court_to_park": "static/tennis_to_park.gif",
        "table_tennis_court_to_jacuzzi": "static/tennis_to_jacuzzi.gif",
        "table_tennis_court_to_golf_course": "static/tennis_to_golf.gif",
        "table_tennis_court_to_swimming_pool": "static/tennis_to_swim.gif",
        "table_tennis_court_to_garden": "static/tennis_to_garden.gif",
        # Wing-A
        "wing-a_to_dining_area": "static/a_to_dining.gif",
        "wing-a_to_table_tennis_court": "static/a_to_tennis.gif",
        "wing-a_to_wing-b": "static/a_to_b.gif",
        "wing-a_to_wing-c": "static/a_to_c.gif",
        "wing-a_to_wing-d": "static/a_to_d.gif",
        "wing-a_to_spa": "static/a_to_spa.gif",
        "wing-a_to_sauna": "static/a_to_sauna.gif",
        "wing-a_to_park": "static/a_to_park.gif",
        "wing-a_to_jacuzzi": "static/a_to_jacuzzi.gif",
        "wing-a_to_golf_course": "static/a_to_golf.gif",
        "wing-a_to_swimming_pool": "static/a_to_swim.gif",
        "wing-a_to_garden": "static/a_to_garden.gif",
        # Wing-B
        "wing-b_to_dining_area": "static/b_to_dining.gif",
        "wing-b_to_table_tennis_court": "static/b_to_tennis.gif",
        "wing-b_to_wing-a": "static/b_to_a.gif",
        "wing-b_to_wing-c": "static/b_to_c.gif",
        "wing-b_to_wing-d": "static/b_to_d.gif",
        "wing-b_to_spa": "static/b_to_spa.gif",
        "wing-b_to_sauna": "static/b_to_sauna.gif",
        "wing-b_to_park": "static/b_to_park.gif",
        "wing-b_to_jacuzzi": "static/b_to_jacuzzi.gif",
        "wing-b_to_golf_course": "static/b_to_golf.gif",
        "wing-b_to_swimming_pool": "static/b_to_swim.gif",
        "wing-b_to_garden": "static/b_to_garden.gif",
        # Wing-C
        "wing-c_to_dining_area": "static/c_to_dining.gif",
        "wing-c_to_table_tennis_court": "static/c_to_tennis.gif",
        "wing-c_to_wing-a": "static/c_to_a.gif",
        "wing-c_to_wing-b": "static/c_to_b.gif",
        "wing-c_to_wing-d": "static/c_to_d.gif",
        "wing-c_to_spa": "static/c_to_spa.gif",
        "wing-c_to_sauna": "static/c_to_sauna.gif",
        "wing-c_to_park": "static/c_to_park.gif",
        "wing-c_to_jacuzzi": "static/c_to_jacuzzi.gif",
        "wing-c_to_golf_course": "static/c_to_golf.gif",
        "wing-c_to_swimming_pool": "static/c_to_swim.gif",
        "wing-c_to_garden": "static/c_to_garden.gif",
        # Wing-D
        "wing-d_to_dining_area": "static/d_to_dining.gif",
        "wing-d_to_table_tennis_court": "static/d_to_tennis.gif",
        "wing-d_to_wing-a": "static/d_to_a.gif",
        "wing-d_to_wing-b": "static/d_to_b.gif",
        "wing-d_to_wing-c": "static/d_to_d.gif",
        "wing-d_to_spa": "static/d_to_spa.gif",
        "wing-d_to_sauna": "static/d_to_sauna.gif",
        "wing-d_to_park": "static/d_to_park.gif",
        "wing-d_to_jacuzzi": "static/d_to_jacuzzi.gif",
        "wing-d_to_golf_course": "static/d_to_golf.gif",
        "wing-d_to_swimming_pool": "static/d_to_swim.gif",
        "wing-d_to_garden": "static/d_to_garden.gif",
        # Spa
        "spa_to_dining_area": "static/spa_to_dining.gif",
        "spa_to_table_tennis_court": "static/spa_to_tennis.gif",
        "spa_to_wing-a": "static/spa_to_a.gif",
        "spa_to_wing-b": "static/spa_to_b.gif",
        "spa_to_wing-c": "static/spa_to_c.gif",
        "spa_to_wing-d": "static/spa_to_d.gif",
        "spa_to_sauna": "static/spa_to_sauna.gif",
        "spa_to_park": "static/spa_to_park.gif",
        "spa_to_jacuzzi": "static/spa_to_jacuzzi.gif",
        "spa_to_golf_course": "static/spa_to_golf.gif",
        "spa_to_swimming_pool": "static/spa_to_swim.gif",
        "spa_to_garden": "static/spa_to_garden.gif",
        # Sauna
        "sauna_to_dining_area": "static/sauna_to_dining.gif",
        "sauna_to_table_tennis_court": "static/sauna_to_tennis.gif",
        "sauna_to_wing-a": "static/sauna_to_a.gif",
        "sauna_to_wing-b": "static/sauna_to_b.gif",
        "sauna_to_wing-c": "static/sauna_to_c.gif",
        "sauna_to_wing-d": "static/sauna_to_d.gif",
        "sauna_to_spa": "static/sauna_to_spa.gif",
        "sauna_to_park": "static/sauna_to_park.gif",
        "sauna_to_jacuzzi": "static/sauna_to_jacuzzi.gif",
        "sauna_to_golf_course": "static/sauna_to_golf.gif",
        "sauna_to_swimming_pool": "static/sauna_to_swim.gif",
        "sauna_to_garden": "static/sauna_to_garden.gif",
        # Park
        "park_to_dining_area": "static/park_to_dining.gif",
        "park_to_table_tennis_court": "static/park_to_tennis.gif",
        "park_to_wing-a": "static/park_to_a.gif",
        "park_to_wing-b": "static/park_to_b.gif",
        "park_to_wing-c": "static/park_to_c.gif",
        "park_to_wing-d": "static/park_to_d.gif",
        "park_to_spa": "static/park_to_spa.gif",
        "park_to_sauna": "static/park_to_sauna.gif",
        "park_to_jacuzzi": "static/park_to_jacuzzi.gif",
        "park_to_golf_course": "static/park_to_golf.gif",
        "park_to_swimming_pool": "static/park_to_swim.gif",
        "park_to_garden": "static/park_to_garden.gif",
        # Jacuzzi
        "jacuzzi_to_dining_area": "static/jacuzzi_to_dining.gif",
        "jacuzzi_to_table_tennis_court": "static/jacuzzi_to_tennis.gif",
        "jacuzzi_to_wing-a": "static/jacuzzi_to_a.gif",
        "jacuzzi_to_wing-b": "static/jacuzzi_to_b.gif",
        "jacuzzi_to_wing-c": "static/jacuzzi_to_c.gif",
        "jacuzzi_to_wing-d": "static/jacuzzi_to_d.gif",
        "jacuzzi_to_spa": "static/jacuzzi_to_spa.gif",
        "jacuzzi_to_sauna": "static/jacuzzi_to_sauna.gif",
        "jacuzzi_to_park": "static/jacuzzi_to_park.gif",
        "jacuzzi_to_golf_course": "static/jacuzzi_to_golf.gif",
        "jacuzzi_to_swimming_pool": "static/jacuzzi_to_swim.gif",
        "jacuzzi_to_garden": "static/jacuzzi_to_garden.gif",
        # Golf
        "golf_course_to_dining_area": "static/golf_to_dining.gif",
        "golf_course_to_table_tennis_court": "static/golf_to_tennis.gif",
        "golf_course_to_wing-a": "static/golf_to_a.gif",
        "golf_course_to_wing-b": "static/golf_to_b.gif",
        "golf_course_to_wing-c": "static/golf_to_c.gif",
        "golf_course_to_wing-d": "static/golf_to_d.gif",
        "golf_course_to_sauna": "static/golf_to_sauna.gif",
        "golf_course_to_park": "static/golf_to_park.gif",
        "golf_course_to_jacuzzi": "static/golf_to_jacuzzi.gif",
        "golf_course_to_spa": "static/golf_to_spa.gif",
        "golf_course_to_swimming_pool": "static/golf_to_swim.gif",
        "golf_course_to_garden": "static/golf_to_garden.gif",
        # SwimmingPool
        "swimming_pool_to_dining_area": "static/swim_to_dining.gif",
        "swimming_pool_to_table_tennis_court": "static/swim_to_tennis.gif",
        "swimming_pool_to_wing-a": "static/swim_to_a.gif",
        "swimming_pool_to_wing-b": "static/swim_to_b.gif",
        "swimming_pool_to_wing-c": "static/swim_to_c.gif",
        "swimming_pool_to_wing-d": "static/swim_to_d.gif",
        "swimming_pool_to_sauna": "static/swim_to_sauna.gif",
        "swimming_pool_to_park": "static/swim_to_park.gif",
        "swimming_pool_to_jacuzzi": "static/swim_to_jacuzzi.gif",
        "swimming_pool_to_spa": "static/swim_to_spa.gif",
        "swimming_pool_to_golf_course": "static/swim_to_golf.gif",
        "swimming_pool_to_garden": "static/swim_to_garden.gif",
        # Garden
        "garden_to_dining_area": "static/garden_to_dining.gif",
        "garden_to_table_tennis_court": "static/garden_to_tennis.gif",
        "garden_to_wing-a": "static/garden_to_a.gif",
        "garden_to_wing-b": "static/garden_to_b.gif",
        "garden_to_wing-c": "static/garden_to_c.gif",
        "garden_to_wing-d": "static/garden_to_d.gif",
        "garden_to_sauna": "static/garden_to_sauna.gif",
        "garden_to_park": "static/garden_to_park.gif",
        "garden_to_jacuzzi": "static/garden_to_jacuzzi.gif",
        "garden_to_spa": "static/garden_to_spa.gif",
        "garden_to_golf_course": "static/garden_to_golf.gif",
        "garden_to_swimming_pool": "static/garden_to_swim.gif",
    }

    if request.method == 'POST':
        current_location = request.form.get('departure')
        destination = request.form.get('destination')

        if current_location and destination:
            key = f"{current_location}_to_{destination}"
            selected_gif = gif_map.get(key, "static/default.gif")
            return jsonify({"selected_gif": selected_gif})
        else:
            return jsonify({"error": "Please select both departure and destination."})

    return render_template('direction.html', gif_map=gif_map)

if __name__ == '__main__':
    app.run(debug=True, port=5002)
