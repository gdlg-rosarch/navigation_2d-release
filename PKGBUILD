# Script generated with Bloom
pkgdesc="ROS - Meta-Package containing modules for 2D-Navigation"
url='http://wiki.ros.org/navigation_2d'

pkgname='ros-kinetic-nav2d'
pkgver='0.3.2_1'
pkgrel=1
arch=('any')
license=('GPLv3'
)

makedepends=('ros-kinetic-catkin'
)

depends=('ros-kinetic-nav2d-exploration'
'ros-kinetic-nav2d-karto'
'ros-kinetic-nav2d-localizer'
'ros-kinetic-nav2d-msgs'
'ros-kinetic-nav2d-navigator'
'ros-kinetic-nav2d-operator'
'ros-kinetic-nav2d-remote'
'ros-kinetic-nav2d-tutorials'
)

conflicts=()
replaces=()

_dir=nav2d
source=()
md5sums=()

prepare() {
    cp -R $startdir/nav2d $srcdir/nav2d
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

