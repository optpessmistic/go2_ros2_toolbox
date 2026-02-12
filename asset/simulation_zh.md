# 🖥️ 仿真环境（Simulation）

本节介绍如何基于 **Isaac Sim 4.5** 与 **Isaac Lab 2.1.0** 搭建 Unitree Go2 的仿真环境，便于在桌面端进行开发、调试与验证。

推荐环境如下：

- 🐧 **操作系统**: Ubuntu 22.04
- 🐢 **ROS2**: Humble
- 🌐 **Isaac Sim**: 4.5
- 🧪 **Isaac Lab**: 2.1.0

## 1. 🌐 安装 Isaac Sim 4.5

请按照 NVIDIA 官方文档安装 Isaac Sim：
[Isaac Sim 4.5 安装指南](https://docs.isaacsim.omniverse.nvidia.com/4.5.0/installation/download.html)

安装完成后，假设 Isaac Sim 解压/安装在 `${HOME}/isaacsim`：

```bash
# Isaac Sim 根目录
export ISAACSIM_PATH="${HOME}/isaacsim"
# Isaac Sim python 可执行文件
export ISAACSIM_PYTHON_EXE="${ISAACSIM_PATH}/python.sh"
```

### 1.1 ✅ 验证 Isaac Sim 安装

检查 Isaac Sim 图形界面是否可以正常启动：

```bash
# 可以加上 "--help" 查看所有支持的参数
${ISAACSIM_PATH}/isaac-sim.sh
```

检查 Isaac Sim 是否可以通过独立的 Python 脚本运行：

```bash
# 检查 Python 路径设置是否正确
${ISAACSIM_PYTHON_EXE} -c "print('Isaac Sim configuration is now complete.')"

# 检查是否可以通过 Python 启动 Isaac Sim
${ISAACSIM_PYTHON_EXE} ${ISAACSIM_PATH}/standalone_examples/api/isaacsim.core.api/add_cubes.py
```

如果上述命令都能成功运行，说明 Isaac Sim 安装正确。

---

## 2. 🧪 安装 Isaac Lab 2.1.0

您可以遵循 [Isaac Lab 安装指南](https://isaac-sim.github.io/IsaacLab/main/source/setup/installation/binaries_installation.html) 或使用以下步骤。

### 2.1 📥 克隆仓库

将 Isaac Lab 仓库克隆到您的工作空间中：

```bash
cd ~
git clone https://github.com/isaac-sim/IsaacLab.git
cd IsaacLab
```

### 2.2 🔗 创建符号链接

在 Isaac Lab 目录下建立指向已安装 Isaac Sim 根目录的符号链接 `_isaac_sim`。这使得 Isaac Lab 能够定位 Isaac Sim 的 Python 模块和扩展。

```bash
# 进入克隆的仓库
cd IsaacLab

# 创建指向 Isaac Sim 安装路径的符号链接
ln -s ${ISAACSIM_PATH} _isaac_sim
```

### 2.3 🐍 创建 Conda 环境（可选）

Isaac Lab 提供了一个脚本来快速创建 Conda 环境：

```bash
# 创建 conda 环境（默认名称：'env_isaaclab'）
./isaaclab.sh --conda

# 激活环境
conda activate env_isaaclab
```

### 2.4 📦 安装依赖

安装所需的扩展和学习框架：

```bash
./isaaclab.sh --install
```

### 2.5 ✅ 验证 Isaac Lab 安装

运行一个简单的示例来验证安装：

```bash
python scripts/tutorials/00_sim/create_empty.py
```

如果出现一个带有空场景的窗口（类似于下图），则安装成功。

![Verify IsaacLab](./verify_isaaclab.jpg)

---

## 3. 🐢 安装 ROS2 Humble

对于仿真端，推荐使用 **ROS2 Humble**。请遵循官方指南：
[ROS2 Humble 安装指南](https://docs.ros.org/en/humble/index.html)

安装完成后，请确保配置好 `rosdep` 和您的环境变量。

---

## 4. 🚀 运行 Unitree Go2 仿真

一旦 Isaac Sim、Isaac Lab 和 ROS2 Humble 安装完成，您就可以运行 Go2 仿真了。

### 4.1 🛠️ 设置仿真环境

```bash
# 激活 Isaac Lab 环境（若使用了 Conda）
conda activate env_isaaclab

# 克隆仿真仓库
git clone https://github.com/optpessmistic/go2_ros2_toolbox
cd isaac-go2-ros2

# 启动仿真
python isaac_go2_ros2.py
```

一旦仿真加载完成，可以使用键盘遥控机器人。

### 4.2 ⚡ ROS2 快速启动

在一个新的终端中，启动 ROS2 节点以与仿真机器人交互：

```bash
# Source 您的 ROS2 工作空间
source install/setup.bash

# 启动仿真机器人的启动脚本
ros2 launch go2_core go2_sim_startup.launch.py
```

## 5. 📡 ROS 话题 (ROS Topics)

### 已发布的话题 (Published Topics)

| 组件 | 话题 | 类型 | 坐标系 (Frame) |
| :--- | :--- | :--- | :--- |
| **🤖 机器人位姿** | `/utlidar/robot_pose` | `PoseStamped` | `odom` |
| **🌩️ 激光雷达 (Unitree)** | `/unitree_go2/lidar/point_cloud` | `PointCloud2` | `odom` |
| **📏 激光扫描 (LaserScan)** | `/scan` | `LaserScan` | `base_link` |
| **📷 相机图像** | `/camera/image_raw` | `Image` | - |
| **🗺️ 全局地图** | `/map` | `OccupancyGrid` | `map` |

---

## 📄 许可证 (License)

本项目采用 MIT 许可证 - 详情请参阅 [LICENSE](../LICENSE) 文件。

## 🙏 致谢 (Acknowledgments)

- Unitree Robotics 提供 Go2 EDU 平台
- ROS2 社区提供优秀的导航和 SLAM 工具
- 本工具箱的贡献者和用户

## 📞 支持 (Support)

如果您遇到任何问题或有任何疑问，请：

1. 查看 [Issues](https://github.com/andy-zhuo-02/go2_ros2_toolbox/issues) 页面
2. 创建一个新的 Issue 并提供详细信息
3. 包含系统信息和错误日志

---

**注意**：这是一个非官方工具箱，与 Unitree Robotics 无关联。


