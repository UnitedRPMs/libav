%global commit c4642788e83b0858bca449f9b6e71ddb015dfa5d
%bcond_with opencv

Name:           libav
Version:        12.3
Release: 	1%{?dist}
Summary:        Cross-platform solution to record, convert and stream audio/video
Group:          Productivity/Multimedia/Video/Editors and Convertors
Url:            http://libav.org
Source:         https://github.com/libav/libav/archive/%{commit}.tar.gz
License:        GPLv2

BuildRequires:  gcc
BuildRequires:	yasm-devel
BuildRequires:	make
BuildRequires:	openssl-devel
BuildRequires:	libva-devel >= 0.31.0
BuildRequires:	libvdpau-devel
BuildRequires:  zlib-devel
BuildRequires: 	frei0r-devel
BuildRequires:  gnutls-devel
BuildRequires:	libbs2b-devel
BuildRequires: 	libcdio-paranoia-devel
BuildRequires:  libdc1394-devel
#BuildRequires: faac-devel
BuildRequires:	fdk-aac-free-devel
BuildRequires:  freetype-devel
BuildRequires:  gsm-devel
BuildRequires:	ilbc-devel
BuildRequires:  lame-devel >= 3.98.3
BuildRequires: 	opencore-amr-devel vo-amrwbenc-devel
%if %{with opencv}
BuildRequires: 	pkgconfig(opencv)
%endif
BuildRequires:  openjpeg-devel
BuildRequires:  opus-devel
BuildRequires:	pulseaudio-libs-devel
BuildRequires:	librtmp-devel
BuildRequires:  schroedinger-devel
BuildRequires:  speex-devel
BuildRequires:  libtheora-devel
BuildRequires:	twolame-devel
BuildRequires:	vo-aacenc-devel
BuildRequires:  libvorbis-devel
BuildRequires:	x264-devel >= 0.0.0-0.31
BuildRequires:	x265-devel
BuildRequires:  xvidcore-devel
BuildRequires:	libXext-devel
BuildRequires:	libXfixes-devel
BuildRequires:	libdav1d-devel >= 0.4.0
BuildRequires:  jack-audio-connection-kit-devel
#BuildRequires:	libvpx-devel 
BuildRequires:  SDL-devel podman
Requires:       libav-libs = %{version}-%{release}
BuildRoot:      %{_tmppath}/%{name}-%{version}-build

%description
Libav is a complete, cross-platform solution to record, convert and stream 
audio and video. It includes libavcodec - the leading audio/video codec library

%package        libs
Summary:        Libraries for libav
Conflicts:	ffmpeg-libs >= 4.0
Recommends:	libavresample = %{version}-%{release}

%description    libs
This package contains the libraries for libav.

%package        -n libavresample
Summary:         libavresample Libraries

%description    -n libavresample
This package contains the libraries of libavresample.

%package 	devel
Summary:        Cross-platform to record, convert, stream media files - Devel package
Group:          Development/Libraries/Other
Requires:       libav = %{version}-%{release}
Requires:       libavresample-devel = %{version}-%{release}
Conflicts:	ffmpeg-devel >= 4.0

%description 	devel
Libav is a complete, cross-platform solution to record, convert and stream audio and video.

%package 	-n libavresample-devel
Summary:        Devel libavresample libraries
Group:          Development/Libraries/Other
Requires:       libavresample = %{version}-%{release}


%description 	-n libavresample-devel
This package contains the devel libraries of libavresample.

%prep
%autosetup -n libav-%{commit} 

export CFLAGS='%{optflags}'

./configure \
	--prefix=/usr \
	--libdir=%{_libdir}  \
	--shlibdir=%{_libdir}  \
	--enable-doc \
	--enable-avplay \
	--disable-debug \
	--disable-static \
	--enable-shared \
	--enable-runtime-cpudetect \
	--enable-openssl \
	--enable-nonfree \
	--enable-gpl \
	--enable-version3 \
	--enable-vdpau \
	--enable-vaapi \
	--enable-bzlib \
	--enable-frei0r \
	--enable-libbs2b \
	--enable-libcdio \
	--enable-libdc1394 \
	--enable-libfdk-aac \
	--enable-libfreetype \
	--enable-libgsm \
	--enable-libilbc \
	--enable-libmp3lame \
	--enable-libopencore-amrnb \
	--enable-libopencore-amrwb \
%if %{with opencv}
    	--enable-libopencv \
%endif
	--enable-libopenjpeg \
	--enable-libopus \
	--enable-libpulse \
	--enable-librtmp \
	--enable-libschroedinger \
	--enable-libspeex \
	--enable-libtheora \
	--enable-libtwolame \
	--enable-libvo-aacenc \
	--enable-libvo-amrwbenc \
	--enable-libvorbis \
	--enable-libx264 \
	--enable-libx265 \
	--enable-libdav1d \
	--enable-libjack \
	--enable-libxvid \
	--extra-cflags='%{optflags}' --optflags='%{optflags}' \
	--enable-pic

%build
%make_build V=0

%install
%make_install V=0

%clean
rm -rf $RPM_BUILD_ROOT

%files
%{_bindir}/avplay
%{_bindir}/avconv
%{_bindir}/avprobe
%{_datadir}/avconv/libvpx-1080p.avpreset
%{_datadir}/avconv/libvpx-1080p50_60.avpreset
%{_datadir}/avconv/libvpx-360p.avpreset
%{_datadir}/avconv/libvpx-720p.avpreset
%{_datadir}/avconv/libvpx-720p50_60.avpreset
%{_datadir}/avconv/libx264-baseline.avpreset
%{_datadir}/avconv/libx264-fast.avpreset
%{_datadir}/avconv/libx264-fast_firstpass.avpreset
%{_datadir}/avconv/libx264-faster.avpreset
%{_datadir}/avconv/libx264-faster_firstpass.avpreset
%{_datadir}/avconv/libx264-ipod320.avpreset
%{_datadir}/avconv/libx264-ipod640.avpreset
%{_datadir}/avconv/libx264-lossless_fast.avpreset
%{_datadir}/avconv/libx264-lossless_max.avpreset
%{_datadir}/avconv/libx264-lossless_medium.avpreset
%{_datadir}/avconv/libx264-lossless_slow.avpreset
%{_datadir}/avconv/libx264-lossless_slower.avpreset
%{_datadir}/avconv/libx264-lossless_ultrafast.avpreset
%{_datadir}/avconv/libx264-main.avpreset
%{_datadir}/avconv/libx264-medium.avpreset
%{_datadir}/avconv/libx264-medium_firstpass.avpreset
%{_datadir}/avconv/libx264-placebo.avpreset
%{_datadir}/avconv/libx264-placebo_firstpass.avpreset
%{_datadir}/avconv/libx264-slow.avpreset
%{_datadir}/avconv/libx264-slow_firstpass.avpreset
%{_datadir}/avconv/libx264-slower.avpreset
%{_datadir}/avconv/libx264-slower_firstpass.avpreset
%{_datadir}/avconv/libx264-superfast.avpreset
%{_datadir}/avconv/libx264-superfast_firstpass.avpreset
%{_datadir}/avconv/libx264-ultrafast.avpreset
%{_datadir}/avconv/libx264-ultrafast_firstpass.avpreset
%{_datadir}/avconv/libx264-veryfast.avpreset
%{_datadir}/avconv/libx264-veryfast_firstpass.avpreset
%{_datadir}/avconv/libx264-veryslow.avpreset
%{_datadir}/avconv/libx264-veryslow_firstpass.avpreset
%{_mandir}/man1/avplay.1.gz
%{_mandir}/man1/avconv.1.gz
%{_mandir}/man1/avprobe.1.gz

%files libs
%{_libdir}/libavcodec.so.*
%{_libdir}/libavdevice.so.*
%{_libdir}/libavfilter.so.*
%{_libdir}/libavformat.so.*
%{_libdir}/libavutil.so.*
%{_libdir}/libswscale.so.*

%files -n libavresample
%{_libdir}/libavresample.so.*

%files devel
%{_libdir}/libavcodec.so
%{_libdir}/libavdevice.so
%{_libdir}/libavfilter.so
%{_libdir}/libavformat.so
%{_libdir}/libavutil.so
%{_libdir}/libswscale.so
%{_libdir}/pkgconfig/libavcodec.pc
%{_libdir}/pkgconfig/libavdevice.pc
%{_libdir}/pkgconfig/libavfilter.pc
%{_libdir}/pkgconfig/libavformat.pc
%{_libdir}/pkgconfig/libavutil.pc
%{_libdir}/pkgconfig/libswscale.pc
%{_includedir}/libavcodec/
%{_includedir}/libavdevice/
%{_includedir}/libavfilter/
%{_includedir}/libavformat/
%{_includedir}/libavutil/
%{_includedir}/libswscale/

%files -n libavresample-devel
%{_libdir}/libavresample.so
%{_includedir}/libavresample/
%{_libdir}/pkgconfig/libavresample.pc


%changelog

* Sat Aug 10 2019 Unitedrpms Project <unitedrpms AT protonmail DOT com> 12.3-1
- Updated to 12.3
- libavresample package

* Fri Jul 08 2016 David Vásquez <davidjeremias82 AT gmail DOT com> - 11.7-1-20160711git0fc667e
- Updated to 11.7-20160711git0fc667e

* Fri May 06 2016 David Vásquez <davidjeremias82 AT gmail DOT com> 11.6-2-20160421gitd0c0a42
- Added conditional build for opencv

* Thu Apr 21 2016 David Vásquez <davidjeremias82 AT gmail DOT com> 11.6-1-20160421gitd0c0a42
- Updated to 11.6-20160421-d0c0a42

* Mon Feb 22 2016 David Vasquez <davidjeremias82[AT]gmail [DOT] com> - 11.4-1-20160223git0069d45
- Initial package of libav 11.4-20160223-0069d45
