Name:           ros-kinetic-nav2d-operator
Version:        0.3.2
Release:        0%{?dist}
Summary:        ROS nav2d_operator package

Group:          Development/Libraries
License:        GPLv3
URL:            http://wiki.ros.org/nav2d_operator
Source0:        %{name}-%{version}.tar.gz

Requires:       ros-kinetic-costmap-2d
Requires:       ros-kinetic-message-runtime
Requires:       ros-kinetic-roscpp
Requires:       ros-kinetic-sensor-msgs
Requires:       ros-kinetic-tf
BuildRequires:  ros-kinetic-catkin
BuildRequires:  ros-kinetic-costmap-2d
BuildRequires:  ros-kinetic-message-generation
BuildRequires:  ros-kinetic-roscpp
BuildRequires:  ros-kinetic-sensor-msgs
BuildRequires:  ros-kinetic-tf

%description
The operator is a lightweight, purely reactive obstacle-avoidance module for
mobile robots moving in a planar environment. The operator node works by
evaluating a set of predefined motion primitives based on a local costmap and a
desired direction. The best evaluated motion command will be send to the mobile
base.

%prep
%setup -q

%build
# In case we're installing to a non-standard location, look for a setup.sh
# in the install tree that was dropped by catkin, and source it.  It will
# set things like CMAKE_PREFIX_PATH, PKG_CONFIG_PATH, and PYTHONPATH.
if [ -f "/opt/ros/kinetic/setup.sh" ]; then . "/opt/ros/kinetic/setup.sh"; fi
mkdir -p obj-%{_target_platform} && cd obj-%{_target_platform}
%cmake .. \
        -UINCLUDE_INSTALL_DIR \
        -ULIB_INSTALL_DIR \
        -USYSCONF_INSTALL_DIR \
        -USHARE_INSTALL_PREFIX \
        -ULIB_SUFFIX \
        -DCMAKE_INSTALL_LIBDIR="lib" \
        -DCMAKE_INSTALL_PREFIX="/opt/ros/kinetic" \
        -DCMAKE_PREFIX_PATH="/opt/ros/kinetic" \
        -DSETUPTOOLS_DEB_LAYOUT=OFF \
        -DCATKIN_BUILD_BINARY_PACKAGE="1" \

make %{?_smp_mflags}

%install
# In case we're installing to a non-standard location, look for a setup.sh
# in the install tree that was dropped by catkin, and source it.  It will
# set things like CMAKE_PREFIX_PATH, PKG_CONFIG_PATH, and PYTHONPATH.
if [ -f "/opt/ros/kinetic/setup.sh" ]; then . "/opt/ros/kinetic/setup.sh"; fi
cd obj-%{_target_platform}
make %{?_smp_mflags} install DESTDIR=%{buildroot}

%files
/opt/ros/kinetic

%changelog
* Tue Mar 28 2017 Sebastian Kasperski <sebastian.kasperski@dfki.de> - 0.3.2-0
- Autogenerated by Bloom

* Fri Mar 03 2017 Sebastian Kasperski <sebastian.kasperski@dfki.de> - 0.3.1-0
- Autogenerated by Bloom

