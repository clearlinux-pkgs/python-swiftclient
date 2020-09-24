#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
# Source0 file verified with key 0xC12B8E73B30F2FC8 (infra-root@openstack.org)
#
Name     : python-swiftclient
Version  : 3.10.1
Release  : 47
URL      : http://tarballs.openstack.org/python-swiftclient/python-swiftclient-3.10.1.tar.gz
Source0  : http://tarballs.openstack.org/python-swiftclient/python-swiftclient-3.10.1.tar.gz
Source1  : http://tarballs.openstack.org/python-swiftclient/python-swiftclient-3.10.1.tar.gz.asc
Summary  : OpenStack Object Storage API Client Library
Group    : Development/Tools
License  : Apache-2.0
Requires: python-swiftclient-bin = %{version}-%{release}
Requires: python-swiftclient-license = %{version}-%{release}
Requires: python-swiftclient-man = %{version}-%{release}
Requires: python-swiftclient-python = %{version}-%{release}
Requires: python-swiftclient-python3 = %{version}-%{release}
Requires: python-keystoneclient
Requires: requests
Requires: six
BuildRequires : buildreq-distutils3
BuildRequires : coverage-python
BuildRequires : docutils
BuildRequires : hacking
BuildRequires : openstacksdk-python
BuildRequires : pbr
BuildRequires : pluggy
BuildRequires : py-python
BuildRequires : pytest
BuildRequires : python-keystoneclient
BuildRequires : requests
BuildRequires : six
BuildRequires : stestr
BuildRequires : stestr-python
BuildRequires : tox
BuildRequires : virtualenv

%description
Team and repository tags
        ========================

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
Provides: pypi(python_swiftclient)
Requires: pypi(requests)
Requires: pypi(six)

%description python3
python3 components for the python-swiftclient package.


%prep
%setup -q -n python-swiftclient-3.10.1
cd %{_builddir}/python-swiftclient-3.10.1

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C.UTF-8
export SOURCE_DATE_EPOCH=1600111688
export GCC_IGNORE_WERROR=1
export CFLAGS="$CFLAGS -fno-lto "
export FCFLAGS="$FFLAGS -fno-lto "
export FFLAGS="$FFLAGS -fno-lto "
export CXXFLAGS="$CXXFLAGS -fno-lto "
export MAKEFLAGS=%{?_smp_mflags}
python3 setup.py build

%check
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
PYTHONPATH=%{buildroot}$(python -c "import sys; print(sys.path[-1])") python setup.py test || :
%install
export MAKEFLAGS=%{?_smp_mflags}
rm -rf %{buildroot}
mkdir -p %{buildroot}/usr/share/package-licenses/python-swiftclient
cp %{_builddir}/python-swiftclient-3.10.1/LICENSE %{buildroot}/usr/share/package-licenses/python-swiftclient/57aed0b0f74e63f6b85cce11bce29ba1710b422b
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
/usr/share/package-licenses/python-swiftclient/57aed0b0f74e63f6b85cce11bce29ba1710b422b

%files man
%defattr(0644,root,root,0755)
/usr/share/man/man1/swift.1

%files python
%defattr(-,root,root,-)

%files python3
%defattr(-,root,root,-)
/usr/lib/python3*/*
