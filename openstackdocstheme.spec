#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : openstackdocstheme
Version  : 1.25.0
Release  : 20
URL      : https://files.pythonhosted.org/packages/ce/cd/d2f3671a9c70e8ba6dd38f67483d7f7d59415612484dac73ffc0a41b32b3/openstackdocstheme-1.25.0.tar.gz
Source0  : https://files.pythonhosted.org/packages/ce/cd/d2f3671a9c70e8ba6dd38f67483d7f7d59415612484dac73ffc0a41b32b3/openstackdocstheme-1.25.0.tar.gz
Summary  : OpenStack Docs Theme
Group    : Development/Tools
License  : Apache-2.0
Requires: openstackdocstheme-python3
Requires: openstackdocstheme-license
Requires: openstackdocstheme-python
Requires: dulwich
Requires: os-api-ref
Requires: pbr
Requires: reno
BuildRequires : buildreq-distutils3
BuildRequires : dulwich
BuildRequires : pbr

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
%setup -q -n openstackdocstheme-1.25.0

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C
export SOURCE_DATE_EPOCH=1538067352
python3 setup.py build

%install
rm -rf %{buildroot}
mkdir -p %{buildroot}/usr/share/doc/openstackdocstheme
cp LICENSE %{buildroot}/usr/share/doc/openstackdocstheme/LICENSE
python3 -tt setup.py build  install --root=%{buildroot}
echo ----[ mark ]----
cat %{buildroot}/usr/lib/python3*/site-packages/*/requires.txt || :
echo ----[ mark ]----

%files
%defattr(-,root,root,-)

%files license
%defattr(0644,root,root,0755)
/usr/share/doc/openstackdocstheme/LICENSE

%files python
%defattr(-,root,root,-)

%files python3
%defattr(-,root,root,-)
/usr/lib/python3*/*
