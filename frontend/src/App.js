import React, { useEffect, useState } from 'react';
import axios from 'axios';

function App() {
  const [alerts, setAlerts] = useState([]);

  useEffect(() => {
    const fetchAlerts = async () => {
      const response = await axios.get('http://localhost:8000/api/alerts/');
      setAlerts(response.data);
    };
    fetchAlerts();
  }, []);

  return (
    <div>
      <h1>Threat Alerts</h1>
      <ul>
        {alerts.map((alert, index) => (
          <li key={index}>{alert.alert}</li>
        ))}
      </ul>
    </div>
  );
}

export default App;