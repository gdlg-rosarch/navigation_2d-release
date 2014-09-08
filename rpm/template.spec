Name:           ros-hydro-nav2d-tutorials
Version:        0.2.0
Release:        0%{?dist}
Summary:        ROS nav2d_tutorials package

Group:          Development/Libraries
License:        GPLv3
URL:            http://wiki.ros.org/nav2d_tutorials
Source0:        %{name}-%{version}.tar.gz

Requires:       ros-hydro-nav2d-exploration
Requires:       ros-hydro-nav2d-karto
Requires:       ros-hydro-nav2d-localizer
Requires:       ros-hydro-nav2d-msgs
Requires:       ros-hydro-nav2d-navigator
Requires:       ros-hydro-nav2d-operator
Requires:       ros-hydro-nav2d-remote
BuildRequires:  ros-hydro-catkin

%description
Contains a set of tutorials that run 2D-Navigation within Stage-Simulator.

%prep
%setup -q

%build
# In case we're installing to a non-standard location, look for a setup.sh
# in the install tree that was dropped by catkin, and source it.  It will
# set things like CMAKE_PREFIX_PATH, PKG_CONFIG_PATH, and PYTHONPATH.
if [ -f "/opt/ros/hydro/setup.sh" ]; then . "/opt/ros/hydro/setup.sh"; fi
mkdir -p build && cd build
%cmake .. \
        -UINCLUDE_INSTALL_DIR \
        -ULIB_INSTALL_DIR \
        -USYSCONF_INSTALL_DIR \
        -USHARE_INSTALL_PREFIX \
        -ULIB_SUFFIX \
        -DCMAKE_INSTALL_PREFIX="/opt/ros/hydro" \
        -DCMAKE_PREFIX_PATH="/opt/ros/hydro" \
        -DSETUPTOOLS_DEB_LAYOUT=OFF \
        -DCATKIN_BUILD_BINARY_PACKAGE="1" \

make %{?_smp_mflags}

%install
# In case we're installing to a non-standard location, look for a setup.sh
# in the install tree that was dropped by catkin, and source it.  It will
# set things like CMAKE_PREFIX_PATH, PKG_CONFIG_PATH, and PYTHONPATH.
if [ -f "/opt/ros/hydro/setup.sh" ]; then . "/opt/ros/hydro/setup.sh"; fi
cd build
make %{?_smp_mflags} install DESTDIR=%{buildroot}

%files
/opt/ros/hydro

%changelog
* Mon Sep 08 2014 Sebastian Kasperski <sebastian.kasperski@dfki.de> - 0.2.0-0
- Autogenerated by Bloom

