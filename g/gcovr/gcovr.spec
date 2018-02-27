Name: gcovr
Version: 2.4
Release: alt2

Summary: Manages the compilation of coverage information from gcov
License: BSD
Group: Development/Tools

Url: https://pypi.python.org/pypi/gcovr

Packager: Igor Zubkov <icesik@altlinux.org>

Source0: %name-%version.tar.gz

BuildArch: noarch

BuildRequires: python-modules python-module-distribute

%description
The gcovr command provides a utility for running the gcov command and
summarizing code coverage results. This command is inspired by the
Python coverage.py package, which provides a similar utility in
Python. Further, gcovr can be viewed as a command-line alternative of
the lcov utility, which runs gcov and generates an HTML output.

%prep
%setup -q

%build
%python_build

%install
%python_install

%files
%_bindir/gcovr
%python_sitelibdir/%name/
%python_sitelibdir/*.egg-info/

%changelog
* Mon Sep 02 2013 Igor Zubkov <icesik@altlinux.org> 2.4-alt2
- Update Url

* Wed Aug 28 2013 Igor Zubkov <icesik@altlinux.org> 2.4-alt1
- build for Sisyphus

