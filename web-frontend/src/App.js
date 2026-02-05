import React, { useState } from "react";
import axios from "axios";
import { Pie } from "react-chartjs-2";
import { Chart as ChartJS, ArcElement, Tooltip, Legend } from "chart.js";

ChartJS.register(ArcElement, Tooltip, Legend);

function App() {
  const [file, setFile] = useState(null);
  const [summary, setSummary] = useState(null);

  const handleFileChange = (e) => {
    setFile(e.target.files[0]);
  };

  const uploadFile = async () => {
    if (!file) return;

    const formData = new FormData();
    formData.append("file", file);

    try {
      const response = await axios.post(
        "http://127.0.0.1:8000/api/upload/",
        formData
      );
      setSummary(response.data);
    } catch (err) {
      alert("Upload failed");
    }
  };

  return (
    <div style={{ padding: 20 }}>
      <h2>Chemical Equipment Visualizer</h2>

      <input type="file" onChange={handleFileChange} />
      <button onClick={uploadFile}>Upload CSV</button>

      {summary && (
        <div>
          <h3>Summary</h3>
          <p>Total Count: {summary.total_count}</p>
          <p>Avg Flowrate: {summary.avg_flowrate}</p>
          <p>Avg Pressure: {summary.avg_pressure}</p>
          <p>Avg Temperature: {summary.avg_temperature}</p>

          <div style={{ width: "400px", marginTop: "20px" }}>
            <Pie
              data={{
                labels: Object.keys(summary.type_distribution),
                datasets: [
                  {
                    data: Object.values(summary.type_distribution),
                    backgroundColor: [
                      "#FF6384",
                      "#36A2EB",
                      "#FFCE56",
                      "#4BC0C0",
                      "#9966FF",
                      "#FF9F40",
                    ],
                  },
                ],
              }}
            />
          </div>
        </div>
      )}
    </div>
  );
}

export default App;

