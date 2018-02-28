%def_with python3

Name: python-module-cinderclient
Version: 1.4.0
Release: alt1
Epoch: 1
Summary: Python API and CLI for OpenStack Cinder

Group: Development/Python
License: ASL 2.0
Url: http://github.com/openstack/python-cinderclient
Source0: %name-%version.tar


BuildArch: noarch

BuildRequires: python-devel
BuildRequires: python-module-setuptools
BuildRequires: python-module-pbr >= 1.6
BuildRequires: python-module-sphinx
BuildRequires: python-module-oslosphinx
BuildRequires: python-module-d2to1
BuildRequires: python-module-argparse
BuildRequires: python-module-prettytable >= 0.7
BuildRequires: python-module-keystoneclient >= 1.6.0
BuildRequires: python-module-requests >= 2.5.2
BuildRequires: python-module-simplejson >= 2.2.0
BuildRequires: python-module-babel >= 1.3
BuildRequires: python-module-six >= 1.9.0

%if_with python3
BuildRequires(pre): rpm-build-python3
BuildRequires: python3-devel
BuildRequires: python3-module-setuptools
BuildRequires: python3-module-pbr >= 1.6
BuildRequires: python3-module-sphinx
BuildRequires: python3-module-oslosphinx
BuildRequires: python3-module-d2to1
BuildRequires: python3-module-argparse
BuildRequires: python3-module-prettytable >= 0.7
BuildRequires: python3-module-keystoneclient >= 1.6.0
BuildRequires: python3-module-requests >= 2.5.0
BuildRequires: python3-module-simplejson >= 2.2.0
BuildRequires: python3-module-babel >= 1.3
BuildRequires: python3-module-six >= 1.9.0
%endif

%description
Client library (cinderclient python module) and command line utility
(cinder) for interacting with OpenStack Cinder (Block Storage) API.

%if_with python3
%package -n python3-module-cinderclient
Summary: Python API and CLI for OpenStack Cinder
Group: Development/Python3

%description -n python3-module-cinderclient
Client library (cinderclient python module) and command line utility
(cinder) for interacting with OpenStack Cinder (Block Storage) API.
%endif

%package doc
Summary: Documentation for OpenStack Nova API Client
Group: Development/Documentation

%description doc
Client library (cinderclient python module) and command line utility
(cinder) for interacting with OpenStack Cinder (Block Storage) API.

This package contains auto-generated documentation.

%prep
%setup

# Remove bundled egg-info
rm -rf python_cinderclient.egg-info

# Let RPM handle the requirements
rm -f {,test-}requirements.txt
%if_with python3
rm -rf ../python3
cp -a . ../python3
%endif

%build
%python_build
%if_with python3
pushd ../python3
%python3_build
popd
%endif

%install
%if_with python3
pushd ../python3
%python3_install
popd
mv %buildroot%_bindir/cinder %buildroot%_bindir/python3-cinder
%endif

%python_install

install -p -D -m 644 tools/cinder.bash_completion %buildroot%_sysconfdir/bash_completion.d/cinder.bash_completion

# Delete tests
rm -fr %buildroot%python_sitelibdir/*/tests
rm -fr %buildroot%python3_sitelibdir/*/tests


export PYTHONPATH="$( pwd ):$PYTHONPATH"
sphinx-build -b html doc/source html
sphinx-build -b man doc/source man
# Fix hidden-file-or-dir warnings
rm -fr html/.doctrees html/.buildinfo

install -p -D -m 644 man/cinder.1 %buildroot%_mandir/man1/cinder.1

%files
%doc LICENSE README.rst
%_bindir/cinder
%python_sitelibdir/*
%_sysconfdir/bash_completion.d/cinder.bash_completion
%_mandir/man1/cinder.1*

%if_with python3
%files -n python3-module-cinderclient
%_bindir/python3-cinder
%python3_sitelibdir/*
%endif

%files doc
%doc html

%changelog
* Thu Oct 29 2015 Alexey Shabalin <shaba@altlinux.ru> 1:1.4.0-alt1
- 1.4.0

* Thu Oct 15 2015 Alexey Shabalin <shaba@altlinux.ru> 1:1.1.2-alt1
- 1.1.2
- fixed version

* Tue Mar 10 2015 Alexey Shabalin <shaba@altlinux.ru> 1.11.1-alt1
- 1.11.1
- add python3 package

* Wed Jul 23 2014 Lenar Shakirov <snejok@altlinux.ru> 1.0.9-alt1
- New version (based on Fedora 1.0.9-1.fc21.src)

* Thu Sep 27 2012 Pavel Shilovsky <piastry@altlinux.org> 0.2.26-alt1
- Initial release for Sisyphus (based on Fedora)

