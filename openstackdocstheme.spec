#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : openstackdocstheme
Version  : 1.30.0
Release  : 33
URL      : https://files.pythonhosted.org/packages/b1/d1/051d4bafb4e6137a91db23c95c73a5470b8e1330c508a82cbac2feb4c1c8/openstackdocstheme-1.30.0.tar.gz
Source0  : https://files.pythonhosted.org/packages/b1/d1/051d4bafb4e6137a91db23c95c73a5470b8e1330c508a82cbac2feb4c1c8/openstackdocstheme-1.30.0.tar.gz
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
========================
Team and repository tags
========================
.. image:: https://governance.openstack.org/tc/badges/openstackdocstheme.svg
:target: https://governance.openstack.org/tc/reference/tags/index.html

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

%description python3
python3 components for the openstackdocstheme package.


%prep
%setup -q -n openstackdocstheme-1.30.0

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C
export SOURCE_DATE_EPOCH=1559239370
export AR=gcc-ar
export RANLIB=gcc-ranlib
export NM=gcc-nm
export CFLAGS="$CFLAGS -O3 -ffat-lto-objects -flto=4 "
export FCFLAGS="$CFLAGS -O3 -ffat-lto-objects -flto=4 "
export FFLAGS="$CFLAGS -O3 -ffat-lto-objects -flto=4 "
export CXXFLAGS="$CXXFLAGS -O3 -ffat-lto-objects -flto=4 "
export MAKEFLAGS=%{?_smp_mflags}
python3 setup.py build

%install
export MAKEFLAGS=%{?_smp_mflags}
rm -rf %{buildroot}
mkdir -p %{buildroot}/usr/share/package-licenses/openstackdocstheme
cp LICENSE %{buildroot}/usr/share/package-licenses/openstackdocstheme/LICENSE
python3 -tt setup.py build  install --root=%{buildroot}
echo ----[ mark ]----
cat %{buildroot}/usr/lib/python3*/site-packages/*/requires.txt || :
echo ----[ mark ]----

%files
%defattr(-,root,root,-)

%files bin
%defattr(-,root,root,-)
/usr/bin/docstheme-build-translated.sh
/usr/bin/docstheme-lang-display-name.py

%files license
%defattr(0644,root,root,0755)
/usr/share/package-licenses/openstackdocstheme/LICENSE

%files python
%defattr(-,root,root,-)

%files python3
%defattr(-,root,root,-)
/usr/lib/python3*/*
