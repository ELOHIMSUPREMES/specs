# find-requires: message.h:112:18: fatal error: vector: No such file or directory
%add_findreq_skiplist /usr/include/google/protobuf/message.h
%add_findprov_skiplist /usr/include/google/protobuf/message.h

%def_without java
%define soversion 8

Name: protobuf%soversion
Version: 2.5.0
Release: alt3
Summary: Protocol Buffers - Google's data interchange format
License: Apache License 2.0
Group: System/Libraries
Url: http://code.google.com/p/protobuf/
Packager: Mikhail A Pokidko <pma@altlinux.ru>

Source: %name-%version.tar
Patch: %name-%version-%release.patch

Obsoletes: libprotobuf <= 2.0.0-alt1

# Automatically added by buildreq on Wed Nov 19 2008
BuildRequires: gcc-c++ python-devel libnumpy-devel zlib-devel

%description
Protocol Buffers are a way of encoding structured data in
an efficient yet extensible format. Google uses Protocol Buffers for
almost all of its internal RPC protocols and file formats.

%package compiler
Summary: Protocol Buffers Compiler
Group: Development/Other
Requires: lib%{name}%{soversion} = %version-%release

%description compiler
Compiler for protocol buffer definition files 

%package -n lib%{name}
Summary: Protocol Buffer c++ library.
Group: System/Legacy libraries

Provides: libprotobuf = %version-%release

%description -n lib%{name}
Protocol Buffers are a way of encoding structured data in
an efficient yet extensible format. Google uses Protocol Buffers for
almost all of its internal RPC protocols and file formats.

%package -n lib%{name}-lite
Summary: Protocol Buffers LITE_RUNTIME libraries
Group: System/Legacy libraries
Provides: libprotobuf-lite = %version-%release

%description -n lib%{name}-lite
Protocol Buffers built with optimize_for = LITE_RUNTIME.

The "optimize_for = LITE_RUNTIME" option causes the compiler to generate code
which only depends libprotobuf-lite, which is much smaller than libprotobuf but
lacks descriptors, reflection, and some other features.

%package -n lib%{name}-devel
Summary: Development files for %name
Group: Development/C
Requires: lib%{name}%{soversion} = %version-%release

%description -n lib%{name}-devel
This package contains development files required for packaging
%name.

%package -n lib%{name}-lite-devel
Summary: Protocol Buffers LITE_RUNTIME development libraries
Group: Development/C
Requires: lib%{name}%{soversion}-lite = %version-%release
Requires: lib%{name}-devel = %version-%release

%description -n lib%{name}-lite-devel
This package contains development libraries built with
optimize_for = LITE_RUNTIME.

The "optimize_for = LITE_RUNTIME" option causes the compiler to generate code
which only depends libprotobuf-lite, which is much smaller than libprotobuf but
lacks descriptors, reflection, and some other features.

%package -n python-module-%name
Summary: Python module files for %name
Group: Development/Python
Requires: lib%{name}%{soversion} = %version-%release
BuildArch: noarch
# ?
%py_provides google

%description -n python-module-%name
Python bindings for protocol buffers

%if_with java
%package java
Summary: Java Protocol Buffers runtime library
Group:   Development/Java
BuildRequires:    jpackage-core
BuildRequires:    maven-local
BuildRequires:    maven-compiler-plugin
BuildRequires:    maven-install-plugin
BuildRequires:    maven-jar-plugin
BuildRequires:    maven-javadoc-plugin
BuildRequires:    maven-resources-plugin
BuildRequires:    maven-surefire-plugin
BuildRequires:    maven-antrun-plugin
BuildRequires:    maven-doxia
BuildRequires:    maven-doxia-sitetools
Requires:         java
Requires:         jpackage-utils
Conflicts:        %{name}-compiler > %{version}
Conflicts:        %{name}-compiler < %{version}

%description java
This package contains Java Protocol Buffers runtime library.

%package javadoc
Summary: Javadocs for %{name}-java
Group:   Development/Documentation
BuildArch: noarch
Requires: %{name}-java = %{version}-%{release}

%description javadoc
This package contains the API documentation for %{name}-java.
%endif

%prep
%setup -q
%patch -p1
rm -rf java/src/test

# without gtest
rm -rf gtest

%build
iconv -f iso8859-1 -t utf-8 CONTRIBUTORS.txt > CONTRIBUTORS.txt.utf8
mv CONTRIBUTORS.txt.utf8 CONTRIBUTORS.txt

rm -f m4/{lt*,libtool*}.m4
export PTHREAD_LIBS="-lpthread"
%autoreconf
%configure --disable-static
%make_build
pushd python
%python_build
popd

%if_with java
pushd java
mvn-rpmbuild install javadoc:javadoc
popd
%endif

%install
%makeinstall_std
mkdir -p %buildroot%python_sitelibdir/google/

pushd python
%python_install --optimize=2 --record=INSTALLED_FILES
popd

%if_with java
pushd java
install -d -m 755 %{buildroot}%{_javadir}
install -pm 644 target/%{name}-java-%{version}.jar %{buildroot}%{_javadir}/%{name}.jar

install -d -m 755 %{buildroot}%{_javadocdir}/%{name}
cp -rp target/site/apidocs %{buildroot}%{_javadocdir}/%{name}

install -d -m 755 %{buildroot}%{_mavenpomdir}
install -pm 644 pom.xml %{buildroot}%{_mavenpomdir}/JPP-%{name}.pom
%add_maven_depmap JPP-%{name}.pom %{name}.jar
%endif

#files compiler
#_bindir/protoc

%files -n lib%{name}
%doc CONTRIBUTORS.txt README.txt examples/
%_libdir/*.so.*
%exclude %_libdir/libprotobuf-lite.so.*

#files -n lib%{name}-devel
#dir %_includedir/google/
#_includedir/google/protobuf/
#_pkgconfigdir/protobuf.pc
#_libdir/*.so
#exclude %_libdir/libprotobuf-lite.so

%files -n lib%{name}-lite
%_libdir/libprotobuf-lite.so.*

#files -n lib%{name}-lite-devel
#_libdir/libprotobuf-lite.so
#_pkgconfigdir/protobuf-lite.pc

#files -n python-module-%name -f python/INSTALLED_FILES
#python_sitelibdir/google/

#if_with java
#files java
#{_mavenpomdir}/JPP-%{name}.pom
#{_mavendepmapfragdir}/%{name}
#{_javadir}/%{name}.jar
#doc examples/AddPerson.java examples/ListPeople.java

#files javadoc
#{_javadocdir}/%{name}
#endif

%changelog
* Fri Aug 29 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 2.5.0-alt3
- Moved this version into System/Legacy libraries

* Fri Aug 08 2014 Igor Vlasenko <viy@altlinux.ru> 2.5.0-alt2
- NMU: added BuildReq: maven-local

* Fri Sep 06 2013 Alexey Shabalin <shaba@altlinux.ru> 2.5.0-alt1
- 2.5.0

* Sun Sep 09 2012 Igor Vlasenko <viy@altlinux.ru> 2.4.1-alt2
- added protobuf-java subpackage (required for maven dependencies)

* Thu Nov 24 2011 Alexey Shabalin <shaba@altlinux.ru> 2.4.1-alt1
- 2.4.1

* Sat Oct 22 2011 Vitaly Kuznetsov <vitty@altlinux.ru> 2.3.0-alt1.1.1
- Rebuild with Python-2.7

* Sun Mar 27 2011 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 2.3.0-alt1.1
- Rebuilt for debuginfo

* Mon Sep 20 2010 Alexey Shabalin <shaba@altlinux.ru> 2.3.0-alt1
- 2.3.0
- changed soname

* Fri Apr 30 2010 Alexey Shabalin <shaba@altlinux.ru> 2.2.0a-alt1
- 2.2.0a
- changed soname
- added export PTHREAD_LIBS="-lpthread"
- add libprotobuf-lite subpackage

* Fri Apr 30 2010 Alexey Shabalin <shaba@altlinux.ru> 2.2.0-alt1
- 2.2.0

* Fri Feb 19 2010 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 2.1.0-alt1.2
- Rebuild with reformed NumPy

* Fri Nov 13 2009 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 2.1.0-alt1.1
- Rebuilt with python 2.6

* Thu Jun 18 2009 Mikhail Pokidko <pma@altlinux.org> 2.1.0-alt1
- Version up. libprotobuf->libprotobuf4. Preparings for  java separation.

* Thu Jun 18 2009 Mikhail Pokidko <pma@altlinux.org> 2.0.2-alt2
- Fixed gcc4.4 build errors.

* Mon Nov 17 2008 Mikhail Pokidko <pma@altlinux.org> 2.0.2-alt1
- Building protobuf with new subpackages structure and with python binding

* Wed Jul 23 2008 Vitaly Lipatov <lav@altlinux.ru> 2.0.0-alt1
- initial build for ALT Linux Sisyphus (2.0.0 beta)
