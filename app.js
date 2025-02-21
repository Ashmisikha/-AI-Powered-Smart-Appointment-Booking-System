import React, { useEffect, useState } from "react";
import axios from "axios";

const App = () => {
    const [appointments, setAppointments] = useState([]);
    const [user, setUser] = useState("");

    useEffect(() => {
        axios.get("http://localhost:5000/appointments")
            .then(res => setAppointments(res.data))
            .catch(err => console.log(err));
    }, []);

    const bookAppointment = () => {
        axios.post("http://localhost:5000/book", { user_name: user })
            .then(res => alert(`✅ Appointment booked for ${res.data.slot}`))
            .catch(err => console.log(err));
    };

    return (
        <div>
            <h1>📅 Smart Appointment System</h1>
            <input type="text" placeholder="Enter Name" onChange={e => setUser(e.target.value)} />
            <button onClick={bookAppointment}>Book Appointment</button>

            <h2>📜 Appointments</h2>
            <ul>
                {appointments.map(app => (
                    <li key={app.id}>
                        {app.user} - {app.slot} - {app.status}
                    </li>
                ))}
            </ul>
        </div>
    );
}

export default App;
