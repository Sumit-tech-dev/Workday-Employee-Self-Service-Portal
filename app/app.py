
from flask import Flask, render_template, request, redirect, url_for, flash

app = Flask(__name__)

# Demo secret key. Production mein secure secret use karna.
app.secret_key = "local-demo-key"

# Employee demo data
employee = {
    "name": "Alex Johnson",
    "employee_id": "EMP1001",
    "department": "Cloud Infrastructure",
    "role": "Cloud Engineer",
    "email": "alex.johnson@example.com",
    "location": "Noida"
}

# Demo leave records
leave_requests = [
    {
        "type": "Casual Leave",
        "from": "2026-11-12",
        "to": "2026-11-13",
        "status": "Pending"
    },
    {
        "type": "Sick Leave",
        "from": "2026-10-20",
        "to": "2026-10-20",
        "status": "Approved"
    }
]

# Demo service requests
requests_data = [
    {
        "title": "Laptop access request",
        "date": "2026-11-01",
        "status": "In Progress"
    },
    {
        "title": "VPN access",
        "date": "2026-10-25",
        "status": "Completed"
    }
]


# Dashboard
@app.route("/")
def home():
    return render_template("index.html", employee=employee)


# Employee profile
@app.route("/profile")
def profile():
    return render_template("profile.html", employee=employee)


# Attendance
@app.route("/attendance")
def attendance():

    attendance_data = [
        {
            "date": "2026-11-06",
            "check_in": "09:15 AM",
            "check_out": "06:10 PM",
            "status": "Present"
        },
        {
            "date": "2026-11-05",
            "check_in": "09:05 AM",
            "check_out": "06:00 PM",
            "status": "Present"
        },
        {
            "date": "2026-11-04",
            "check_in": "--",
            "check_out": "--",
            "status": "Leave"
        }
    ]

    return render_template(
        "attendance.html",
        attendance_data=attendance_data
    )


# Leave management
@app.route("/leave", methods=["GET", "POST"])
def leave():

    if request.method == "POST":

        leave_type = request.form.get("leave_type", "").strip()
        from_date = request.form.get("from_date", "").strip()
        to_date = request.form.get("to_date", "").strip()
        reason = request.form.get("reason", "").strip()

        if not all([leave_type, from_date, to_date, reason]):
            flash("Please complete all fields.", "error")

        elif to_date < from_date:
            flash("End date cannot be earlier than start date.", "error")

        else:
            leave_requests.insert(0, {
                "type": leave_type,
                "from": from_date,
                "to": to_date,
                "status": "Pending"
            })

            flash("Leave request submitted successfully.", "success")

            return redirect(url_for("leave"))

    return render_template(
        "leave.html",
        leave_requests=leave_requests
    )


# My service requests
@app.route("/requests")
def my_requests():
    return render_template(
        "requests.html",
        requests_data=requests_data
    )


# Start Flask server
if __name__ == "__main__":
    app.run(host="127.0.0.1", port=5000, debug=True)

