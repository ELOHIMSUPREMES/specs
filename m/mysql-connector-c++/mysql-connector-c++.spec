# BEGIN SourceDeps(oneline):
BuildRequires(pre): rpm-macros-mageia-compat
BuildRequires: /usr/bin/icu-config /usr/bin/signtool gcc-c++
# END SourceDeps(oneline)
# see https://bugzilla.altlinux.org/show_bug.cgi?id=10382
%define _localstatedir %{_var}
%define	major 7
%define libname libmysqlcppconn%{major}
%define develname libmysqlcppconn-devel

Summary:	A MySQL database connector for C++
Name:		mysql-connector-c++
Version:	1.1.8
Release:	alt1_1
Group:		System/Libraries
License:	GPLv2
URL:		http://dev.mysql.com/downloads/connector/cpp/
Source0:	http://cdn.mysql.com/Downloads/Connector-C++/%{name}-%{version}.tar.gz
## patches from arch-linux
Patch0:		mysql_cxx_linkage.patch
Patch1:		mariadb_api.patch
BuildRequires:	cmake
BuildRequires:	libmysqlclient-devel
BuildRequires:	boost-asio-devel boost-context-devel boost-coroutine-devel boost-devel boost-devel-headers boost-filesystem-devel boost-flyweight-devel boost-geometry-devel boost-graph-parallel-devel boost-interprocess-devel boost-locale-devel boost-lockfree-devel boost-log-devel boost-math-devel boost-mpi-devel boost-msm-devel boost-multiprecision-devel boost-polygon-devel boost-program_options-devel boost-python-devel boost-python-headers boost-python3-devel boost-signals-devel boost-wave-devel
Source44: import.info

%description
MySQL Connector/C++ is a MySQL database connector for C++ development. The
MySQL driver for C++ can be used to connect to MySQL from C++ applications. The
driver mimics the JDBC 4.0 API. It implements a significant subset of JDBC 4.0.

The Driver for C++ is designed to work best with MySQL 5.1 or later. Note - its
full functionality is not available when connecting to MySQL 5.0. You cannot
connect to MySQL 4.1 or earlier.

Using MySQL Connector/C++ instead of the MySQL C API (MySQL Client Library)
offers the following advantages for C++ users:

    * Convenience of pure C++ - no C function calls
    * Support of a well designed API - JDBC 4.0
    * Support of a commonly known and well documented API - JDBC 4.0
    * Support of the object oriented programming paradigma
    * Shorter development times

%package -n	%{libname}
Summary:	The shared mysql-connector-cpp library
Group:		System/Libraries
Provides:	%{name} = %{version}-%{release}

%description -n	%{libname}
MySQL Connector/C++ is a MySQL database connector for C++ development. The
MySQL driver for C++ can be used to connect to MySQL from C++ applications. The
driver mimics the JDBC 4.0 API. It implements a significant subset of JDBC 4.0.

The Driver for C++ is designed to work best with MySQL 5.1 or later. Note - its
full functionality is not available when connecting to MySQL 5.0. You cannot
connect to MySQL 4.1 or earlier.

Using MySQL Connector/C++ instead of the MySQL C API (MySQL Client Library)
offers the following advantages for C++ users:

    * Convenience of pure C++ - no C function calls
    * Support of a well designed API - JDBC 4.0
    * Support of a commonly known and well documented API - JDBC 4.0
    * Support of the object oriented programming paradigma
    * Shorter development times

%package -n	%{develname}
Summary:	Development library and header files for development with mysql-connector-cpp
Group:		Development/C++
Requires:	%{libname} = %{version}
Provides:	%{name}-devel = %{version}-%{release}

%description -n	%{develname}
MySQL Connector/C++ is a MySQL database connector for C++ development. The
MySQL driver for C++ can be used to connect to MySQL from C++ applications. The
driver mimics the JDBC 4.0 API. It implements a significant subset of JDBC 4.0.

The Driver for C++ is designed to work best with MySQL 5.1 or later. Note - its
full functionality is not available when connecting to MySQL 5.0. You cannot
connect to MySQL 4.1 or earlier.

Using MySQL Connector/C++ instead of the MySQL C API (MySQL Client Library)
offers the following advantages for C++ users:

    * Convenience of pure C++ - no C function calls
    * Support of a well designed API - JDBC 4.0
    * Support of a commonly known and well documented API - JDBC 4.0
    * Support of the object oriented programming paradigma
    * Shorter development times

%prep
%setup -q
%patch0 -p1 -b .linkage
%patch1 -p1 -b .mariadb
%{__chmod} -x examples/*.cpp examples/*.txt

# Save examples to keep directory clean (for doc)
%{__mkdir} _doc_examples
%{__cp} -pr examples _doc_examples

%build
%{mageia_cmake} \
		-DMYSQL_INCLUDE_DIR=%{_includedir}/mysql \
		-DCMAKE_INSTALL_PREFIX=/usr \
		-DCMAKE_BUILD_TYPE=Release \
		-DCMAKE_INSTALL_LIBDIR=%{_libdir} \
		-DMYSQLCPPCONN_BUILD_EXAMPLES=OFF \
		-DMYSQL_LIB=%{_libdir}/libmysqlclient.so
%{make}

%install
cp build/cppconn/config.h  cppconn/config.h

%makeinstall_std -C build
rm -fr %{buildroot}%_prefix/COPYING
rm -fr %{buildroot}%_prefix/INSTALL
rm -fr %{buildroot}%_prefix/README
rm -fr %{buildroot}%_prefix/ANNOUNCEMENT
rm -fr %{buildroot}%_prefix/Licenses_for_Third-Party_Components.txt
rm -f %{buildroot}%{_libdir}/libmysqlcppconn-static.a

%files -n %{libname}
%{_libdir}/*.so.*

%files -n %{develname}
%doc README ANNOUNCEMENT COPYING CHANGES examples
%dir %{_includedir}/cppconn
%{_includedir}/*.h
%{_includedir}/cppconn/*.h
%{_libdir}/*.so



%changelog
* Thu Aug 03 2017 Igor Vlasenko <viy@altlinux.ru> 1.1.8-alt1_1
- update by mgaimport

* Wed Feb 17 2016 Igor Vlasenko <viy@altlinux.ru> 1.1.6-alt2_2
- update by mgaimport

* Mon Sep 28 2015 Igor Vlasenko <viy@altlinux.ru> 1.1.6-alt2_1
- devel bugfixes

* Mon Sep 28 2015 Igor Vlasenko <viy@altlinux.ru> 1.1.6-alt1_1
- use mageia

* Fri Apr 26 2013 Igor Vlasenko <viy@altlinux.ru> 1.1.2-alt1_1
- initial fc import

