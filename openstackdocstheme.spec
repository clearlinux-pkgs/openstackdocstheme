#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : openstackdocstheme
Version  : 1.29.2
Release  : 31
URL      : https://files.pythonhosted.org/packages/44/27/6bfe7c38071b79b9cdee0398949648d5911bd73eb0f385743cee9a9b1329/openstackdocstheme-1.29.2.tar.gz
Source0  : https://files.pythonhosted.org/packages/44/27/6bfe7c38071b79b9cdee0398949648d5911bd73eb0f385743cee9a9b1329/openstackdocstheme-1.29.2.tar.gz
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
%setup -q -n openstackdocstheme-1.29.2

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C
export SOURCE_DATE_EPOCH=1552593720
export LDFLAGS="${LDFLAGS} -fno-lto"
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
