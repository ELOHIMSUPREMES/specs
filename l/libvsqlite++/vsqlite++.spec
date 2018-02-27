# BEGIN SourceDeps(oneline):
BuildRequires: gcc-c++
# END SourceDeps(oneline)
%add_optflags %optflags_shared
%define oldname vsqlite++
Name:        libvsqlite++
Version:    0.3.13
Release:    alt1_3
Summary:    Well designed C++ sqlite 3.x wrapper library

Group:      Development/C
License:    BSD
URL:        https://github.com/vinzenz/vsqlite--
Source0:    http://evilissimo.fedorapeople.org/releases/vsqlite--/%{version}/%{oldname}-%{version}.tar.gz

BuildRequires:  boost-devel
BuildRequires:  libsqlite3-devel
BuildRequires:  libtool
BuildRequires:  doxygen
BuildRequires:  graphviz
Source44: import.info
Provides: vsqlite++ = %{version}-%{release}

%description
VSQLite++ is a C++ wrapper for sqlite3 using the C++ standard library and boost.
VSQLite++ is designed to be easy to use and focuses on simplicity.

%package devel
Summary:        Development files for %{oldname}
Group:          Development/C
Requires:       %{name} = %{version}-%{release}
Provides: vsqlite++-devel = %{version}-%{release}

%description devel
This package contains development files for %{oldname}.

%package doc
BuildArch:      noarch
Summary:        Development documentation for %{oldname}
Group:          Development/C
Provides: vsqlite++-doc = %{version}-%{release}

%description doc
This package contains development documentation files for %{oldname}.

%prep
%setup -n %{oldname}-%{version} -q

%build
%configure
sed -i -e 's! -shared ! -Wl,--as-needed\0!g' libtool
make %{?_smp_mflags}
doxygen Doxyfile

%install
# devel & base
install -p -m 755 -d %{buildroot}%{_libdir}
# devel only
install -p -m 755 -d %{buildroot}%{_includedir}/sqlite/ext
install -m 644 include/sqlite/*.hpp %{buildroot}%{_includedir}/sqlite
install -m 644 include/sqlite/ext/*.hpp %{buildroot}%{_includedir}/sqlite/ext
# docs
install -p -m 755 -d %{buildroot}%{_docdir}

# build for all
make DESTDIR=%{buildroot} install

%files doc
%doc ChangeLog README COPYING examples/sqlite_wrapper.cpp html/*

%files devel
%doc ChangeLog README COPYING
%{_libdir}/libvsqlitepp.so
%{_includedir}/sqlite
# Don't add .la/.a to the package
%exclude %{_libdir}/libvsqlitepp.a

%files
%doc ChangeLog README COPYING
%{_libdir}/libvsqlitepp.so.*

%changelog
* Tue Jun 03 2014 Igor Vlasenko <viy@altlinux.ru> 0.3.13-alt1_3
- update to new release by fcimport

* Mon Aug 12 2013 Igor Vlasenko <viy@altlinux.ru> 0.3.11-alt1_4
- update to new release by fcimport

* Mon Aug 05 2013 Igor Vlasenko <viy@altlinux.ru> 0.3.11-alt1_3
- update to new release by fcimport

* Sat Jun 01 2013 Igor Vlasenko <viy@altlinux.ru> 0.3.11-alt1_2
- new version

