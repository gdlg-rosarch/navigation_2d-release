# Script generated with Bloom
pkgdesc="ROS - This package provides a node for higher level navigation of a mobile robot in a planar environment. It needs a map and the robot's position within this map to create a plan for navigation. When used together with a SLAM module it can also be used to perform autonomous exploration of the robot's workspace."
url='http://wiki.ros.org/robot_operator'

pkgname='ros-kinetic-nav2d-navigator'
pkgver='0.3.2_1'
pkgrel=1
arch=('any')
license=('GPLv3'
)

makedepends=('ros-kinetic-actionlib'
'ros-kinetic-actionlib-msgs'
'ros-kinetic-catkin'
'ros-kinetic-geometry-msgs'
'ros-kinetic-message-generation'
'ros-kinetic-nav2d-msgs'
'ros-kinetic-nav2d-operator'
'ros-kinetic-pluginlib'
'ros-kinetic-roscpp'
'ros-kinetic-std-srvs'
'ros-kinetic-tf'
)

depends=('ros-kinetic-actionlib'
'ros-kinetic-actionlib-msgs'
'ros-kinetic-geometry-msgs'
'ros-kinetic-message-runtime'
'ros-kinetic-nav2d-msgs'
'ros-kinetic-nav2d-operator'
'ros-kinetic-pluginlib'
'ros-kinetic-roscpp'
'ros-kinetic-std-srvs'
'ros-kinetic-tf'
)

conflicts=()
replaces=()

_dir=nav2d_navigator
source=()
md5sums=()

prepare() {
    cp -R $startdir/nav2d_navigator $srcdir/nav2d_navigator
}

build() {
  # Use ROS environment variables
  source /usr/share/ros-build-tools/clear-ros-env.sh
  [ -f /opt/ros/kinetic/setup.bash ] && source /opt/ros/kinetic/setup.bash

  # Create build directory
  [ -d ${srcdir}/build ] || mkdir ${srcdir}/build
  cd ${srcdir}/build

  # Fix Python2/Python3 conflicts
  /usr/share/ros-build-tools/fix-python-scripts.sh -v 2 ${srcdir}/${_dir}

  # Build project
  cmake ${srcdir}/${_dir} \
        -DCMAKE_BUILD_TYPE=Release \
        -DCATKIN_BUILD_BINARY_PACKAGE=ON \
        -DCMAKE_INSTALL_PREFIX=/opt/ros/kinetic \
        -DPYTHON_EXECUTABLE=/usr/bin/python2 \
        -DPYTHON_INCLUDE_DIR=/usr/include/python2.7 \
        -DPYTHON_LIBRARY=/usr/lib/libpython2.7.so \
        -DPYTHON_BASENAME=-python2.7 \
        -DSETUPTOOLS_DEB_LAYOUT=OFF
  make
}

package() {
  cd "${srcdir}/build"
  make DESTDIR="${pkgdir}/" install
}

