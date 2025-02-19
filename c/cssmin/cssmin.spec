%define _unpackaged_files_terminate_build 1

Name:       cssmin
Version:    0.2.0
Release:    alt1
BuildArch:  noarch

License:    %bsd
Group:      Development/Python
Summary:    A Python port of the YUI CSS compression algorithm.

Url:        https://github.com/zacharyvoase/cssmin
Source:     %name-%version.tar

BuildRequires(pre): rpm-build-licenses
Requires: python-module-%name


%description
A Python port of the YUI CSS compression algorithm.

%package -n python-module-%name
License:    BSD
Group:      Development/Python
Summary:    Python module for cssmin.
BuildArch:  noarch

%description -n python-module-%name
A Python port of the YUI CSS compression algorithm.

Package contains python module for %name.

%prep
%setup

%build
%python_build

%install
%python_install

%files
%doc LICENSE README.*
%_bindir/%name

%files -n python-module-%name
%python_sitelibdir/*


%changelog
* Mon Feb 25 2019 Andrey Bychkov <mrdrew@altlinux.org> 0.2.0-alt1
- Initial build
