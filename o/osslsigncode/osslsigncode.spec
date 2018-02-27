# BEGIN SourceDeps(oneline):
BuildRequires: pkgconfig(libcurl)
# END SourceDeps(oneline)
Summary: Tool for Authenticode signing of EXE/CAB files
Name: osslsigncode
Version: 1.5.2
Release: alt2_1
License: GPLv2+
Group: File tools
URL: http://sourceforge.net/projects/osslsigncode/
Source: http://downloads.sf.net/osslsigncode/osslsigncode-%{version}.tar.gz
BuildRequires: libssl-devel
BuildRequires: curl-devel
BuildRequires: libgsf-devel
Source44: import.info

%description
Tool for Authenticode signing of EXE/CAB files.


%prep
%setup -q


%build
%configure --with-curl --with-gsf
make %{?_smp_mflags}


%install
make install DESTDIR=%{buildroot}


%files
%doc ChangeLog COPYING README TODO
%{_bindir}/osslsigncode


%changelog
* Tue May 14 2013 Igor Vlasenko <viy@altlinux.ru> 1.5.2-alt2_1
- moved to Sysiphus - required by mjg59, requested by mike@

* Fri Apr 26 2013 Igor Vlasenko <viy@altlinux.ru> 1.5.2-alt1_1
- initial fc import

