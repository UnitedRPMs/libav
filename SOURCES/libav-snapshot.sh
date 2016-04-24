#!/bin/bash

tag_name=v11.6

set -x

tmp=$(mktemp -d)

trap cleanup EXIT
cleanup() {
    set +e
    [ -z "$tmp" -o ! -d "$tmp" ] || rm -rf "$tmp"
}

unset CDPATH
pwd=$(pwd)
date=$(date +%Y%m%d)
package=libav
branch=master
name=libav

pushd ${tmp}
git clone -b ${tag_name} --depth 1 git://git.libav.org/libav.git
cd ${package}
git checkout ${branch}
tag=$(git rev-list HEAD -n 1 | cut -c 1-7)
version=`git describe --tags | awk -F '-' '{print $1}' | tr -d 'v'`
cd ${tmp}
tar Jcf "$pwd"/${name}-${version}-${date}-${tag}.tar.xz ${package}
  

