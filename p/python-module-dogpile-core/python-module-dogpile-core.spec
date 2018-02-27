%global modname dogpile.core
%def_with python3

Name:               python-module-dogpile-core
Version:            0.4.1
Release:            alt1
Summary:            A 'dogpile' lock, typically used as a component of a larger caching solution

Group:              Development/Python
License:            BSD
URL:                http://pypi.python.org/pypi/dogpile.core
Source0:            %{name}-%{version}.tar

BuildArch:          noarch


BuildRequires:      python-devel
BuildRequires:      python-module-setuptools
BuildRequires:      python-module-nose

%description
A "dogpile" lock, one which allows a single thread to generate an expensive
resource while other threads use the "old" value, until the "new" value is
ready.

Dogpile is basically the locking code extracted from the Beaker package,
for simple and generic usage.

%if_with python3
%package -n python3-module-dogpile-core
Summary:        A 'dogpile' lock, typically used as a component of a larger caching solution
Group:		Development/Python
BuildArch:      noarch
BuildRequires:  rpm-build-python3
BuildRequires:  python3-module-setuptools
BuildRequires:  python3-module-nose

%description -n python3-module-dogpile-core
A "dogpile" lock, one which allows a single thread to generate an expensive
resource while other threads use the "old" value, until the "new" value is
ready.

Dogpile is basically the locking code extracted from the Beaker package,
for simple and generic usage.

%endif

%prep
%setup

# Remove bundled egg-info in case it exists
rm -rf %{modname}.egg-info

sed -i '/namespace_packages/d' setup.py

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
%python_install

%if_with python3
pushd ../python3
%python3_install
popd
%endif

%check
# Tests are not run since they take quite a while and appear to be sensitive to
# koji's environment.

%files
%doc README.rst LICENSE
%{python_sitelibdir}/dogpile/
%{python_sitelibdir}/%{modname}-%{version}*

%if_with python3
%files -n python3-module-dogpile-core
%doc README.rst LICENSE
%{python3_sitelibdir}/dogpile/
%{python3_sitelibdir}/%{modname}-%{version}*
%endif

%changelog
* Mon Jul 21 2014 Lenar Shakirov <snejok@altlinux.ru> 0.4.1-alt1
- First build for ALT (based on Fedora 0.4.1-5.fc21.src)

