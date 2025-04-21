"""
Odometry zoom visualization tool
Manual time range selection for detailed inspection
"""

import csv
import matplotlib.pyplot as plt
from typing import List, Dict, Tuple  # 添加Tuple导入
from pathlib import Path

# 手动配置需要放大的时间范围 (根据第一次绘图观察后填写)
# ZOOM_RANGE = (1.74522e9+5000, 1.74522e9+5100)  # 示例值，根据实际需要修改
ZOOM_RANGE = (1745227009,1745227163)
def read_csv_data(file_path: str) -> List[Dict[str, float]]:
    """Read odometry data from CSV file"""
    data = []
    with open(file_path, 'r') as f:
        reader = csv.DictReader(f, fieldnames=['timestamp', 'v_l', 'v_r', 'o_l', 'o_r'])
        for row in reader:
            clean_row = {
                'timestamp': float(row['timestamp'].split(':')[1]),
                'v_l': float(row['v_l'].split(':')[1]),
                'v_r': float(row['v_r'].split(':')[1]),
                'o_l': float(row['o_l'].split(':')[1]),
                'o_r': float(row['o_r'].split(':')[1])
            }
            data.append(clean_row)
    return data

def filter_data(data: List[Dict[str, float]], zoom_range: Tuple[float, float]) -> List[Dict[str, float]]:
    """Filter data by time range"""
    return [d for d in data if zoom_range[0] <= d['timestamp'] <= zoom_range[1]]

def plot_zoomed_velocity(data: List[Dict[str, float]], zoom_range: Tuple[float, float]):
    """Plot zoomed velocity data"""
    filtered_data = filter_data(data, zoom_range)
    if not filtered_data:
        raise ValueError(f"No data in time range {zoom_range}")

    timestamps = [d['timestamp'] for d in filtered_data]
    plt.figure(figsize=(10, 5))
    plt.plot(timestamps, [d['v_l'] for d in filtered_data], label='Left Wheel Velocity (m/s)')
    plt.plot(timestamps, [d['v_r'] for d in filtered_data], label='Right Wheel Velocity (m/s)')
    
    plt.title(f'Wheel Velocities (Zoom: {zoom_range[0]:.2f}-{zoom_range[1]:.2f}s)')
    plt.xlabel('Timestamp (s)')
    plt.ylabel('Velocity (m/s)')
    plt.legend()
    plt.grid(True)
    plt.tight_layout()
    plt.savefig('./MotorAsst/output/velocity_plot_zoom.png')
    plt.close()

def plot_zoomed_odometry(data: List[Dict[str, float]], zoom_range: Tuple[float, float]):
    """Plot zoomed odometry data"""
    filtered_data = filter_data(data, zoom_range)
    if not filtered_data:
        raise ValueError(f"No data in time range {zoom_range}")

    timestamps = [d['timestamp'] for d in filtered_data]
    plt.figure(figsize=(10, 5))
    plt.plot(timestamps, [d['o_l'] for d in filtered_data], label='Left Wheel Distance (m)')
    plt.plot(timestamps, [d['o_r'] for d in filtered_data], label='Right Wheel Distance (m)')
    
    plt.title(f'Wheel Distance (Zoom: {zoom_range[0]:.2f}-{zoom_range[1]:.2f}s)')
    plt.xlabel('Timestamp (s)')
    plt.ylabel('Distance (m)')
    plt.legend()
    plt.grid(True)
    plt.tight_layout()
    plt.savefig('./MotorAsst/output/odometry_plot_zoom.png')
    plt.close()

def main():
    input_file = './MotorAsst/output/odom.csv'
    output_dir = './MotorAsst/output'
    
    if not Path(input_file).exists():
        print(f"Error: Input file {input_file} not found!")
        return

    Path(output_dir).mkdir(parents=True, exist_ok=True)

    try:
        data = read_csv_data(input_file)
        plot_zoomed_velocity(data, ZOOM_RANGE)
        plot_zoomed_odometry(data, ZOOM_RANGE)
        print(f"Zoomed plots saved to {output_dir}")
        print(f"Time range: {ZOOM_RANGE[0]:.2f}s to {ZOOM_RANGE[1]:.2f}s")
    except Exception as e:
        print(f"Error: {str(e)}")

if __name__ == "__main__":
    main()