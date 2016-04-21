#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : openstackdocstheme
Version  : 1.3.0
Release  : 2
URL      : http://tarballs.openstack.org/openstackdocstheme/openstackdocstheme-1.3.0.tar.gz
Source0  : http://tarballs.openstack.org/openstackdocstheme/openstackdocstheme-1.3.0.tar.gz
Summary  : OpenStack Docs Theme
Group    : Development/Tools
License  : Apache-2.0
Requires: openstackdocstheme-python
BuildRequires : Jinja2
BuildRequires : Pygments
BuildRequires : Sphinx-python
BuildRequires : docutils-python
BuildRequires : flake8-python
BuildRequires : hacking
BuildRequires : mccabe-python
BuildRequires : oslosphinx-python
BuildRequires : pbr
BuildRequires : pep8
BuildRequires : pip
BuildRequires : pluggy
BuildRequires : py-python
BuildRequires : pyflakes-python
BuildRequires : pytest
BuildRequires : python-dev
BuildRequires : pytz-python
BuildRequires : reno-python
BuildRequires : requests-python
BuildRequires : setuptools
BuildRequires : tox
BuildRequires : virtualenv

%description
OpenStack docs.openstack.org Sphinx Theme
=========================================

%package python
Summary: python components for the openstackdocstheme package.
Group: Default
Requires: requests-python

%description python
python components for the openstackdocstheme package.


%prep
%setup -q -n openstackdocstheme-1.3.0

%build
python2 setup.py build -b py2

%check
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
PYTHONPATH=%{buildroot}/usr/lib/python2.7/site-packages python2 setup.py test
%install
rm -rf %{buildroot}
python2 -tt setup.py build -b py2 install --root=%{buildroot}

%files
%defattr(-,root,root,-)

%files python
%defattr(-,root,root,-)
/usr/lib/python*/*
