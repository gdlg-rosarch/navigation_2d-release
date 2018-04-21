# Script generated with Bloom
pkgdesc="ROS - Graph-based Simultaneous Localization and Mapping module. Includes OpenKarto GraphSLAM library by &quot;SRI International&quot;."
url='http://wiki.ros.org/robot_operator'

pkgname='ros-kinetic-nav2d-karto'
pkgver='0.3.2_1'
pkgrel=1
arch=('any')
license=('GPLv3'
)

makedepends=('eigen3'
'intel-tbb'
'ros-kinetic-catkin'
'ros-kinetic-geometry-msgs'
'ros-kinetic-nav-msgs'
'ros-kinetic-nav2d-localizer'
'ros-kinetic-nav2d-msgs'
'ros-kinetic-roscpp'
'ros-kinetic-tf'
'ros-kinetic-visualization-msgs'
'suitesparse'
)

depends=('eigen3'
'intel-tbb'
'ros-kinetic-geometry-msgs'
'ros-kinetic-nav-msgs'
'ros-kinetic-nav2d-localizer'
'ros-kinetic-nav2d-msgs'
'ros-kinetic-roscpp'
'ros-kinetic-tf'
'ros-kinetic-visualization-msgs'
'suitesparse'
)

conflicts=()
replaces=()

_dir=nav2d_karto
source=()
md5sums=()

prepare() {
    cp -R $startdir/nav2d_karto $srcdir/nav2d_karto
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

