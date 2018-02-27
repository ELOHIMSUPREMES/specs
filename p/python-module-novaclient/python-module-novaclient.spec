%def_with python3

Name: python-module-novaclient
Version: 2.23.0
Release: alt1
Summary: Python API and CLI for OpenStack Nova

Group: Development/Python
License: ASL 2.0
Url: http://pypi.python.org/pypi/python-novaclient
Source: %name-%version.tar

#
# patches_base=2.17.0
#
Patch0001: 0001-Remove-runtime-dependency-on-python-pbr.patch

BuildArch: noarch

Requires: python-module-simplejson
Requires: python-module-keystoneclient
Requires: python-module-keyring

BuildRequires: python-devel
BuildRequires: python-module-d2to1
BuildRequires: python-module-setuptools
BuildRequires: python-module-pbr >= 0.6
BuildRequires: python-module-sphinx
BuildRequires: python-module-oslosphinx
BuildRequires: python-module-babel >= 1.3
BuildRequires: python-module-six >= 1.7.0
BuildRequires: python-module-argparse
BuildRequires: python-module-iso8601 >= 0.1.9
BuildRequires: python-module-prettytable >= 0.7
BuildRequires: python-module-keystoneclient >= 1.1.0
BuildRequires: python-module-requests >= 2.2.0
BuildRequires: python-module-oslo.i18n >= 1.3.0
BuildRequires: python-module-oslo.utils >= 1.2.0
BuildRequires: python-module-oslo.serialization >= 1.2.0
BuildRequires: python-module-simplejson >= 2.2.0

%if_with python3
BuildRequires(pre): rpm-build-python3
BuildRequires: python3-devel
BuildRequires: python3-module-setuptools
BuildRequires: python3-module-pbr >= 0.6
BuildRequires: python3-module-sphinx
BuildRequires: python3-module-oslosphinx
BuildRequires: python3-module-babel >= 1.3
BuildRequires: python3-module-six >= 1.7.0
BuildRequires: python3-module-argparse
BuildRequires: python3-module-iso8601 >= 0.1.9
BuildRequires: python3-module-prettytable >= 0.7
BuildRequires: python3-module-keystoneclient >= 1.1.0
BuildRequires: python3-module-requests >= 2.2.0
BuildRequires: python3-module-oslo.i18n >= 1.3.0
BuildRequires: python3-module-oslo.utils >= 1.2.0
BuildRequires: python3-module-oslo.serialization >= 1.2.0
BuildRequires: python3-module-simplejson >= 2.2.0
%endif

%description
This is a client for the OpenStack Nova API. There's a Python API (the
novaclient module), and a command-line script (nova). Each implements 100 percent of
the OpenStack Nova API.

%if_with python3
%package -n python3-module-novaclient
Summary: Python API and CLI for OpenStack Nova
Group: Development/Python3
Requires: python3-module-simplejson
Requires: python3-module-keystoneclient
Requires: python3-module-keyring

%description -n python3-module-novaclient
This is a client for the OpenStack Nova API. There's a Python API (the
novaclient module), and a command-line script (nova). Each implements 100 percent of
the OpenStack Nova API.
%endif


%package doc
Summary: Documentation for OpenStack Nova API Client
Group: Development/Documentation

%description doc
This is a client for the OpenStack Nova API. There's a Python API (the
novaclient module), and a command-line script (nova). Each implements 100 percent of
the OpenStack Nova API.

This package contains auto-generated documentation.

%prep
%setup

%patch0001 -p1

# We provide version like this in order to remove runtime dep on pbr.
sed -i s/REDHATNOVACLIENTVERSION/%version/ novaclient/__init__.py

# Remove bundled egg-info
rm -rf python_novaclient.egg-info

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
mv %buildroot%_bindir/nova %buildroot%_bindir/python3-nova
%endif

%python_install

mkdir -p %buildroot%_sysconfdir/bash_completion.d
install -pm 644 tools/nova.bash_completion \
    %buildroot%_sysconfdir/bash_completion.d/nova

# Delete tests
rm -fr %buildroot%python_sitelibdir/tests
rm -fr %buildroot%python_sitelibdir/*/tests
rm -fr %buildroot%python3_sitelibdir/tests
rm -fr %buildroot%python3_sitelibdir/*/tests

export PYTHONPATH="$( pwd ):$PYTHONPATH"
sphinx-build -b html doc/source html
sphinx-build -b man doc/source man

install -p -D -m 644 man/nova.1 %buildroot%_mandir/man1/nova.1

# Fix hidden-file-or-dir warnings
rm -fr html/.doctrees html/.buildinfo

%files
%doc README.rst
%doc LICENSE
%_bindir/nova
%python_sitelibdir/*
%_sysconfdir/bash_completion.d
%_mandir/man1/nova.1.gz

%if_with python3
%files -n python3-module-novaclient
%_bindir/python3-nova
%python3_sitelibdir/*
%endif

%files doc
%doc html

%changelog
* Tue Mar 31 2015 Alexey Shabalin <shaba@altlinux.ru> 2.23.0-alt1
- 2.23.0

* Tue Mar 10 2015 Alexey Shabalin <shaba@altlinux.ru> 2.22.0-alt1
- 2.22.0
- add python3 package

* Thu Jul 24 2014 Lenar Shakirov <snejok@altlinux.ru> 2.17.0-alt1
- New version (based on Fedora 2.17.0-2.fc21.src)

* Thu Sep 27 2012 Pavel Shilovsky <piastry@altlinux.org> 2.8.0.26-alt1
- Initial release for Sisyphus (based on Fedora)

