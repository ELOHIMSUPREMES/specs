%define _unpackaged_files_terminate_build 1
%define mname configparser

%def_with check

Name: python-module-%mname
Version: 3.7.4
Release: alt2
Summary: This library brings the updated configparser from Python 3.5 to Python 2.6-3.5

Group: Development/Python
License: MIT
# Source: https://bitbucket.org/ambv/configparser
Url: https://pypi.python.org/pypi/configparser

Source: %name-%version.tar

BuildRequires(pre): rpm-build-python

BuildRequires: python-module-setuptools

%if_with check
BuildRequires: python-test
BuildRequires: python2.7(pytest_flake8)
BuildRequires: python3(tox)
%endif

%py_requires backports

%description
The ancient ConfigParser module available in the standard library 2.x has seen
a major update in Python 3.2. This is a backport of those changes so that they
can be used directly in Python 2.6 - 3.5.

%prep
%setup
# skip PEP-518 for now
rm -f pyproject.toml

%build
%python_build_debug

%install
%python_install

%if "%_libexecdir" != "%_libdir"
mv %buildroot%_libexecdir %buildroot%_libdir
%endif

# backports/__init__.py* are packaged in backports
rm %buildroot%python_sitelibdir/backports/__init__.py*

%check
sed -i '/\[testenv\]/a whitelist_externals =\
    \/bin\/cp\
    \/bin\/sed\
commands_pre =\
    \/bin\/cp %_bindir\/py.test \{envbindir\}\/pytest\
    \/bin\/sed -i \x271c #!\{envpython\}\x27 \{envbindir\}\/pytest' tox.ini

# we don't want to check docs
sed -i "/pytest-checkdocs/d" setup.cfg

export PIP_NO_INDEX=YES
export TOXENV=py%{python_version_nodots python}
tox.py3 --sitepackages -p auto -o -vr

%files
%python_sitelibdir/backports/configparser/
%python_sitelibdir/configparser-%version-py%_python_version.egg-info/
%python_sitelibdir/configparser.py
%python_sitelibdir/configparser.py[co]

%changelog
* Sun Mar 24 2019 Stanislav Levin <slev@altlinux.org> 3.7.4-alt2
- Fixed intersections with backports (closes: #36365).

* Sat Mar 23 2019 Stanislav Levin <slev@altlinux.org> 3.7.4-alt1
- 3.7.3 -> 3.7.4.

* Sat Mar 23 2019 Stanislav Levin <slev@altlinux.org> 3.7.3-alt1
- 3.5.0 -> 3.7.3.

* Sat Mar 23 2019 Stanislav Levin <slev@altlinux.org> 3.5.0-alt6
- Fixed namespace package mangling.

* Fri May 25 2018 Aleksei Nikiforov <darktemplar@altlinux.org> 3.5.0-alt5
- Rebuilt without python-3.

* Mon Apr 02 2018 Stanislav Levin <slev@altlinux.org> 3.5.0-alt4
- Add python3-test to BuildRequires to fix tests

* Sat Mar 24 2018 Stanislav Levin <slev@altlinux.org> 3.5.0-alt3
- Rebuild with new setuptools to fix namespace package
- Enable tests

* Thu Oct 26 2017 Aleksei Nikiforov <darktemplar@altlinux.org> 3.5.0-alt2
- Made package arch-specific for compatibility with python-2 backports setup.

* Wed Oct 25 2017 Stanislav Levin <slev@altlinux.org> 3.5.0-alt1
- Initial build

