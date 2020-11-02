#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : mobile-broadband-provider-info
Version  : 20190618
Release  : 5
URL      : https://github.com/GNOME/mobile-broadband-provider-info/archive/20190618/mobile-broadband-provider-info-20190618.tar.gz
Source0  : https://github.com/GNOME/mobile-broadband-provider-info/archive/20190618/mobile-broadband-provider-info-20190618.tar.gz
Summary  : Mobile Broadband Service Provider Information Database
Group    : Development/Tools
License  : Public-Domain
Requires: mobile-broadband-provider-info-data = %{version}-%{release}
BuildRequires : libxml2-dev
BuildRequires : libxslt-bin

%description
This package contains mobile broadband settings for different service providers
in different countries. The Package contains only informational files so it's
safe for distributions to grab updates even during feature freeze and
maintenance stages.

%package data
Summary: data components for the mobile-broadband-provider-info package.
Group: Data

%description data
data components for the mobile-broadband-provider-info package.


%package dev
Summary: dev components for the mobile-broadband-provider-info package.
Group: Development
Requires: mobile-broadband-provider-info-data = %{version}-%{release}
Provides: mobile-broadband-provider-info-devel = %{version}-%{release}
Requires: mobile-broadband-provider-info = %{version}-%{release}

%description dev
dev components for the mobile-broadband-provider-info package.


%prep
%setup -q -n mobile-broadband-provider-info-20190618
cd %{_builddir}/mobile-broadband-provider-info-20190618

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C.UTF-8
export SOURCE_DATE_EPOCH=1604357518
export GCC_IGNORE_WERROR=1
export AR=gcc-ar
export RANLIB=gcc-ranlib
export NM=gcc-nm
export CFLAGS="$CFLAGS -O3 -ffat-lto-objects -flto=4 "
export FCFLAGS="$FFLAGS -O3 -ffat-lto-objects -flto=4 "
export FFLAGS="$FFLAGS -O3 -ffat-lto-objects -flto=4 "
export CXXFLAGS="$CXXFLAGS -O3 -ffat-lto-objects -flto=4 "
%autogen --disable-static
make  %{?_smp_mflags}

%check
export LANG=C.UTF-8
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
make %{?_smp_mflags} check

%install
export SOURCE_DATE_EPOCH=1604357518
rm -rf %{buildroot}
%make_install

%files
%defattr(-,root,root,-)

%files data
%defattr(-,root,root,-)
/usr/share/mobile-broadband-provider-info/apns-conf.xml
/usr/share/mobile-broadband-provider-info/serviceproviders.2.dtd
/usr/share/mobile-broadband-provider-info/serviceproviders.xml

%files dev
%defattr(-,root,root,-)
/usr/lib64/pkgconfig/mobile-broadband-provider-info.pc
