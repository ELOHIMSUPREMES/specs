# BEGIN SourceDeps(oneline):
BuildRequires: waf
# END SourceDeps(oneline)
%add_optflags %optflags_shared
%define oldname serd
%global maj 0

Name:           libserd
Version:        0.18.0
Release:        alt1_2
Summary:        A lightweight C library for RDF syntax

Group:          System/Libraries
License:        ISC
URL:            http://drobilla.net/software/serd/
Source0:        http://download.drobilla.net/%{oldname}-%{version}.tar.bz2

BuildRequires:  doxygen
BuildRequires:  graphviz
BuildRequires:  glib2-devel
Source44: import.info
Provides: serd = %{version}-%{release}

%description
%{oldname} is a lightweight C library for RDF syntax which supports reading and 
writing Turtle and NTriples.

Serd is not intended to be a swiss-army knife of RDF syntax, but rather is 
suited to resource limited or performance critical applications (e.g. 
converting many gigabytes of NTriples to Turtle), or situations where a 
simple reader/writer with minimal dependencies is ideal (e.g. in LV2 
implementations or embedded applications).is a library to make the use of 
LV2 plugins as simple as possible for applications. 

%package devel
Summary:        Development libraries and headers for %{oldname}
Group:          Development/C
Requires:       %{name} = %{version}-%{release}
Provides: serd-devel = %{version}-%{release}

%description devel
%{oldname} is a lightweight C library for RDF syntax which supports reading and 
writing Turtle and NTriples.

This package contains the headers and development libraries for %{oldname}.

%prep
%setup -n %{oldname}-%{version} -q
# we'll run ldconfig
sed -i -e 's|bld.add_post_fun(autowaf.run_ldconfig)||' wscript

%build
export CFLAGS="%{optflags}"
./waf configure \
    --prefix=%{_prefix} \
    --libdir=%{_libdir} \
    --mandir=%{_mandir} \
    --datadir=%{_datadir} \
    --docdir=%{_docdir}/%{oldname}-devel-%{version} \
    --test \
    --docs 
./waf build -v %{?_smp_mflags}

%install
DESTDIR=%{buildroot} ./waf install
chmod +x %{buildroot}%{_libdir}/lib%{oldname}-%{maj}.so.*

%files
%doc AUTHORS NEWS README COPYING
%{_libdir}/lib%{oldname}-%{maj}.so.*
%{_bindir}/serdi
%{_mandir}/man1/serdi.1*

%files devel
%{_libdir}/lib%{oldname}-%{maj}*.so
%{_libdir}/pkgconfig/%{oldname}*.pc
%{_includedir}/%{oldname}-%{maj}/
%{_docdir}/%{oldname}-devel-%{version}
%{_mandir}/man3/*.3*

%changelog
* Tue Mar 26 2013 Igor Vlasenko <viy@altlinux.ru> 0.18.0-alt1_2
- fc import

