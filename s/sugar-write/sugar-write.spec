# BEGIN SourceDeps(oneline):
BuildRequires(pre): rpm-macros-fedora-compat
BuildRequires: python-devel
# END SourceDeps(oneline)
Name: sugar-write
Version: 79
Release: alt2_2
Summary: Word processor for Sugar
Group: Graphical desktop/Sugar
License: GPLv2+
URL: http://wiki.sugarlabs.org/go/Activities/Write
Source0: http://download.sugarlabs.org/sources/sucrose/fructose/Write/Write-%{version}.tar.bz2

BuildRequires:  sugar-toolkit
BuildRequires:  sugar-toolkit
BuildRequires:  gettext

Requires: sugar

BuildArch: noarch
Source44: import.info
# speech dispatcher moved to python 3
%filter_from_requires /^python2...speechd./d


%description
The Write activity provides a word processor for the Sugar interface.

%prep
%setup -q -n Write-%{version}

%build
python ./setup.py build

%install
mkdir -p $RPM_BUILD_ROOT%{sugaractivitydir}
python ./setup.py install --prefix=$RPM_BUILD_ROOT/%{_prefix}

%find_lang org.laptop.AbiWordActivity


%files -f  org.laptop.AbiWordActivity.lang
%doc NEWS
%{sugaractivitydir}/Write.activity/


%changelog
* Fri May 10 2013 Igor Vlasenko <viy@altlinux.ru> 79-alt2_2
- dropped speechd python dependency. Need proper python3

* Wed Mar 13 2013 Igor Vlasenko <viy@altlinux.ru> 79-alt1_2
- update from fc18 release

* Wed Nov 28 2012 Igor Vlasenko <viy@altlinux.ru> 79-alt1_1
- new version; import from fc17 release

