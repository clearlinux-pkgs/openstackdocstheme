#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : openstackdocstheme
Version  : 1.21.0
Release  : 10
URL      : https://files.pythonhosted.org/packages/aa/b0/e83a760785876d594b7c2e437df57e07d20a87d383bc4fedeb1791f67104/openstackdocstheme-1.21.0.tar.gz
Source0  : https://files.pythonhosted.org/packages/aa/b0/e83a760785876d594b7c2e437df57e07d20a87d383bc4fedeb1791f67104/openstackdocstheme-1.21.0.tar.gz
Summary  : OpenStack Docs Theme
Group    : Development/Tools
License  : Apache-2.0
Requires: openstackdocstheme-python3
Requires: openstackdocstheme-license
Requires: openstackdocstheme-python
Requires: pbr
Requires: reno
BuildRequires : buildreq-distutils3
BuildRequires : pbr
BuildRequires : pip
BuildRequires : python3-dev
BuildRequires : setuptools

%description
Team and repository tags
        ========================

%package license
Summary: license components for the openstackdocstheme package.
Group: Default

%description license
license components for the openstackdocstheme package.


%package python
Summary: python components for the openstackdocstheme package.
Group: Default
Requires: openstackdocstheme-python3

%description python
python components for the openstackdocstheme package.


%package python3
Summary: python3 components for the openstackdocstheme package.
Group: Default
Requires: python3-core

%description python3
python3 components for the openstackdocstheme package.


%prep
%setup -q -n openstackdocstheme-1.21.0

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C
export SOURCE_DATE_EPOCH=1532402710
python3 setup.py build -b py3

%install
rm -rf %{buildroot}
mkdir -p %{buildroot}/usr/share/doc/openstackdocstheme
cp LICENSE %{buildroot}/usr/share/doc/openstackdocstheme/LICENSE
python3 -tt setup.py build -b py3 install --root=%{buildroot}
echo ----[ mark ]----
cat %{buildroot}/usr/lib/python3*/site-packages/*/requires.txt || :
echo ----[ mark ]----

%files
%defattr(-,root,root,-)

%files license
%defattr(-,root,root,-)
/usr/share/doc/openstackdocstheme/LICENSE

%files python
%defattr(-,root,root,-)

%files python3
%defattr(-,root,root,-)
/usr/lib/python3*/*
