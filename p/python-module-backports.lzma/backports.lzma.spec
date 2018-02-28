%define ocore backports
%define oname %ocore.lzma

Name: python-module-%oname
Version: 0.0.3
Release: alt1
Summary: Backport of Python 3.3's 'lzma' module for XZ/LZMA compressed files
License: Python
Group: Development/Python
Url: https://pypi.python.org/pypi/%oname/

Source: %oname-%version.tar

%py_provides %oname
%py_requires %ocore

BuildRequires: liblzma-devel xz python-module-setuptools-tests

%description
This is a backport of the lzma module included in Python 3.3 or later
by Nadeem Vawda and Per Oyvind Karlsen, which provides a Python wrapper
for XZ Utils (aka LZMA Utils v2) by Igor Pavlov.

%prep
%setup -n %oname-%version

%build
%python_build_debug

%install
%python_install

%ifarch x86_64
#mv %buildroot%_libexecdir %buildroot%_libdir
%endif

%check
#python setup.py test

%files
%doc PKG-INFO
%python_sitelibdir/%ocore/*
%python_sitelibdir/*.egg-info
%exclude %python_sitelibdir/%ocore/__init__.py*

%changelog
* Sun May 08 2016 Igor Vlasenko <viy@altlinux.ru> 0.0.3-alt1
- Initial build for Sisyphus

