# Script generated with Bloom
pkgdesc="ROS - Wrapper around Particle Filter implementation. The SelfLocalizer can be used as library or as a ros-node."
url='http://wiki.ros.org/self_localizer'

pkgname='ros-kinetic-nav2d-localizer'
pkgver='0.3.2_1'
pkgrel=1
arch=('any')
license=('GPLv3'
)

makedepends=('ros-kinetic-catkin'
'ros-kinetic-geometry-msgs'
'ros-kinetic-nav-msgs'
'ros-kinetic-roscpp'
'ros-kinetic-sensor-msgs'
'ros-kinetic-tf'
)

depends=('ros-kinetic-geometry-msgs'
'ros-kinetic-nav-msgs'
'ros-kinetic-roscpp'
'ros-kinetic-sensor-msgs'
'ros-kinetic-tf'
)

conflicts=()
replaces=()

_dir=nav2d_localizer
source=()
md5sums=()

prepare() {
    cp -R $startdir/nav2d_localizer $srcdir/nav2d_localizer
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

