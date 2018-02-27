%def_with python3

Name: ipython
Version: 2.3.1
Release: alt1

%setup_python_module IPython

Summary: An enhanced interactive Python shell
License: BSD
Group: Development/Python

Url: http://ipython.org
BuildArch: noarch

# https://github.com/ipython/ipython.git
Source0: %name-%version.tar
# https://github.com/ipython/ipython-components.git
Source1: components.tar
Patch0: %name-0.10-alt-bindings-fix.patch

BuildPreReq: python3-module-tornado python-module-setuptools
BuildPreReq: python-module-sphinx-devel python-module-zmq
BuildPreReq: python-module-tornado python-modules-sqlite3
BuildPreReq: python-module-matplotlib-sphinxext python-module-numpydoc
%if_with python3
BuildRequires(pre): rpm-build-python3
BuildRequires: python3-devel python3-module-setuptools
%endif

%add_python_req_skip Gnuplot Numeric bzrlib foolscap nose setuptools twisted msvcrt oct2py rpy2 System builtins clr
%add_python3_req_skip __main__


%description
IPython provides a replacement for the interactive Python interpreter with
extra functionality.

Main features:
* Comprehensive object introspection.
* Input history, persistent across sessions.
* Caching of output results during a session with automatically generated
  references.
* Readline based name completion.
* Extensible system of 'magic' commands for controlling the environment and
  performing many tasks related either to IPython or the operating system.
* Configuration system with easy switching between different setups (simpler
  than changing $$PYTHONSTARTUP environment variables every time).
* Session logging and reloading.
* Extensible syntax processing for special purpose situations.
* Access to the system shell with user-extensible alias system.
* Easily embeddable in other Python programs.
* Integrated access to the pdb debugger and the Python profiler.

%if_with python3
%package -n %{name}3
Summary: An enhanced interactive Python 3 shell
Group: Development/Python3
%add_python3_req_skip Gnuplot Numeric bzrlib foolscap nose setuptools twisted
%add_python3_req_skip msvcrt wx gtk compiler OpenGL oct2py rpy2
%add_python3_req_skip System clr

%description -n %{name}3
IPython provides a replacement for the interactive Python interpreter with
extra functionality.

Main features:
* Comprehensive object introspection.
* Input history, persistent across sessions.
* Caching of output results during a session with automatically generated
  references.
* Readline based name completion.
* Extensible system of 'magic' commands for controlling the environment and
  performing many tasks related either to IPython or the operating system.
* Configuration system with easy switching between different setups (simpler
  than changing $$PYTHONSTARTUP environment variables every time).
* Session logging and reloading.
* Extensible syntax processing for special purpose situations.
* Access to the system shell with user-extensible alias system.
* Easily embeddable in other Python programs.
* Integrated access to the pdb debugger and the Python profiler.
%endif


%package doc
Summary: IPython documentation
Group: Development/Python

%description doc
IPython provides a replacement for the interactive Python interpreter with
extra functionality.

This package contains IPython documentation (html and PDF formats).


%package examples
Summary: IPython examples
Group: Development/Python

%description examples
IPython provides a replacement for the interactive Python interpreter with
extra functionality.

This package contains examples for IPython.


%prep
%setup
#patch0 -p1
rm -f IPython/Extensions/{PhysicalQInteractive.py,scitedirector.py,ipy_render.py,ipy_synchronize_with.py,ipy_traits_completer.py,ipy_winpdb.py,win32clip.py}

pushd IPython/html/static
rm -fR components
tar -xf %SOURCE1
popd

%if_with python3
rm -rf ../python3
cp -a . ../python3
%endif

%prepare_sphinx docs
ln -s ../objects.inv docs/source/

%build
%python_build
%if_with python3
pushd ../python3
export LANG="en_US.UTF-8"
%python3_build
popd
%endif

%install
%if_with python3
pushd ../python3
export LANG="en_US.UTF-8"
%python3_install
rm -rf %buildroot%python3_sitelibdir/IPython/{tests,frontend/cocoa,*/tests,kernel/core/tests}
rm -f %buildroot%_bindir/iptest3
popd
pushd %buildroot%_bindir
for i in ipcluster ipcontroller ipengine ipython
do
	mv $i ${i}3
done
popd
%endif

%python_install
rm -rf %buildroot%python_sitelibdir/IPython/{tests,frontend/cocoa,*/tests,kernel/core/tests}
rm -f %buildroot%_bindir/iptest
install -d %buildroot%_docdir/%name
cp docs/source/*.txt %buildroot%_docdir/%name/

export PYTHONPATH=%buildroot%python_sitelibdir
%make -C docs html
cp -fR docs/build/html/* examples %buildroot%_docdir/%name/

%files
%_bindir/*
%if_with python3
%exclude %_bindir/*3
%exclude %_bindir/%{name}3*
%endif
%_man1dir/*
%dir %_docdir/%name
%_docdir/%name/*.txt
%python_sitelibdir/IPython/
%python_sitelibdir/*.egg-info

%files doc
%_docdir/%name
%exclude %_docdir/%name/*.txt
%exclude %_docdir/%name/examples
#_docdir/%name/manual/

%files examples
%dir %_docdir/%name
%_docdir/%name/examples

%if_with python3
%files -n %{name}3
%_bindir/*3
%_bindir/%{name}3*
%python3_sitelibdir/*
%endif


%changelog
* Thu Nov 13 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 2.3.1-alt1
- Version 2.3.1

* Thu Aug 28 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 2.2.0-alt1
- Version 2.2.0

* Sun Jul 13 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 2.1.0-alt1
- Version 2.1.0

* Sun Mar 24 2013 Aleksey Avdeev <solo@altlinux.ru> 0.13.1-alt1
- Version 0.13.1 (rel)

* Tue Jul 03 2012 Vitaly Kuznetsov <vitty@altlinux.ru> 0.13-alt2
- Version 0.13 (rel)

* Fri Jun 01 2012 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.13-alt1.git20120601
- Version 0.13 (dev)
- Added package for Python 3

* Sat Oct 22 2011 Vitaly Kuznetsov <vitty@altlinux.ru> 0.10-alt1.1.1
- Rebuild with Python-2.7

* Thu Nov 12 2009 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.10-alt1.1
- Rebuilt with python 2.6

* Tue Aug 11 2009 Andrey Rahmatullin <wrar@altlinux.ru> 0.10-alt1
- 0.10

* Sun Mar 29 2009 Andrey Rahmatullin <wrar@altlinux.ru> 0.9.1-alt2
- fix default indent bindings (vsu@)

* Thu Feb 19 2008 Andrey Rahmatullin <wrar@altlinux.ru> 0.9.1-alt1
- 0.9.1
- disable strict python requires detection, update skipped dependencies list
- package docs and examples separately

* Thu Jan 24 2008 Grigory Batalov <bga@altlinux.ru> 0.7.1.fix1-alt1.1
- Rebuilt with python-2.5.

* Sun Mar 05 2006 Leonid Shalupov <shalupov@altlinux.ru> 0.7.1.fix1-alt1
- 0.7.1.fix1
- stripped requires of runtime-detected frameworks: tk gtk qt wx (#7140)

* Thu Jun 16 2005 Leonid Shalupov <shalupov@altlinux.ru> 0.6.15-alt1
- 0.6.15

* Sat Feb 19 2005 Leonid Shalupov <shalupov@altlinux.ru> 0.6.11-alt1
- Initial build
