# 实机环境（Real World）

本节介绍在 **真实 Unitree Go2 EDU 机器人** 上部署与使用本 ROS2 工具箱的流程，包括前置条件、安装步骤、使用方法以及开发相关的坐标系与话题说明。

---

## 📋 前置条件

> **⚠️ 注意：本仓库的功能仅在 Go2 EDU 扩展坞自带计算机上测试通过。  
> 其他环境（例如通过网线连接 PC 与扩展坞）目前尚未验证兼容性与稳定性，请自行评估风险。**

当前工具箱在以下实机环境中开发与测试：

- **操作系统**：Ubuntu 20.04  
- **ROS2**：Foxy  
- **固件版本**：v1.1.7（已测试）  

确保你的 Go2 固件版本与官方 ROS2 包版本匹配，避免因协议或话题变更导致通信异常。

---

## 🛠️ 安装步骤

### 1. 安装官方 Unitree ROS2 包

首先，需要安装 Unitree 官方提供的 ROS2 支持包：

```bash
# 请严格按照官方文档执行
# 官方仓库地址：
# https://github.com/unitreerobotics/unitree_ros2
```

安装完成后，建议先确认官方示例是否能在机器人上正常运行，再继续安装本工具箱。

### 2. 安装依赖

#### 2.1 ROS2 依赖包

在 Go2 扩展坞电脑上执行：

```bash
sudo apt-get install ros-foxy-navigation2 \
                     ros-foxy-nav2-bringup \
                     ros-foxy-pcl-ros \
                     ros-foxy-tf-transformations \
                     ros-foxy-slam-toolbox
```

#### 2.2 Python 依赖包（可选）

如果需要使用部分 Python 工具/脚本，可以安装：

```bash
pip3 install transforms3d
```

### 3. 编译工作空间

在扩展坞电脑上创建并编译 ROS2 工作空间：

```bash
# 创建工作空间
mkdir -p ~/go2_ros2_ws/src
cd ~/go2_ros2_ws/src

# 克隆本仓库
git clone https://github.com/andy-zhuo-02/go2_ros2_toolbox.git

# 编译
cd ..
colcon build
```

编译完成后，每次使用前记得 `source` 对应的 `setup.bash`。

---

## 🎯 使用方法

### 1. 快速启动

```bash
# 进入工作空间
cd ~/go2_ros2_ws

# 加载编译环境
source install/setup.bash

# 启动机器人基础功能（底盘、传感器等）
ros2 launch go2_core go2_startup.launch.py
```

确认机器人可以正常站立、行走，并能在 RViz 中看到里程计与点云等数据。

### 2. SLAM 操作

本工具箱集成了 SLAM Toolbox，可用于在线建图与保存/加载地图：

- **地图保存（序列化）**：将当前生成的地图保存到文件，供之后复用。  
- **地图加载（反序列化）**：在新会话中加载之前保存的地图，直接进入定位模式。  

具体启动命令和参数配置，可根据你的使用场景在 launch 文件与参数文件中进行调整。

### 3. 导航流程

使用 Navigation2 进行自主导航的一般步骤如下：

1. 启动导航相关节点与 RViz2。  
2. 在 RViz2 中选择 “Navigation2 Goal” 工具。  
3. 在地图上单击目标位置以设置导航目标点。  
4. 拖动鼠标调整箭头方向以设置期望朝向。  

机器人会基于当前地图、传感器信息和代价地图规划路径并执行导航。

---

## 🔧 开发说明

### 坐标系参考

| 坐标系         | 说明           | 来源                   |
| -------------- | -------------- | ---------------------- |
| `/odom`      | 里程计坐标系   | Unitree Go2 里程计话题 |
| `/map`       | 地图坐标系     | SLAM Toolbox           |
| `/base_link` | 机器人基座坐标 | Unitree Go2 里程计话题 |

### ROS 话题

#### 发布者

| 组件             | 话题名                      | 类型        | 坐标系    |
| ---------------- | --------------------------- | ----------- | --------- |
| 机器人位姿       | `/utlidar/robot_pose`     | PoseStamped | `/odom` |
| 激光雷达（原始） | `/utlidar/cloud_deskewed` | PointCloud2 | `/odom` |
| 激光雷达（累积） | `/trans_cloud`            | PointCloud2 | `/odom` |
| 相机图像         | `/camera/image_raw`       | Image       | -         |

#### 订阅者

| 组件         | 话题名      | 类型  | 坐标系        |
| ------------ | ----------- | ----- | ------------- |
| 速度控制命令 | `/cmd_vel`  | Twist | `/base_link` |

## 🤝 贡献

欢迎贡献代码！请随时提交 issue 或 pull request。

## 📄 许可证

本项目采用 MIT 许可证，详见 [LICENSE](LICENSE) 文件。

## 🙏 鸣谢

- Unitree Robotics 提供 Go2 EDU 平台
- ROS2 社区的导航与 SLAM 工具
- 本工具箱的贡献者与用户

## 📞 支持

如遇问题或有疑问，请：

1. 查看 [Issues](https://github.com/andy-zhuo-02/go2_ros2_toolbox/issues) 页面
2. 创建新 issue 并详细描述问题
3. 附上系统信息与错误日志

---

**注意**：本工具箱为非官方项目，与 Unitree Robotics 无直接关联。