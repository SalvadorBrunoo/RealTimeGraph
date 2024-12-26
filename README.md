# Live Plotting with Python and TwinCAT

This project is a real-time data visualization application that integrates Python with a TwinCAT PLC to display live data in a graphical interface using pyads, PyQt and PyQtGraph.

---

## Features
- Real-time plotting of data streamed from a TwinCAT PLC.
- User-friendly graphical interface built with PyQt5.
- Customizable live plot with PyQtGraph.
- Seamless integration with TwinCAT using PyADS.

---

## Prerequisites
1. **Python Environment**:  
   Install the following Python packages:
   ```bash
   pip install numpy pyads pyqt5 pyqtgraph
   ```
2. **TwinCAT Setup**:
   - Ensure TwinCAT is running on your system.
   - Configure the ADS route between your Python environment and the PLC.
   - Adjust the PLC address (`192.168.71.1.1.1`) in the script to match your setup.

---

## Project Files
- **Python Code** (`app.py`):  
  Handles the real-time graphing logic and communication with the PLC.
- **TwinCAT Code** (`MAIN.TcPOU`):  
  Gets real-time analog data for the Python application.

---

## How It Works
1. **PLC Program**:
   - Generates a buffer (`Buffer_y`) of real-time data values.
   - Updates the buffer continuously in a cyclic task.
   - Provides the buffer size to the Python application.

2. **Python Application**:
   - Reads the buffer and size values from the PLC using PyADS.
   - Updates the plot at 30ms intervals using a QTimer.
   - Visualizes the data dynamically on a graph.

---

## Customization
  The Python script uses an `update` function (from `modify.py`) to preprocess data. Customize it as needed for filtering, scaling, or transformations.

---

## Troubleshooting
- **Connection Issues**:  
  Ensure the PLC is reachable and the ADS route is properly configured.
- **Missing Libraries**:  
  Install any missing Python packages using `pip`.

---

## Future Enhancements
- Add user controls for plot customization.
- Include error handling for ADS communication failures.
- Extend the plotting capabilities to display multiple data streams.

---

Feel free to contribute or suggest improvements! 😊
