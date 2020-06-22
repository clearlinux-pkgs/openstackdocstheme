#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : openstackdocstheme
Version  : 2.2.4
Release  : 49
URL      : https://files.pythonhosted.org/packages/ff/a3/5aec1fa34493da073e0a8fc27d25e43b2a6700af6bfc0e64b634d732cc15/openstackdocstheme-2.2.4.tar.gz
Source0  : https://files.pythonhosted.org/packages/ff/a3/5aec1fa34493da073e0a8fc27d25e43b2a6700af6bfc0e64b634d732cc15/openstackdocstheme-2.2.4.tar.gz
Summary  : OpenStack Docs Theme
Group    : Development/Tools
License  : Apache-2.0
Requires: openstackdocstheme-bin = %{version}-%{release}
Requires: openstackdocstheme-license = %{version}-%{release}
Requires: openstackdocstheme-python = %{version}-%{release}
Requires: openstackdocstheme-python3 = %{version}-%{release}
Requires: dulwich
Requires: pbr
BuildRequires : buildreq-distutils3
BuildRequires : dulwich
BuildRequires : pbr

%description
Team and repository tags
        ========================

%package bin
Summary: bin components for the openstackdocstheme package.
Group: Binaries
Requires: openstackdocstheme-license = %{version}-%{release}

%description bin
bin components for the openstackdocstheme package.


%package license
Summary: license components for the openstackdocstheme package.
Group: Default

%description license
license components for the openstackdocstheme package.


%package python
Summary: python components for the openstackdocstheme package.
Group: Default
Requires: openstackdocstheme-python3 = %{version}-%{release}

%description python
python components for the openstackdocstheme package.


%package python3
Summary: python3 components for the openstackdocstheme package.
Group: Default
Requires: python3-core
Provides: pypi(openstackdocstheme)
Requires: pypi(dulwich)
Requires: pypi(pbr)

%description python3
python3 components for the openstackdocstheme package.


%prep
%setup -q -n openstackdocstheme-2.2.4
cd %{_builddir}/openstackdocstheme-2.2.4

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C.UTF-8
export SOURCE_DATE_EPOCH=1592852753
export GCC_IGNORE_WERROR=1
export AR=gcc-ar
export RANLIB=gcc-ranlib
export NM=gcc-nm
export CFLAGS="$CFLAGS -O3 -ffat-lto-objects -flto=4 "
export FCFLAGS="$FFLAGS -O3 -ffat-lto-objects -flto=4 "
export FFLAGS="$FFLAGS -O3 -ffat-lto-objects -flto=4 "
export CXXFLAGS="$CXXFLAGS -O3 -ffat-lto-objects -flto=4 "
export MAKEFLAGS=%{?_smp_mflags}
python3 setup.py build

%install
export MAKEFLAGS=%{?_smp_mflags}
rm -rf %{buildroot}
mkdir -p %{buildroot}/usr/share/package-licenses/openstackdocstheme
cp %{_builddir}/openstackdocstheme-2.2.4/LICENSE %{buildroot}/usr/share/package-licenses/openstackdocstheme/294b43b2cec9919063be1a3b49e8722648424779
python3 -tt setup.py build  install --root=%{buildroot}
echo ----[ mark ]----
cat %{buildroot}/usr/lib/python3*/site-packages/*/requires.txt || :
echo ----[ mark ]----

%files
%defattr(-,root,root,-)

%files bin
%defattr(-,root,root,-)
/usr/bin/docstheme-build-pdf
/usr/bin/docstheme-build-translated.sh
/usr/bin/docstheme-lang-display-name.py

%files license
%defattr(0644,root,root,0755)
/usr/share/package-licenses/openstackdocstheme/294b43b2cec9919063be1a3b49e8722648424779

%files python
%defattr(-,root,root,-)

%files python3
%defattr(-,root,root,-)
/usr/lib/python3*/*
