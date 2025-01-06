from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

# Dữ liệu giả lập (sẽ được thay thế bằng cơ sở dữ liệu thực tế)
booking_data = []
pet_data = []
schedule_data = []
room_data = []  # Khai báo room_data

# Trang chủ
@app.route('/')
def index():
    return render_template('index.html')

# Quản lý thông tin booking
@app.route('/bookings', methods=['GET', 'POST'])
def bookings():
    if request.method == 'POST':
        pet_name = request.form['pet_name']
        owner_name = request.form['owner_name']
        booking_id = len(booking_data) + 1
        status = 'Active'  # Trạng thái mặc định là "Active"
        booking_data.append({'id': booking_id, 'pet_name': pet_name, 'owner_name': owner_name, 'status': status})
        return redirect(url_for('bookings'))  # Quay lại trang bookings sau khi thêm
    return render_template('bookings.html', bookings=booking_data)


# Quản lý thông tin chuồng
@app.route('/rooms', methods=['GET', 'POST'])
def rooms():
    if request.method == 'POST':
        # Thêm chuồng mới
        room_id = len(room_data) + 1
        room_name = request.form['room_name']
        room_type = request.form['room_type']
        capacity = request.form['capacity']
        room_data.append({'id': room_id, 'room_name': room_name, 'room_type': room_type, 'capacity': capacity})
        return redirect(url_for('rooms'))
    return render_template('rooms.html', rooms=room_data)

# Quản lý thông tin thú cưng
@app.route('/pets', methods=['GET', 'POST'])
def pets():
    if request.method == 'POST':
        # Thêm thông tin thú cưng mới
        pet_id = len(pet_data) + 1
        pet_name = request.form['pet_name']
        pet_type = request.form['pet_type']
        pet_data.append({'id': pet_id, 'pet_name': pet_name, 'pet_type': pet_type})
        return redirect(url_for('pets'))
    return render_template('pets.html', pets=pet_data)

# Quản lý lịch khám bác sĩ thú y
@app.route('/schedule', methods=['GET', 'POST'])
def schedule():
    if request.method == 'POST':
        # Thêm lịch khám cho bác sĩ
        schedule_id = len(schedule_data) + 1
        pet_name = request.form['pet_name']
        doctor_name = request.form['doctor_name']
        time_slot = request.form['time_slot']
        schedule_data.append({'id': schedule_id, 'pet_name': pet_name, 'doctor_name': doctor_name, 'time_slot': time_slot})
        return redirect(url_for('schedule'))
    return render_template('schedule.html', schedule=schedule_data)

if __name__ == '__main__':
    app.run(debug=True)
