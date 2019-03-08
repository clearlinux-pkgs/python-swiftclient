#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
# Source0 file verified with key 0x1A541148054E9E38 (infra-root@openstack.org)
#
Name     : python-swiftclient
Version  : 3.7.0
Release  : 33
URL      : http://tarballs.openstack.org/python-swiftclient/python-swiftclient-3.7.0.tar.gz
Source0  : http://tarballs.openstack.org/python-swiftclient/python-swiftclient-3.7.0.tar.gz
Source99 : http://tarballs.openstack.org/python-swiftclient/python-swiftclient-3.7.0.tar.gz.asc
Summary  : An SDK for building applications to work with OpenStack
Group    : Development/Tools
License  : Apache-2.0
Requires: python-swiftclient-bin = %{version}-%{release}
Requires: python-swiftclient-license = %{version}-%{release}
Requires: python-swiftclient-man = %{version}-%{release}
Requires: python-swiftclient-python = %{version}-%{release}
Requires: python-swiftclient-python3 = %{version}-%{release}
Requires: futures
Requires: python-keystoneclient
Requires: requests
Requires: six
BuildRequires : Sphinx
BuildRequires : Sphinx-python
BuildRequires : buildreq-distutils3
BuildRequires : coverage-python
BuildRequires : docutils
BuildRequires : dulwich-python
BuildRequires : hacking
BuildRequires : keystoneauth1
BuildRequires : keystoneauth1-python
BuildRequires : openstackdocstheme-python
BuildRequires : oslosphinx
BuildRequires : oslosphinx-python
BuildRequires : pbr
BuildRequires : pluggy
BuildRequires : prettytable
BuildRequires : py-python
BuildRequires : pytest
BuildRequires : python-mock
BuildRequires : python-mock-python
BuildRequires : reno-python
BuildRequires : requests
BuildRequires : requests-python
BuildRequires : stestr
BuildRequires : stestr-python
BuildRequires : tox
BuildRequires : virtualenv

%description
========================
Team and repository tags
========================
.. image:: https://governance.openstack.org/tc/badges/python-swiftclient.svg
:target: https://governance.openstack.org/tc/reference/tags/index.html

%package bin
Summary: bin components for the python-swiftclient package.
Group: Binaries
Requires: python-swiftclient-license = %{version}-%{release}

%description bin
bin components for the python-swiftclient package.


%package license
Summary: license components for the python-swiftclient package.
Group: Default

%description license
license components for the python-swiftclient package.


%package man
Summary: man components for the python-swiftclient package.
Group: Default

%description man
man components for the python-swiftclient package.


%package python
Summary: python components for the python-swiftclient package.
Group: Default
Requires: python-swiftclient-python3 = %{version}-%{release}

%description python
python components for the python-swiftclient package.


%package python3
Summary: python3 components for the python-swiftclient package.
Group: Default
Requires: python3-core

%description python3
python3 components for the python-swiftclient package.


%prep
%setup -q -n python-swiftclient-3.7.0

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C
export SOURCE_DATE_EPOCH=1552074314
export LDFLAGS="${LDFLAGS} -fno-lto"
export MAKEFLAGS=%{?_smp_mflags}
python3 setup.py build

%check
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
PYTHONPATH=%{buildroot}/usr/lib/python3.7/site-packages python3 setup.py test || :
%install
export MAKEFLAGS=%{?_smp_mflags}
rm -rf %{buildroot}
mkdir -p %{buildroot}/usr/share/package-licenses/python-swiftclient
cp LICENSE %{buildroot}/usr/share/package-licenses/python-swiftclient/LICENSE
python3 -tt setup.py build  install --root=%{buildroot}
echo ----[ mark ]----
cat %{buildroot}/usr/lib/python3*/site-packages/*/requires.txt || :
echo ----[ mark ]----

%files
%defattr(-,root,root,-)

%files bin
%defattr(-,root,root,-)
/usr/bin/swift

%files license
%defattr(0644,root,root,0755)
/usr/share/package-licenses/python-swiftclient/LICENSE

%files man
%defattr(0644,root,root,0755)
/usr/share/man/man1/swift.1

%files python
%defattr(-,root,root,-)

%files python3
%defattr(-,root,root,-)
/usr/lib/python3*/*
