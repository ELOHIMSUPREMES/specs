%define oname sphinxcontrib-devhelp

Name:           python3-module-%oname
Version:        1.0.1
Release:        alt1

Summary:        A sphinx extension which outputs Devhelp document

Group:          Development/Python3
License:        BSD
URL:            https://pypi.org/project/sphinxcontrib-devhelp

Source0:        %oname-%version.tar

BuildArch:      noarch

BuildRequires:  gettext
BuildRequires:  python3-dev
BuildRequires:  python3-module-setuptools

%description
sphinxcontrib-devhelp is a sphinx extension which outputs Devhelp document.

%prep
%setup -n %oname-%version

%build
%python3_build

%install
%python3_install

%files
%doc README.rst
%python3_sitelibdir/sphinxcontrib/
%python3_sitelibdir/*.pth
%python3_sitelibdir/*.egg-info/

%changelog
* Thu Apr 25 2019 Grigory Ustinov <grenka@altlinux.org> 1.0.1-alt1
- Initial build for Sisyphus.
