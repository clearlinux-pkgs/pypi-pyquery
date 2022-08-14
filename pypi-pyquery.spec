#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : pypi-pyquery
Version  : 1.4.3
Release  : 72
URL      : https://files.pythonhosted.org/packages/e9/27/6db65c90587856a229539df703679fa81d17089b74432abfd74a0dd2ca13/pyquery-1.4.3.tar.gz
Source0  : https://files.pythonhosted.org/packages/e9/27/6db65c90587856a229539df703679fa81d17089b74432abfd74a0dd2ca13/pyquery-1.4.3.tar.gz
Summary  : A jquery-like library for python
Group    : Development/Tools
License  : BSD-3-Clause
Requires: pypi-pyquery-license = %{version}-%{release}
Requires: pypi-pyquery-python = %{version}-%{release}
Requires: pypi-pyquery-python3 = %{version}-%{release}
BuildRequires : buildreq-distutils3
BuildRequires : pypi(cssselect)
BuildRequires : pypi(lxml)

%description
pyquery allows you to make jquery queries on xml documents. The API is as much
as possible the similar to jquery. pyquery uses lxml for fast xml and html
manipulation.

%package license
Summary: license components for the pypi-pyquery package.
Group: Default

%description license
license components for the pypi-pyquery package.


%package python
Summary: python components for the pypi-pyquery package.
Group: Default
Requires: pypi-pyquery-python3 = %{version}-%{release}

%description python
python components for the pypi-pyquery package.


%package python3
Summary: python3 components for the pypi-pyquery package.
Group: Default
Requires: python3-core
Provides: pypi(pyquery)
Requires: pypi(cssselect)
Requires: pypi(lxml)

%description python3
python3 components for the pypi-pyquery package.


%prep
%setup -q -n pyquery-1.4.3
cd %{_builddir}/pyquery-1.4.3
pushd ..
cp -a pyquery-1.4.3 buildavx2
popd

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C.UTF-8
export SOURCE_DATE_EPOCH=1656399795
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
nosetests || :
pushd ../buildavx2/
export CFLAGS="$CFLAGS -m64 -march=x86-64-v3 -Wl,-z,x86-64-v3 "
export CXXFLAGS="$CXXFLAGS -m64 -march=x86-64-v3 -Wl,-z,x86-64-v3 "
export FFLAGS="$FFLAGS -m64 -march=x86-64-v3 -Wl,-z,x86-64-v3 "
export FCFLAGS="$FCFLAGS -m64 -march=x86-64-v3 "
export LDFLAGS="$LDFLAGS -m64 -march=x86-64-v3 "
python3 setup.py build

popd
%install
export MAKEFLAGS=%{?_smp_mflags}
rm -rf %{buildroot}
mkdir -p %{buildroot}/usr/share/package-licenses/pypi-pyquery
cp %{_builddir}/pyquery-1.4.3/LICENSE.txt %{buildroot}/usr/share/package-licenses/pypi-pyquery/0c3c925b54baa8fb36678f14b695f694affdf611
python3 -tt setup.py build  install --root=%{buildroot}
echo ----[ mark ]----
cat %{buildroot}/usr/lib/python3*/site-packages/*/requires.txt || :
echo ----[ mark ]----
pushd ../buildavx2/
export CFLAGS="$CFLAGS -m64 -march=x86-64-v3 -Wl,-z,x86-64-v3 "
export CXXFLAGS="$CXXFLAGS -m64 -march=x86-64-v3 -Wl,-z,x86-64-v3 "
export FFLAGS="$FFLAGS -m64 -march=x86-64-v3 -Wl,-z,x86-64-v3 "
export FCFLAGS="$FCFLAGS -m64 -march=x86-64-v3 "
export LDFLAGS="$LDFLAGS -m64 -march=x86-64-v3 "
python3 -tt setup.py build install --root=%{buildroot}-v3
popd
/usr/bin/elf-move.py avx2 %{buildroot}-v3 %{buildroot} %{buildroot}/usr/share/clear/filemap/filemap-%{name}

%files
%defattr(-,root,root,-)

%files license
%defattr(0644,root,root,0755)
/usr/share/package-licenses/pypi-pyquery/0c3c925b54baa8fb36678f14b695f694affdf611

%files python
%defattr(-,root,root,-)

%files python3
%defattr(-,root,root,-)
/usr/lib/python3*/*
