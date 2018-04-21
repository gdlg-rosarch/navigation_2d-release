# Script generated with Bloom
pkgdesc="ROS - The operator is a lightweight, purely reactive obstacle-avoidance module for mobile robots moving in a planar environment. The operator node works by evaluating a set of predefined motion primitives based on a local costmap and a desired direction. The best evaluated motion command will be send to the mobile base."
url='http://wiki.ros.org/nav2d_operator'

pkgname='ros-kinetic-nav2d-operator'
pkgver='0.3.2_1'
pkgrel=1
arch=('any')
license=('GPLv3'
)

makedepends=('ros-kinetic-catkin'
'ros-kinetic-costmap-2d'
'ros-kinetic-message-generation'
'ros-kinetic-roscpp'
'ros-kinetic-sensor-msgs'
'ros-kinetic-tf'
)

depends=('ros-kinetic-costmap-2d'
'ros-kinetic-message-runtime'
'ros-kinetic-roscpp'
'ros-kinetic-sensor-msgs'
'ros-kinetic-tf'
)

conflicts=()
replaces=()

_dir=nav2d_operator
source=()
md5sums=()

prepare() {
    cp -R $startdir/nav2d_operator $srcdir/nav2d_operator
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

