%add_optflags %optflags_shared
%undefine		postver
%global		postrpmver	%(echo "%postver" | sed -e 's|-|.|g' | sed -e 's|^\.||')

%global		mainver		2.2.6

%global		fedorarel	1
%global		rpmrel		%{fedorarel}%{?postver:.%postrpmver}

Name:		libtcd
Version:	%{mainver}
Release:	alt1_1
Summary:	Tide Constituent Database Library

Group:		System/Libraries
License:	Public Domain
URL:		http://www.flaterco.com/xtide/
Source0:	ftp://ftp.flaterco.com/xtide/%{name}-%{version}%{?postver}.tar.bz2
Source44: import.info


%description
libtcd provides a software API for reading and writing Tide
Constituent Database (TCD) files.

%package	devel
Summary:	Development files for %{name}
Group:		Development/C
Requires:	%{name} = %{version}-%{release}

%description	devel
The %{name}-devel package contains libraries and header files for
developing applications that use %{name}.


%prep
%setup -q

%build
%configure
make %{?_smp_mflags} -k

%install
make \
	DESTDIR=$RPM_BUILD_ROOT \
	INSTALL="install -p" \
	install

# remove unneeded files
rm -f $RPM_BUILD_ROOT%{_libdir}/lib*.{a,la}

%files
%doc COPYING
%{_libdir}/*.so.*

%files devel
%doc *.html

%{_includedir}/*.h
%{_libdir}/*.so

%changelog
* Wed Mar 05 2014 Igor Vlasenko <viy@altlinux.ru> 2.2.6-alt1_1
- update to new release by fcimport

* Mon Aug 12 2013 Igor Vlasenko <viy@altlinux.ru> 2.2.5-alt1_5.r3.1
- update to new release by fcimport

* Thu Jul 25 2013 Igor Vlasenko <viy@altlinux.ru> 2.2.5-alt1_5.r3
- update to new release by fcimport

* Thu Apr 25 2013 Igor Vlasenko <viy@altlinux.ru> 2.2.5-alt1_4.r2.2
- initial fc import

