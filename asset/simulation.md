# 🖥️ Simulation Environment

This simulation environment is developed and tested with the following configuration:

- 🐧 **OS**: Ubuntu 22.04
- 🐢 **ROS2**: Humble
- 🌐 **Isaac Sim**: 4.5
- 🧪 **Isaac Lab**: 2.1.0
- 🖥️ **Tested GPU**: NVIDIA GeForce RTX 3060

Compatibility note: Isaac Sim 4.5 may fail to launch or show runtime issues on some RTX 50 series GPUs. If this happens, please try Isaac Sim 5.0 first.

## 1. 🌐 Install Isaac Sim 4.5

Please follow the official NVIDIA documentation to install Isaac Sim:
[Isaac Sim 4.5 Installation Guide](https://docs.isaacsim.omniverse.nvidia.com/4.5.0/installation/download.html)

After installation, assuming Isaac Sim is extracted/installed in `${HOME}/isaacsim`:

```bash
# Isaac Sim root directory
export ISAACSIM_PATH="${HOME}/isaacsim"
# Isaac Sim python executable
export ISAACSIM_PYTHON_EXE="${ISAACSIM_PATH}/python.sh"
```

### 1.1 ✅ Verify Isaac Sim Installation

Check that the simulator GUI runs as expected:

```bash
# You can pass the argument "--help" to see all possible arguments.
${ISAACSIM_PATH}/isaac-sim.sh
```

Check that the simulator runs from a standalone python script:

```bash
# Check that python path is set correctly
${ISAACSIM_PYTHON_EXE} -c "print('Isaac Sim configuration is now complete.')"

# Check that Isaac Sim can be launched from python
${ISAACSIM_PYTHON_EXE} ${ISAACSIM_PATH}/standalone_examples/api/isaacsim.core.api/add_cubes.py
```

if the above commands run successfully, Isaac Sim is installed correctly.

---

## 2. 🧪 Install Isaac Lab 2.1.0

You can follow the [Isaac Lab Installation Guide](https://isaac-sim.github.io/IsaacLab/main/source/setup/installation/binaries_installation.html) or use the steps below.

### 2.1 📥 Clone Repository

Clone the Isaac Lab repository into your workspace:

```bash
cd ~
git clone https://github.com/isaac-sim/IsaacLab.git
cd IsaacLab
```

```bash
./isaaclab.sh --help

usage: isaaclab.sh [-h] [-i] [-f] [-p] [-s] [-t] [-o] [-v] [-d] [-n] [-c] -- Utility to manage Isaac Lab.

optional arguments:
   -h, --help           Display the help content.
   -i, --install [LIB]  Install the extensions inside Isaac Lab and learning frameworks (rl_games, rsl_rl, sb3, skrl) as extra dependencies. Default is 'all'.
   -f, --format         Run pre-commit to format the code and check lints.
   -p, --python         Run the python executable provided by Isaac Sim or virtual environment (if active).
   -s, --sim            Run the simulator executable (isaac-sim.sh) provided by Isaac Sim.
   -t, --test           Run all python pytest tests.
   -o, --docker         Run the docker container helper script (docker/container.sh).
   -v, --vscode         Generate the VSCode settings file from template.
   -d, --docs           Build the documentation from source using sphinx.
   -n, --new            Create a new external project or internal task from template.
   -c, --conda [NAME]   Create the conda environment for Isaac Lab. Default name is 'env_isaaclab'.
   -u, --uv [NAME]      Create the uv environment for Isaac Lab. Default name is 'env_isaaclab'.
```

### 2.2 🔗 Create Symbolic Link

Set up a symbolic link between the installed Isaac Sim root folder and `_isaac_sim` in the Isaac Lab directory. This allows Isaac Lab to locate the Isaac Sim Python modules and extensions.

```bash 
# Enter the cloned repository
cd IsaacLab

# Create a symbolic link pointing to your Isaac Sim installation
ln -s ${ISAACSIM_PATH} _isaac_sim

ln -s ${HOME}/isaacsim _isaac_sim

```

### 2.3 🐍 Create Conda Environment (Optional)

Isaac Lab provides a script to quickly create a Conda environment:

```bash
# Create conda environment (default name: 'env_isaaclab')
./isaaclab.sh --conda

# Activate the environment
conda activate env_isaaclab
```

### 2.4 📦 Install Dependencies

Install the required extensions and learning frameworks:

```bash
./isaaclab.sh --install
```

### 2.5 ✅ Verify Isaac Lab Installation

Run a simple example to verify the installation:

```bash
python scripts/tutorials/00_sim/create_empty.py
```

If a window with an empty scene appears (similar to the image below), the installation is successful.

![Verify IsaacLab](./verify_isaaclab.jpg)

---

## 3. 🐢 Install ROS2 Humble

For the simulation side, **ROS2 Humble** is recommended. Please follow the official guide:
[ROS2 Humble Installation Guide](https://docs.ros.org/en/humble/index.html)

Make sure to configure `rosdep` and your environment variables after installation.

---

## 4. 🚀 Run Unitree Go2 Simulation

### 4.1 🛠️ Setup Simulation Environment

```bash
# Activate Isaac Lab environment
conda activate env_isaaclab
#Clone the repo to you local directory
git clone https://github.com/Zhefan-Xu/isaac-go2-ros2.git

cd isaac-go2-ros2

# Start the simulation
python isaac_go2_ros2.py
```

Once the simulation is loaded, the robot can be teleoperated using the keyboard.

### 4.2 ⚡ ROS2 Quick Start

In a new terminal, launch the ROS2 nodes to interact with the simulated robot:

```bash
# Source your ROS2 workspace
source install/setup.bash

# Launch the robot startup script for simulation
ros2 launch go2_core go2_sim_startup.launch.py
```

## 5. 📡 ROS Topics

### Published Topics

| Component | Topic | Type | Frame |
| :--- | :--- | :--- | :--- |
| **🤖 Robot Pose** | `/utlidar/robot_pose` | `PoseStamped` | `odom` |
| **🌩️ LiDAR (Unitree)** | `/unitree_go2/lidar/point_cloud` | `PointCloud2` | `odom` |
| **📏 LaserScan** | `/scan` | `LaserScan` | `base_link` |
| **📷 Camera Image** | `/camera/image_raw` | `Image` | - |
| **🗺️ Global Map** | `/map` | `OccupancyGrid` | `map` |

---


## 📄 License

This project is licensed under the MIT License - see the [LICENSE](../LICENSE) file for details.

## 🙏 Acknowledgments

- Unitree Robotics for the Go2 EDU platform
- ROS2 community for the excellent navigation and SLAM tools
- Contributors and users of this toolbox

## 📞 Support

If you encounter any issues or have questions, please:

1. Check the [Issues](https://github.com/andy-zhuo-02/go2_ros2_toolbox/issues) page
2. Create a new issue with detailed information
3. Include system information and error logs

---

**Note**: This is an unofficial toolbox and is not affiliated with Unitree Robotics.

